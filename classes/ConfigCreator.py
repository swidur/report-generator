import json
import os
from types import SimpleNamespace

from classes.Exceptions.FileTooBigError import FileTooBigError
from classes.ReportConfig import ReportConfig

FILE_SIZE_LIMIT = 100


class ConfigCreator:
    def __init__(self):
        pass

    def parse_json(self, to_parse):
        """
        Pareses given string from JSON and returns ReportConfig object
        :param to_parse:
        :return:
        """
        json_string = str(self.stringify_file(to_parse))
        json_object = json.loads(json_string, object_hook=lambda d: SimpleNamespace(**d))

        title = database = sql = headers = style = row_numbering = pdf_password = None
        try:
            title = json_object.report.title
            database = json_object.report.database
            sql = json_object.report.sql
            headers = json_object.report.headers
            style = json_object.report.style
            row_numbering = json_object.report.rowNumbering
            pdf_password = json_object.report.pdfPassword
        except Exception as ex:
            print(ex.__str__())

        if (database or sql) is None:
            raise AttributeError(f"One of following arguments not supplied: database: {database}, sql: {sql}")

        if style != "default":
            style = f"<style>{self.stringify_file(style)}</style>"

        return ReportConfig(title, database, sql, headers, style, pdf_password, row_numbering)

    def stringify_file(self, file_path):
        """
        Opens file and returns its content as a string if file size < FILE_SIZE_LIMIT
        :param file_path:
        :return:
        """
        file_size = os.stat(file_path).st_size / 1024
        if file_size > FILE_SIZE_LIMIT:
            raise FileTooBigError(f"Attempt to open file bigger than {FILE_SIZE_LIMIT}", file_size)
        try:
            with open(file_path, "r", encoding="UTF-8") as json_file:
                return json_file.read().replace("\n", "")
        except FileNotFoundError:
            raise FileNotFoundError(file_path)
