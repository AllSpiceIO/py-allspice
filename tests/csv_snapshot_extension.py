import csv
from collections.abc import Iterable
from io import StringIO

from syrupy.extensions.single_file import SingleFileSnapshotExtension, WriteMode


class CSVSnapshotExtension(SingleFileSnapshotExtension):
    """
    A Syrupy snapshot extension that generates CSV files.

    This extension can only work with two types of data:

    1. An `Iterable` of iterables of strings or objects convertible to strings,
       which will be written as rows in the CSV file.
    2. An `Iterable` of dictionaries, where each dictionary will be written as a
       row in the CSV file. The keys of the first dictionary will be used as
       the header row. This uses csv.DictWriter to write the data, so all
       usual caveats about that apply.

    This extension will raise a ValueError for any other type of data.
    """

    _write_mode = WriteMode.TEXT
    _file_extension = "csv"

    def serialize(self, data, **_):
        if not isinstance(data, Iterable):
            raise ValueError("Data must be an iterable")

        output = StringIO()
        first_row = next(iter(data))
        if isinstance(first_row, dict):
            keys = first_row.keys()
            writer = csv.DictWriter(output, fieldnames=sorted(keys), lineterminator="\n")
            writer.writeheader()
            writer.writerows(data)
        else:
            writer = csv.writer(output, lineterminator="\n")
            writer.writerows(data)

        return output.getvalue()
