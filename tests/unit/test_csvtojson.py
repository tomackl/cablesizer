import pytest as test
import CableSizer.csvtojson as c2j
from pathlib import Path


path = Path("../test_resources/json_test.csv")


def test_class_csvtojson_open_file():
    expected = [{"A": "1", "B": "2", "C": "3", "D": "4", "E": "5", "F": "6"},
                {"A": "11", "B": "12", "C": "13", "D": "14", "E": "15", "F": "16"}]
    test_cls = c2j.CSVtoJSON(path.resolve())
    test_cls.open_file()
    result = test_cls._csv
    assert expected == result


def test_class_csvtojson_dumps():
    expected = ('[{"A": "1", "B": "2", "C": "3", "D": "4", "E": "5", "F": "6"}, '
                '{"A": "11", "B": "12", "C": "13", "D": "14", "E": "15", "F": "16"}]')
    test_cls = c2j.CSVtoJSON(path.resolve())
    test_cls.open_file()
    test_cls.dumps()
    result = test_cls._json
    assert expected == result


def test_class_csvtojson_loads():
    expected = [{"A": "1", "B": "2", "C": "3", "D": "4", "E": "5", "F": "6"},
                {"A": "11", "B": "12", "C": "13", "D": "14", "E": "15", "F": "16"}]
    test_cls = c2j.CSVtoJSON(path.resolve())
    test_cls.open_file()
    test_cls.dumps()
    result = test_cls.loads()
    assert expected == result
