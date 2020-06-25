import pytest as test
# import CSVtoJSON.csvtojson as c2j
import csvtojson.csvtojson as c2j
from pathlib import Path


def test_check_fp():
    """
    Test that the file check works as intended.
    :return:
    """
    pass


def test_class_csvtojson_open_file():
    path = Path("../test_resources/json_test.csv")
    expected = [{"A": "1", "B": "2", "C": "3", "D": "4", "E": "5", "F": "6"},
                {"A": "11", "B": "12", "C": "13", "D": "14", "E": "15", "F": "16"}]
    test_cls = c2j.CSVtoJSON(path.resolve())
    test_cls.open_file()
    result = test_cls._csv
    assert expected == result


def test_class_csvtojson_dumps():
    path = Path("../test_resources/json_test.csv")
    expected = ('[{"A": "1", "B": "2", "C": "3", "D": "4", "E": "5", "F": "6"}, '
                '{"A": "11", "B": "12", "C": "13", "D": "14", "E": "15", "F": "16"}]')
    test_cls = c2j.CSVtoJSON(path.resolve())
    test_cls.open_file()
    test_cls.dumps()
    result = test_cls._json
    assert expected == result


def test_class_csvtojson_loads():
    path = Path("../test_resources/json_test.csv")
    expected = [{"A": "1", "B": "2", "C": "3", "D": "4", "E": "5", "F": "6"},
                {"A": "11", "B": "12", "C": "13", "D": "14", "E": "15", "F": "16"}]
    test_cls = c2j.CSVtoJSON(path.resolve())
    test_cls.open_file()
    test_cls.dumps()
    result = test_cls.loads()
    assert expected == result
