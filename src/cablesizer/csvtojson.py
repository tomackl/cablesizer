import csv as csv
import json as json
import pathlib as path


class CSVtoJSON:
    """
    A class to convert csv to json. It takes a csv and returns a json representation.
    """
    def __init__(self, fp: str = False, csv: str = False):
        """
        Initialise the object.
        :param fp: File path to the .csv file.
        :param csv: A reference to a .csv file that has been stored in memory.
        """
        self._json = None
        if fp:
            self._fp = path.Path(fp)
        if csv:
            self._csv = csv
        else:
            self._csv = []

    def open_file(self):
        """
        Open the csv file and save the contents as a list of dictionaries.
        """
        with open(self._fp, newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self._csv.append(row)

    def dumps(self):
        """
        Convert self._csv to JSON.
        """
        self._json = json.dumps(self._csv)

    def loads(self):
        """
        Convert self._json to dictionary.
        :return: dict
        """
        return json.loads(self._json)
