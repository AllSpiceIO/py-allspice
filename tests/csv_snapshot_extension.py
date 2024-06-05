import csv
from collections.abc import Iterable
from io import StringIO

from syrupy.extensions.single_file import SingleFileSnapshotExtension, WriteMode


class CSVSnapshotExtension(SingleFileSnapshotExtension):
    _write_mode = WriteMode.TEXT
    _file_extension = "csv"

    def serialize(self, data, **kwargs):
        if not isinstance(data, Iterable):
            raise ValueError("Data must be an iterable")

        output = StringIO()
        first_row = next(iter(data))
        if isinstance(first_row, dict):
            keys = first_row.keys()
            writer = csv.DictWriter(output, fieldnames=keys, lineterminator="\n")
            writer.writeheader()
            writer.writerows(data)
        else:
            writer = csv.writer(output, lineterminator="\n")
            writer.writerows(data)

        return output.getvalue()
