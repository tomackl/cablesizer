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
                              "default": "1pr"
                              })


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


size_list = {"mm2": ["0", "1", "1.5", "2.5", "4"], "awg": ["0000", "000", "1"]}
min_size = "1"
min_single_core_size = "1.5"
unit = {"description": ["MM2", "AWG"], "default": "MM2"}


@pytest.mark.parametrize('t_size_list,key,expected',
                         [(size_list, None, {"MM2": ["0", "1", "1.5", "2.5", "4"],
                                             "AWG": ["0000", "000", "1"]}
                           ),
                          (size_list, "mm2", {"MM2": ["0", "1", "1.5", "2.5", "4"]}),
                          (None, None, None)]
                          # (None, "mm2", None)]
                         )
def test_cls_sizes_size_list_dict(t_size_list, key, expected):
    test_class = defaults.Sizes(size_list=t_size_list)
    expected = expected
    result = test_class.get_size_list_dict(key)
    assert result == expected


def test_cls_sizes_get_size_list_dict():
    test_class = defaults.Sizes()
    with pytest.raises(TypeError):
        test_class.get_size_list_dict(key="mm2")


def test_cls_sizes_list():
    test_class = defaults.Sizes(size_list=size_list, unit_description=unit["description"], unit_default=unit["default"])
    expected = ["0", "1", "1.5", "2.5", "4"]
    result = test_class.size_list
    assert result == expected


def test_cls_sizez_min_size():
    test_class = defaults.Sizes()
    test_class.min_size = "1.5"
    expected = "1.5"
    result = test_class.min_size
    assert result == expected
