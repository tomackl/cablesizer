import pytest
import Constants.import_constants as import_constants
import pathlib as path

def test_import_cable_config():
    """
    Import the cable configuration values. These configuration values are user settable.
    :return:
    """

    cable_config = import_constants.import_cable_config()
    result = cable_config["cable"]["default "]
    expected = "POWER"
    assert expected == result

