#! /usr/bin/env python3

# generate_attribute_types.py
#
# This script generates type hints for attributes of the API Objects. This is
# necessary because attributes for API Objects are dynamically generated from
# the JSON response of the API.
#
# This script runs the pytest suite, hooks the `parse_response` function of the
# API Objects using sys.setprofile, and collects attributes it has observed.
#
# This script depends on MonkeyType (https://github.com/Instagram/MonkeyType)
# and LibCST (https://github.com/Instagram/LibCST) to generate the type hints.
# We can't use MonkeyType directly because it doesn't support stubbing
# attributes, as they can change at any time. We know that API object attribute
# types stay consistent after they are set by `parse_response`, so we can use
# this script to generate type hints for them


import logging
import sys
from contextlib import contextmanager
from types import NoneType
from typing import Any

import libcst as cst
import monkeytype.cli
import monkeytype.stubs
import monkeytype.typing
import pytest
from libcst.codemod.visitors import ApplyTypeAnnotationsVisitor

HOOKED_FUNCTION_NAME = "parse_response"


logger = logging.getLogger(__name__)


class CustomApplyTypeAnnotationsVisitor(ApplyTypeAnnotationsVisitor):
    """
    This class is a custom patch over LibCST to support adding attribute
    declarations to a class definition.

    This class makes many assumptions that may not hold for a general use case,
    but eventually we should clean this up and upstream it to LibCST.
    """

    def __init__(self, context):
        super().__init__(context)
        self.already_annotated_attributes = set()

    def leave_AnnAssign(
        self,
        original_node: cst.AnnAssign,
        updated_node: cst.AnnAssign,
    ) -> cst.AnnAssign:
        # Right now ApplyTypeAnnotationsVisitor doesn't have a leave_AnnAssign
        # method, but if it does get one in the future we should call it first.
        super_updated_node = updated_node
        if hasattr(super(), "leave_AnnAssign"):
            super_updated_node = super().leave_AnnAssign(original_node, updated_node)

        qualified_name = f"{self._qualifier_name()}.{original_node.target.value}"
        # We don't actually care if this attribute was annotated by the user or
        # the visitor, we just care that it was annotated, as is clear from this
        # being an AnnAssign node.
        self.already_annotated_attributes.add(qualified_name)

        # Now, we check the annotation to see if we need to update it.
        expected_annotation = self.annotations.attributes.get(qualified_name)

        # If we don't have an annotation to add, don't do anything. The user
        # might have made an annotation, and we don't want to remove it.
        if expected_annotation is None:
            return super_updated_node

        if self.overwrite_existing_annotations and (
            super_updated_node.annotation is None
            or super_updated_node.annotation != expected_annotation
        ):
            # With a little qualifier twiddling this should use
            # self._apply_annotation_to_attribute_or_global instead.
            self.already_annotated.add(qualified_name)
            self.annotation_counts.attribute_annotations += 1
            return super_updated_node.with_changes(annotation=expected_annotation)

        return super_updated_node

    def leave_ClassDef(
        self,
        original_node: cst.ClassDef,
        updated_node: cst.ClassDef,
    ) -> cst.ClassDef:
        # When the visitor is done with a class definition, we should add all
        # attribute annotations that haven't been added yet.
        attribute_annotations = []
        qualifier_name = self._qualifier_name() + "."
        for attr, annotation in self.annotations.attributes.items():
            if (
                attr not in self.already_annotated
                and attr not in self.already_annotated_attributes
                and attr.startswith(qualifier_name)
            ):
                self.annotation_counts.attribute_annotations += 1
                name = attr[len(qualifier_name) :]
                assign_node = cst.AnnAssign(
                    target=cst.Name(name),
                    annotation=annotation,
                )
                statement = cst.SimpleStatementLine(body=[assign_node])
                attribute_annotations.append(statement)

        # We need to call the super method to let ApplyTypeAnnotationsVisitor
        # do its work. We can't do this before this point because we need the
        # qualifier name, which the super method un-sets.
        updated_node = super().leave_ClassDef(original_node, updated_node)
        updated_body = list(updated_node.body.body)
        docstring = updated_node.get_docstring()
        if docstring is not None:
            docstring = updated_body[0]
            updated_body = updated_body[1:]

        # Now, we need to extract the attribute annotations that are already in
        # the class definition, so we can have one nice block of attribute
        # annotations at the top of the class.
        existing_attribute_annotations = []
        body_statements = []

        for body_element in updated_body:
            if isinstance(body_element, cst.SimpleStatementLine):
                # If the AnnAssign has a value, it was created by the user, and
                # we shouldn't move it. py-allspice has these all over the
                # place, and this script should not be responsible for moving
                # them.
                if (
                    isinstance(body_element.body[0], cst.AnnAssign)
                    and body_element.body[0].value is None
                ):
                    existing_attribute_annotations.append(body_element)
                else:
                    body_statements.append(body_element)
            else:
                body_statements.append(body_element)

        all_attribute_annotations = [*attribute_annotations, *existing_attribute_annotations]
        # Sort the attribute annotations in alphabetical order.
        all_attribute_annotations.sort(key=lambda x: x.body[0].target.value)

        new_body = [docstring] if docstring is not None else []
        new_body.extend(all_attribute_annotations)
        new_body.extend(body_statements)

        return updated_node.with_changes(body=updated_node.body.with_changes(body=new_body))


