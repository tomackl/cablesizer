import pytest
import CableSizer.defaults as defaults
import pprint as pp


def test_cls_cable_run_defaults():
    # test_class = defaults.CableRun("../../src/Constants/cable.json")
    pass
    # for each in [test_class.cable, test_class.circuit, test_class.installation, test_class.power_unit]:
    #     pp.pprint(each)


def test_cls_core_arrangement_defaults():
    test_class = defaults.CoreArrangement()
    test_class.from_dict({"description": ["1TRI", "2TRI", "4TRI"],
                          "name": "triple",
                          "abbreviation": "tri",
                          "default": "1tri"}
                         )
    expected = {"description": ["1TRI", "2TRI", "4TRI"],
                "name": "TRIPLE",
                "abbreviation": "TRI",
                "default": "1TRI"}
    result = test_class.to_dict()
    assert result == expected


def test_cls_core_arrangement_exception():
    test_class = defaults.CoreArrangement()
    with pytest.raises(ValueError):
        test_class.from_dict({"description": ["1TRI", "2TRI", "4TRI"],
                              "name": "triple",
                              "abbreviation": "tri",
                              "default": "1pr"}
                             )


def test_cls_basic_defaults():
    test_class = defaults.BasicDefaults()
    test_class.from_dict({"description": ["CIRCULAR", "FLAT"],
                          "default": "circular"})
    expected = {"description": ["CIRCULAR", "FLAT"],
                "default": "CIRCULAR"}
    result = test_class.to_dict()
    assert result == expected


def test_cls_basic_defaults_exception():
    test_class = defaults.BasicDefaults()
    with pytest.raises(ValueError):
        test_class.from_dict({"description": ["CIRCULAR", "FLAT"],
                              "default": "triangle"})
