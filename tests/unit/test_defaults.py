import pytest
import CableSizer.defaults as defaults
import pprint as pp


def test_cls_cable_run_defaults():
    test_class = defaults.CableRun("../../src/Constants/cable.json")
    for each in [test_class.cable, test_class.circuit, test_class.installation, test_class.power_unit]:
        pp.pprint(each)