class LocalRewriter(monkeytype.typing.TypeRewriter):
    """
    Rewrite types to remove the module name if it's `allspice.apiobject`.
    """

    def generic_rewrite(self, typ):
        # This script specifically generates stubs for the allspice.apiobject
        # module, so we don't need to include the module name in the type hints.
        if hasattr(typ, "__module__") and (
            # I'm unsure why libcst thinks datetime is
            # datetime.datetime.datetime, but that adds a spurious import so
            # hacky fix here.
            typ.__module__ == "allspice.apiobject" or typ.__module__ == "datetime"
        ):
            return typ.__name__
        else:
            return super().generic_rewrite(typ)


def extract_attributes_and_types(api_object: Any) -> dict[str, type]:
    """
    Extract all dynamic attributes and their types from an API Object.

    This uses the fact that py-allspice keeps a private attribute of the same
    name along with a getter property for each attribute. This should give us
    only the dynamic attributes.

    :param api_object: The API Object to extract attributes from.
    :return: A dictionary mapping attribute names to their types.
    """

    non_private_methods = set()
    for attr in dir(api_object):
        if not attr.startswith("_"):
            non_private_methods.add(attr)

    attrs_to_types = {}
    for attr in vars(api_object):
        if attr.startswith("_"):
            non_private_name = attr[1:]
            if non_private_name in non_private_methods:
                attr_value = getattr(api_object, attr)
                attr_type = monkeytype.typing.get_type(attr_value, max_typed_dict_size=0)

                attrs_to_types[non_private_name] = attr_type

    return attrs_to_types


def combine_all_observations(
    observations: list[dict[str, type]],
) -> dict[str, type]:
    """
    Combine all observations for a class into a single type.

    :param observations: The observations to combine.
    :return: A dictionary mapping object types to their attributes and types.
    """

    attrs = set()
    for observation in observations:
        for attr in observation:
            attrs.add(attr)
    types_by_attr = {attr: [] for attr in attrs}
    for observation in observations:
        for attr in attrs:
            attr_type = observation.get(attr, NoneType)
            types_by_attr[attr].append(attr_type)

    combined_observation = {}

    for attr, types in types_by_attr.items():
        combined_type = monkeytype.typing.shrink_types(types, max_typed_dict_size=0)
        combined_observation[attr] = combined_type

    return combined_observation


observations: dict[str, list[dict[str, type]]] = {}


def observe(object_type: str, attrs_and_types: dict[str, type]) -> None:
    observations.setdefault(object_type, []).append(attrs_and_types)


def profile_func(frame, event, arg) -> None:
    if event == "return":
        if frame.f_code.co_name == "parse_response":
            # The returned object of parse_response is the API Object
            api_object_type = arg.__class__
            attrs_and_types = extract_attributes_and_types(arg)
            observe(api_object_type, attrs_and_types)


@contextmanager
def custom_profile():
    sys.setprofile(profile_func)
    yield
    sys.setprofile(None)


def main():
    logging.basicConfig(level=logging.INFO)

    logger.info("Running tests to generate attribute types...")
    with custom_profile():
        result = pytest.main(["-qq", "tests/test_api.py"])
        if result != 0:
            logger.error("Tests failed.")
            sys.exit(1)
    logger.info("Tests finished.")

    logger.info("Generating stubs...")

    class_stubs = []
    type_rewriter = monkeytype.typing.ChainedRewriter(
        [
            LocalRewriter(),
            monkeytype.typing.DEFAULT_REWRITER,
        ]
    )
    for object_type, observations_for_object in observations.items():
        combined_observation = combine_all_observations(observations_for_object)
        attribute_stubs = []
        for attr, attr_type in combined_observation.items():
            rewritten_type = type_rewriter.rewrite(attr_type)
            # If the type of an attribute is NoneType, that does not mean that
            # that value will always be None, but that we don't have a test
            # that provides a value for that attribute. So, we should rewrite
            # NoneType to Any to avoid making an assertion that the attribute
            # will always be None. A type rewriter would shrink this further,
            # leading to worse types, so we do this manually.
            if rewritten_type is None or rewritten_type == type(None):
                rewritten_type = Any

            attribute_stub = monkeytype.stubs.AttributeStub(attr, rewritten_type)
            attribute_stubs.append(attribute_stub)
        class_stub = monkeytype.stubs.ClassStub(
            object_type.__name__, attribute_stubs=attribute_stubs
        )
        class_stubs.append(class_stub)
    module_stub = monkeytype.stubs.ModuleStub(class_stubs=class_stubs)

    logger.info("Generated module stub.")

    logger.info("Applying module stub types to module file...")

    with open("./allspice/apiobject.py", "r") as f:
        source = f.read()

    stub_module = cst.parse_module(module_stub.render())
    source_module = cst.parse_module(source)
    context = cst.codemod.CodemodContext()
    CustomApplyTypeAnnotationsVisitor.store_stub_in_context(
        context,
        stub_module,
        overwrite_existing_annotations=True,
    )
    visitor = CustomApplyTypeAnnotationsVisitor(context)
    patched_source = visitor.transform_module(source_module)

    with open("./allspice/apiobject.py", "w") as f:
        f.write(patched_source.code)

    logger.info("Applied stubs to module file.")

    logger.info("Attribute type generation complete.")


if __name__ == "__main__":
    main()
