import pytest
import Constants.configuration as import_constants


def test_import_cable_config():
    """
    Import the cable configuration values. These configuration values are user settable.
    :return:
    """
    path = "../../src/Constants/cable.json"
    cable_config = import_constants.import_json_config(path)
    result = cable_config["cable"]["default"]
    expected = "POWER"
    assert expected == result

