import pytest
import CableSizer.cable as cable
import datetime as dt


def test_cls_cablespec():
    test_class = cable.CableSpec(run_type='multi', max_parallel=2, allow_parallel_multicore=True, shape="circular",
                                 conductor_material="CU", min_size=4.0, core_arrangement='multi', sheath='none',
                                 insulation_material='xlpe', insulation_code='x-90', operating_temp=45,
                                 max_operating_temp=90, armour='dwa', screen_cable='nil', screen_core='is',
                                 volt_rating='0.6/1kv', flexible=False, vd_max=(round(433*.05, 2)), vd=0.0)
    expected = ("MULTI", 2, True, "CIRCULAR", "CU", 4.0, "MULTI", "NONE", "XLPE", "X-90", 45, 90, "DWA", "NIL", "IS",
                "0.6/1KV", False, 21.65, 0.0)
    result = (test_class.type, test_class.max_parallel, test_class.allow_parallel_multicore, test_class.shape,
              test_class.conductor_material, test_class.min_size, test_class.core_arrangement, test_class.sheath,
              test_class.insulation_material, test_class.insulation_code, test_class.operating_temp,
              test_class.maximum_operating_temp, test_class.armour, test_class.screen_cable, test_class.screen_core,
              test_class.volt_rating, test_class.flexible, test_class.vd_max, test_class.vd)
    assert result == expected


def test_cls_cablespec_dict():
    test_class = cable.CableSpec()
    test_class.from_dict({"cable_type": "multi",
                          "max_parallel": 2,
                          "allow_parallel_multicore": True,
                          "shape": "CIRCULAR",
                          "conductor_material": "CU",
                          "min_size": 4.0,
                          "core_arrangement": "multi",
                          "sheath": "none",
                          "insulation_material": "xlpe",
                          "insulation_code": "X-90",
                          "operating_temp": 45,
                          "maximum_operating_temp": 90,
                          "armour": "DWA",
                          "screen_cable": "nil",
                          "screen_core": "is",
                          "volt_rating": "0.6/1KV",
                          "flexible": False,
                          "vd_max": 21.65,
                          "vd": 0.0
                          })
    expected = {"cable_type": "MULTI",
                "max_parallel": 2,
                "allow_parallel_multicore": True,
                "shape": "CIRCULAR",
                "conductor_material": "CU",
                "min_size": 4.0,
                "core_arrangement": "MULTI",
                "sheath": "NONE",
                "insulation_material": "XLPE",
                "insulation_code": "X-90",
                "operating_temp": 45,
                "maximum_operating_temp": 90,
                "armour": "DWA",
                "screen_cable": "NIL",
                "screen_core": "IS",
                "volt_rating": "0.6/1KV",
                "flexible": False,
                "vd_max": 21.65,
                "vd": 0.0
                }
    result = test_class.to_dict()
    assert result == expected


def test_cls_to_cable():
    test_class = cable.Cable(cable_type="power", active_size=0.0, active_number=0, active_unit="", active_name="",
                             neutral_size=0.0, neutral_number=0, neutral_unit="", neutral_name="", earth_size=0.0,
                             earth_number=0, earth_unit="", earth_name="", instrument_size=0.0, instrument_number=0,
                             instrument_unit="", instrument_name="", control_size=0.0, control_number=0,
                             control_unit="", control_name="", communication_size=0.0, communication_number=0,
                             communication_unit="", communication_name="", data_size=0.0, data_number=0, data_unit="",
                             data_name="", unenclosed_spaced_ccc=0, unenclosed_spaced_install_temp=0,
                             unenclosed_spaced_arrangement="", unenclosed_surface_ccc=0,
                             unenclosed_surface_install_temp=0, unenclosed_surface_arrangement="",
                             unenclosed_touching_ccc=0, unenclosed_touching_install_temp=0,
                             unenclosed_touching_arrangement="", enclosed_conduit_ccc=0,
                             enclosed_conduit_install_temp=0, enclosed_conduit_arrangement="", enclosed_partial_ccc=0,
                             enclosed_partial_install_temp=0, enclosed_partial_arrangement="", enclosed_complete_ccc=0,
                             enclosed_complete_install_temp=0, enclosed_complete_arrangement="", buried_direct_ccc=0,
                             buried_direct_install_temp=0, buried_direct_arrangement="", ducts_single_ccc=0,
                             ducts_single_install_temp=0, ducts_single_arrangement="", ducts_per_cable_ccc=0,
                             ducts_per_cable_install_temp=0, ducts_per_cable_arrangement="", mvam=0.0, r=0.0, r_unit="",
                             x=0.0, x_unit="", z=0.0, z_unit="", cable_screen_type="", cable_screen_withstand=0,
                             core_screen_type="", core_screen_withstand=0, core_arrangement="", cable_shape="",
                             conductor_material="", cable_sheath="", insulation_material="", insulation_code="",
                             cont_conductor_temp=0, max_conductor_temp=0, circuit_type="", volt_rating="", armour=None,
                             description="", flexible=False)
    expected = ("POWER", 0.0, 0, "", "", 0.0, 0, "", "", 0.0, 0, "", "", 0.0, 0, "", "", 0.0, 0, "", "", 0.0, 0, "", "",
                0.0, 0, "", "", 0, 0, "", 0, 0, "", 0, 0, "", 0, 0, "", 0, 0, "", 0, 0, "", 0, 0, "", 0, 0, "", 0, 0,
                "", 0.0, 0.0, "", 0.0, "", 0.0, "", "", 0, "", 0, "", "", "", "", "", "", 0, 0, "", "", None, "", False)
    result = (test_class.cable_type, test_class.activeCores.size, test_class.activeCores.number,
              test_class.activeCores.unit, test_class.activeCores.name, test_class.neutralCores.size,
              test_class.neutralCores.number, test_class.neutralCores.unit, test_class.neutralCores.name,
              test_class.earthCores.size, test_class.earthCores.number, test_class.earthCores.unit,
              test_class.earthCores.name, test_class.instrumentCores.size, test_class.instrumentCores.number,
              test_class.instrumentCores.unit, test_class.instrumentCores.name, test_class.controlCores.size,
              test_class.controlCores.number, test_class.controlCores.unit, test_class.controlCores.name,
              test_class.communicationCores.size, test_class.communicationCores.number,
              test_class.communicationCores.unit, test_class.communicationCores.name, test_class.dataCores.size,
              test_class.dataCores.number, test_class.dataCores.unit, test_class.dataCores.name,
              test_class.unenclosedSpaced.ccc, test_class.unenclosedSpaced.install_temp,
              test_class.unenclosedSpaced.cable_arrangement, test_class.unenclosedSurface.ccc,
              test_class.unenclosedSurface.install_temp, test_class.unenclosedSurface.cable_arrangement,
              test_class.unenclosedTouching.ccc, test_class.unenclosedTouching.install_temp,
              test_class.unenclosedTouching.cable_arrangement, test_class.enclosedConduit.ccc,
              test_class.enclosedConduit.install_temp, test_class.enclosedConduit.cable_arrangement,
              test_class.enclosedPartial.ccc, test_class.enclosedPartial.install_temp,
              test_class.enclosedPartial.cable_arrangement, test_class.enclosedComplete.ccc,
              test_class.enclosedComplete.install_temp, test_class.enclosedComplete.cable_arrangement,
              test_class.buriedDirect.ccc, test_class.buriedDirect.install_temp,
              test_class.buriedDirect.cable_arrangement, test_class.ductsSingle.ccc,
              test_class.ductsSingle.install_temp, test_class.ductsSingle.cable_arrangement,
              test_class.ductsPerCable.ccc, test_class.ductsPerCable.install_temp,
              test_class.ductsPerCable.cable_arrangement, test_class.impedance.mvam, test_class.impedance.r,
              test_class.impedance.r_unit, test_class.impedance.x, test_class.impedance.x_unit, test_class.impedance.z,
              test_class.impedance.z_unit, test_class.cableScreen.name, test_class.cableScreen.fault_withstand,
              test_class.coreScreen.name, test_class.coreScreen.fault_withstand, test_class.core_arrangement,
              test_class.shape, test_class.conductor_material, test_class.sheath, test_class.insulation.material,
              test_class.insulation.code, test_class.insulation.op_temp, test_class.insulation.max_temp,
              test_class.circuit_type, test_class.voltage_rating, test_class.armour, test_class.description,
              test_class.flexible)
    assert result == expected


def test_cls_cable_dict():
    test_class = cable.Cable(cable_type="control", active_size=0.0, active_number=0, active_unit="", active_name="",
                             neutral_size=0.0, neutral_number=0, neutral_unit="", neutral_name="",
                             earth_size=0.0, earth_number=0, earth_unit="", earth_name="",
                             instrument_size=0.0, instrument_number=0, instrument_unit="", instrument_name="",
                             control_size=1.0, control_number=20, control_unit="mm2", control_name="core",
                             communication_size=0.0, communication_number=0, communication_unit="",
                             communication_name="",
                             data_size=0.0, data_number=0, data_unit="", data_name="",
                             mvam=0.0, r=0.0, r_unit="", x=0.0, x_unit="", z=0.0, z_unit="",
                             unenclosed_spaced_ccc=0, unenclosed_spaced_install_temp=0,
                             unenclosed_spaced_arrangement="",
                             unenclosed_surface_ccc=0, unenclosed_surface_install_temp=0,
                             unenclosed_surface_arrangement="",
                             unenclosed_touching_ccc=0, unenclosed_touching_install_temp=0,
                             unenclosed_touching_arrangement="",
                             enclosed_conduit_ccc=0, enclosed_conduit_install_temp=0, enclosed_conduit_arrangement="",
                             enclosed_partial_ccc=0, enclosed_partial_install_temp=0, enclosed_partial_arrangement="",
                             enclosed_complete_ccc=0, enclosed_complete_install_temp=0,
                             enclosed_complete_arrangement="", buried_direct_ccc=0, buried_direct_install_temp=0,
                             buried_direct_arrangement="", ducts_single_ccc=0, ducts_single_install_temp=0,
                             ducts_single_arrangement="", ducts_per_cable_ccc=0, ducts_per_cable_install_temp=0,
                             ducts_per_cable_arrangement="", cable_screen_type="", cable_screen_withstand=0,
                             core_screen_type="", core_screen_withstand=0, insulation_material="", insulation_code="",
                             cont_conductor_temp=0, max_conductor_temp=0, cable_sheath="", volt_rating="",
                             flexible=False, armour=None, rev_number="", rev_date=None, description="",
                             core_arrangement="", cable_shape="", conductor_material="", circuit_type="")
    expected = {"cable_type": "CONTROL",
                "active_cores": {
                    "size": 0.0, "key": "", "number": 0, "name": ""
                },
                "neutral_cores": {
                    "size": 0.0, "key": "", "number": 0, "name": ""
                },
                "earth_cores": {
                    "size": 0.0, "key": "", "number": 0, "name": ""
                },
                "instrument_cores": {
                    "size": 0.0, "key": "", "number": 0, "name": ""
                },
                "control_cores": {
                    "size": 1.0, "key": "MM2", "number": 20, "name": "CORE"
                },
                "communication_cores": {
                    "size": 0.0, "key": "", "number": 0, "name": ""
                },
                "data_cores": {
                    "size": 0.0, "key": "", "number": 0, "name": ""
                },
                "unenclosed_spaced": {
                    "ccc": 0,
                    "install_temp": 0,
                    "arrangement": ""
                },
                "unenclosed_surface": {
                    "ccc": 0,
                    "install_temp": 0,
                    "arrangement": ""
                },
                "unenclosed_touching": {
                    "ccc": 0,
                    "install_temp": 0,
                    "arrangement": ""
                },
                "enclosed_conduit": {
                    "ccc": 0,
                    "install_temp": 0,
                    "arrangement": ""
                },
                "enclosed_partial": {
                    "ccc": 0,
                    "install_temp": 0,
                    "arrangement": ""
                },
                "enclosed_complete": {
                    "ccc": 0,
                    "install_temp": 0,
                    "arrangement": ""
                },
                "buried_direct": {
                    "ccc": 0,
                    "install_temp": 0,
                    "arrangement": ""
                },
                "ducts_single": {
                    "ccc": 0,
                    "install_temp": 0,
                    "arrangement": ""
                },
                "ducts_per_cable": {
                    "ccc": 0,
                    "install_temp": 0,
                    "arrangement": ""
                },
                "impedance": {
                    "mvam": 0.0, "r": 0.0, "r_unit": "", "x": 0.0, "x_unit": "", "z": 0.0, "z_unit": ""
                },
                "cable_screen": {
                    "name": "",
                    "fault_withstand": 0
                },
                "core_screen": {
                    "name": "",
                    "fault_withstand": 0
                },
                "insulation": {
                    "material": "",
                    "code": "",
                    "op_temp": 0,
                    "max_temp": 0
                },
                "sheath": "", "volt_rating": "", "flexible": False, "armour": None,
                "revision": {
                    "number": "",
                    "date": None
                },
                "description": "", "circuit_type": "", "conductor_material": "", "core_arrangement": "",
                "cable_shape": ""
                }
    result = test_class.to_dict()
    assert result == expected


def test_cls_cable_from_dict():
    test_class = cable.Cable()
    expected = ("INSTRUMENT", 0.0, 0, "", "", 0.0, 0, "", "", 0.0, 0, "", "", 0.0, 0, "", "", 1.0, 20, "MM2", "CORE",
                0.0, 0, "", "", 0.0, 0, "", "", 0, 0, "", 0, 0, "", 0, 0, "", 0, 0, "", 0, 0, "", 0, 0, "", 0, 0, "", 0,
                0, "", 0, 0, "", 0.0, 0.0, "", 0.0, "", 0.0, "", "", 0, "", 0, "", "", "", "", "", "", 0, 0, "", "",
                None, "", False)
    details = {"cable_type": "instrument",
               "active_cores": {
                   "size": 0.0, "key": "", "number": 0, "name": ""
               },
               "neutral_cores": {
                   "size": 0.0, "key": "", "number": 0, "name": ""
               },
               "earth_cores": {
                   "size": 0.0, "key": "", "number": 0, "name": ""
               },
               "instrument_cores": {
                   "size": 0.0, "key": "", "number": 0, "name": ""
               },
               "control_cores": {
                   "size": 1.0, "key": "MM2", "number": 20, "name": "CORE"
               },
               "communication_cores": {
                   "size": 0.0, "key": "", "number": 0, "name": ""
               },
               "data_cores": {
                   "size": 0.0, "key": "", "number": 0, "name": ""
               },
               "unenclosed_spaced": {
                   "ccc": 0,
                   "install_temp": 0,
                   "arrangement": ""
               },
               "unenclosed_surface": {
                   "ccc": 0,
                   "install_temp": 0,
                   "arrangement": ""
               },
               "unenclosed_touching": {
                   "ccc": 0,
                   "install_temp": 0,
                   "arrangement": ""
               },
               "enclosed_conduit": {
                   "ccc": 0,
                   "install_temp": 0,
                   "arrangement": ""
               },
               "enclosed_partial": {
                   "ccc": 0,
                   "install_temp": 0,
                   "arrangement": ""
               },
               "enclosed_complete": {
                   "ccc": 0,
                   "install_temp": 0,
                   "arrangement": ""
               },
               "buried_direct": {
                   "ccc": 0,
                   "install_temp": 0,
                   "arrangement": ""
               },
               "ducts_single": {
                   "ccc": 0,
                   "install_temp": 0,
                   "arrangement": ""
               },
               "ducts_per_cable": {
                   "ccc": 0,
                   "install_temp": 0,
                   "arrangement": ""
               },
               "impedance": {
                   "mvam": 0.0, "r": 0.0, "r_unit": "", "x": 0.0, "x_unit": "", "z": 0.0, "z_unit": ""
               },
               "cable_screen": {
                   "name": "",
                   "fault_withstand": 0
               },
               "core_screen": {
                   "name": "",
                   "fault_withstand": 0
               },
               "insulation": {
                   "material": "",
                   "code": "",
                   "op_temp": 0,
                   "max_temp": 0
               },
               "sheath": "", "volt_rating": "", "flexible": False, "armour": None,
               "revision": {
                   "number": "",
                   "date": None
               },
               "description": "", "circuit_type": "", "conductor_material": "", "core_arrangement": "",
               "cable_shape": ""
               }
    test_class.from_dict(details)
    result = (test_class.cable_type, test_class.activeCores.size, test_class.activeCores.number,
              test_class.activeCores.unit, test_class.activeCores.name, test_class.neutralCores.size,
              test_class.neutralCores.number, test_class.neutralCores.unit, test_class.neutralCores.name,
              test_class.earthCores.size, test_class.earthCores.number, test_class.earthCores.unit,
              test_class.earthCores.name, test_class.instrumentCores.size, test_class.instrumentCores.number,
              test_class.instrumentCores.unit, test_class.instrumentCores.name, test_class.controlCores.size,
              test_class.controlCores.number, test_class.controlCores.unit, test_class.controlCores.name,
              test_class.communicationCores.size, test_class.communicationCores.number,
              test_class.communicationCores.unit, test_class.communicationCores.name, test_class.dataCores.size,
              test_class.dataCores.number, test_class.dataCores.unit, test_class.dataCores.name,
              test_class.unenclosedSpaced.ccc, test_class.unenclosedSpaced.install_temp,
              test_class.unenclosedSpaced.cable_arrangement, test_class.unenclosedSurface.ccc,
              test_class.unenclosedSurface.install_temp, test_class.unenclosedSurface.cable_arrangement,
              test_class.unenclosedTouching.ccc, test_class.unenclosedTouching.install_temp,
              test_class.unenclosedTouching.cable_arrangement, test_class.enclosedConduit.ccc,
              test_class.enclosedConduit.install_temp, test_class.enclosedConduit.cable_arrangement,
              test_class.enclosedPartial.ccc, test_class.enclosedPartial.install_temp,
              test_class.enclosedPartial.cable_arrangement, test_class.enclosedComplete.ccc,
              test_class.enclosedComplete.install_temp, test_class.enclosedComplete.cable_arrangement,
              test_class.buriedDirect.ccc, test_class.buriedDirect.install_temp,
              test_class.buriedDirect.cable_arrangement, test_class.ductsSingle.ccc,
              test_class.ductsSingle.install_temp, test_class.ductsSingle.cable_arrangement,
              test_class.ductsPerCable.ccc, test_class.ductsPerCable.install_temp,
              test_class.ductsPerCable.cable_arrangement, test_class.impedance.mvam, test_class.impedance.r,
              test_class.impedance.r_unit, test_class.impedance.x, test_class.impedance.x_unit, test_class.impedance.z,
              test_class.impedance.z_unit, test_class.cableScreen.name, test_class.cableScreen.fault_withstand,
              test_class.coreScreen.name, test_class.coreScreen.fault_withstand, test_class.core_arrangement,
              test_class.shape, test_class.conductor_material, test_class.sheath, test_class.insulation.material,
              test_class.insulation.code, test_class.insulation.op_temp, test_class.insulation.max_temp,
              test_class.circuit_type, test_class.voltage_rating, test_class.armour, test_class.description,
              test_class.flexible)
    assert result == expected


def test_cls_cable_csa():
    test_class = cable.Cable(active_size=35.0)
    result = test_class.csa
    expected = {"POWER": 35.0,
                "NEUTRAL": 0.0,
                "EARTH": 0.0,
                "CONTROL": 0.0,
                "INSTRUMENT": 0.0,
                "DATA": 0.0,
                "COMMUNICATION": 0.0,
                }
    assert result == expected


@pytest.mark.parametrize("install_ccc_test, install_method, test_amp",
                         [(cable.Cable(unenclosed_spaced_ccc=16), "unenclosedSpaced", 16),
                          (cable.Cable(unenclosed_surface_ccc=20), "unenclosedsuRface", 20),
                          (cable.Cable(unenclosed_touching_ccc=150), "unenclosedtouching", 150),
                          (cable.Cable(enclosed_conduit_ccc=65), "encloseDconduit", 65),
                          (cable.Cable(enclosed_partial_ccc=87), "enclosedpartial", 87),
                          (cable.Cable(enclosed_complete_ccc=94), "ENCLOSEDCOMPLETE", 94),
                          (cable.Cable(buried_direct_ccc=29), "burieddirect", 29),
                          (cable.Cable(ducts_single_ccc=45), "ductssingle", 45),
                          (cable.Cable(ducts_per_cable_ccc=450), "ductsperCABLE", 450),
                          (cable.Cable(unenclosed_spaced_ccc=16), "unenclosed_Spaced", 16),
                          (cable.Cable(unenclosed_surface_ccc=20), "unenclosed_suRface", 20),
                          (cable.Cable(unenclosed_touching_ccc=150), "unenclosed_touching", 150),
                          (cable.Cable(enclosed_conduit_ccc=65), "encloseD_conduit", 65),
                          (cable.Cable(enclosed_partial_ccc=87), "enclosed_partial", 87),
                          (cable.Cable(enclosed_complete_ccc=94), "ENCLOSED_COMPLETE", 94),
                          (cable.Cable(buried_direct_ccc=29), "buried_direct", 29),
                          (cable.Cable(ducts_single_ccc=45), "ducts_single", 45),
                          (cable.Cable(ducts_per_cable_ccc=450), "ducts_per_CABLE", 450)
                          ])
def test_cls_cable_find_ccc(install_ccc_test, install_method, test_amp):
    test_class = install_ccc_test
    result = test_class.installation_ccc(install_method)
    expected = test_amp
    assert result == expected


def test_cls_cable_mvam():
    test_class = cable.Cable()
    test_class.mvam = 0.123
    result = test_class.mvam
    expected = 0.123
    assert result == expected


def test_cls_cable_installation_method():
    test_class = cable.CableInstallationMethod()
    test_class.ccc = 140
    test_class.install_temp = 45
    test_class.cable_arrangement = 'trefoil'
    expected = (140, 45, "TREFOIL")
    result = (test_class.ccc, test_class.install_temp, test_class.cable_arrangement)
    assert result == expected


def test_cls_cable_installation_method_to_dict():
    test_class = cable.CableInstallationMethod(140, 45, "trefoil")
    expected = {"ccc": 140, "install_temp": 45, "arrangement": "TREFOIL"}
    result = test_class.to_dict()
    assert result == expected


def test_cls_cable_installation_method_from_dict():
    test_class = cable.CableInstallationMethod()
    expected = (140, 45, "TREFOIL")
    test_class.from_dict({"ccc": 140, "install_temp": 45, "arrangement": "trefoil"})
    result = (test_class.ccc, test_class.install_temp, test_class.cable_arrangement)
    assert result == expected


def test_cls_cable_run():
    test_class = cable.CableRun(required_ccc=10, derating_run=0.8)
    expected = (10.0, 0.8)
    result = (test_class.required_ccc, test_class.derate_run)
    assert result == expected


def test_cls_cable_screen():
    test_class = cable.Screen()
    test_class.name = "dwt"
    test_class.fault_withstand = int(10e6)
    expected = ("DWT", 10000000)
    result = (test_class.name, test_class.fault_withstand)
    assert result == expected


def test_cls_circuit_type():
    test_class = cable.Circuit(circuit_type='power')
    expected = "POWER"
    result = test_class.circuit_type
    assert result == expected


def test_cls_circuit_voltage():
    test_class = cable.Circuit(voltage=22, voltage_unit='kv', phases=4, neutral_required=True)
    expected = (22, 'KV', 4, True)
    result = (test_class.voltage.v, test_class.voltage.unit, test_class.voltage.phases,
              test_class.voltage.neutral_required)
    assert result == expected


def test_cls_circuit_dict():
    test_class = cable.Circuit(circuit_type="power", voltage=22, voltage_unit='kv', frequency=50, frequency_unit="hz",
                               waveform="ac", phases=4, neutral_required=True, physical_method="buried_direct",
                               cable_arrangement="trefoil", load_current=150)
    expected = {"circuit_type": "POWER",
                "voltage": {"v": 22, "key": "KV", "phases": 4, "neutral_required": True},
                "frequency": {"frequency": 50, "key": "HZ", "waveform": "AC"},
                "installation_name": {"installation": "BURIED_DIRECT", "arrangement": "TREFOIL"},
                "load_current": 150
                }
    result = test_class.to_dict()
    assert result == expected


def test_cls_circuit_installation_method():
    test_class = cable.Circuit(physical_method="touching", cable_arrangement='trefoil')
    expected = ("TOUCHING", "TREFOIL")
    result = (test_class.installation.physical_installation, test_class.installation.cable_arrangement)
    assert result == expected


def test_cls_circuit_load_current():
    test_class = cable.Circuit()
    expected = 150
    test_class.load_current = 150
    result = test_class.load_current
    assert result == expected

# def test_cls_cable_run_dict():
#     test_class = cable_list.CableRun(cable_list=[], tag="1234-PU-7890-P1", length=150.0, description="Dewatering pump 7890",
#                                 supply="MCC-1", load="1234-PU-7890", notes="Added 1.1.2019", required_ccc=30.0,
#                                 derating_run=0.8)
#     # todo: complete the below.
#     expected = {"cables": [], "circuit_detail": {}, "conductor": {}, "impedance": {}, "tag": "1234-PU-7890-P1",
#                 "length": 150, "description": "Dewatering pump 7890", "supply": "MCC-1", "load": "1234-PU-7890",
#                 "notes": "Added 1.1.2019", "contracts": {}, "revision": {}, "required_ccc": 150, "derate_run": 0.8
#                 }
#     result = test_class.to_dict()
#     assert result == expected


def test_cls_conductor_detail_size_setter():
    test_class = cable.ConductorDetail()
    test_class.size = 1.5
    expected = 1.5
    result = test_class.size
    assert result == expected


def test_cls_conductor_detail_size_getter():
    test_class = cable.ConductorDetail(size=1.5)
    expected = 1.5
    result = test_class.size
    assert result == expected


def test_cls_conductor_detail_size_unit_setter():
    test_class = cable.ConductorDetail()
    test_class.unit = 'mm2'
    expected = 'MM2'
    result = test_class.unit
    assert result == expected


def test_cls_conductor_detail_size_unit_getter():
    test_class = cable.ConductorDetail(unit='mm2')
    expected = 'MM2'
    result = test_class.unit
    assert result == expected


def test_cls_conductor_detail_to_dict():
    test_class = cable.ConductorDetail(95, "mm2")
    expected = {"size": 95, "key": "MM2"}
    result = test_class.to_dict()
    assert result == expected


def test_cls_conductor_detail_from_dict():
    test_class = cable.ConductorDetail()
    details = {"size": 95, "key": "mm2"}
    test_class.from_dict(details)
    expected = (95, "MM2")
    result = (test_class.size, test_class.unit)
    assert result == expected


def test_cls_conductor_cable_run_size_getter():
    test_class = cable.ConductorCableRun(4, '', 4, '', 1.5, '')
    expected = (4.0, 4.0, 1.5)
    result = (test_class.activeConductors.size, test_class.neutralConductors.size, test_class.earthConductors.size)
    assert result == expected


def test_cls_conductor_cable_run_size_setter():
    test_class = cable.ConductorCableRun()
    test_class.activeConductors.size = 4
    test_class.activeConductors.unit = "mm2"
    test_class.neutralConductors.size = 4
    test_class.neutralConductors.unit = "mm2"
    test_class.earthConductors.size = 1.5
    test_class.earthConductors.unit = "mm2"
    test_class.instrumentationConductors.size = 1.5
    test_class.instrumentationConductors.unit = "mm2"
    test_class.controlConductors.size = 1.5
    test_class.controlConductors.unit = "mm2"
    test_class.dataConductors.size = 0.75
    test_class.dataConductors.unit = "mm2"
    test_class.communicationConductors.size = 1.5
    test_class.communicationConductors.unit = "mm2"
    expected = (4, "MM2", 4, "MM2", 1.5, "MM2", 1.5, "MM2", 1.5, "MM2", 0.75, "MM2", 1.5, "MM2")
    result = (test_class.activeConductors.size, test_class.activeConductors.unit, test_class.neutralConductors.size,
              test_class.neutralConductors.unit, test_class.earthConductors.size, test_class.earthConductors.unit,
              test_class.instrumentationConductors.size, test_class.instrumentationConductors.unit,
              test_class.controlConductors.size, test_class.controlConductors.unit,
              test_class.dataConductors.size, test_class.dataConductors.unit,
              test_class.communicationConductors.size, test_class.communicationConductors.unit
              )
    assert result == expected


def test_cls_conductor_cable_run_to_dict():
    test_class = cable.ConductorCableRun(active_size=4, active_unit="mm2", neutral_size=4, neutral_unit="mm2",
                                         earth_size=1.5, earth_unit="mm2", instrumentation_size=1.5,
                                         instrumentation_unit="mm2", control_size=1.5, control_unit="mm2",
                                         data_size=0.75, data_unit="mm2", communication_size=1.5,
                                         communication_unit="mm2")
    expected = {"active_conductors": {"size": 4, "key": "MM2"},
                "neutral_conductors": {"size": 4, "key": "MM2"},
                "earth_conductors": {"size": 1.5, "key": "MM2"},
                "instrumentation_conductors": {"size": 1.5, "key": "MM2"},
                "communication_conductors": {"size": 1.5, "key": "MM2"},
                "data_conductors": {"size": 0.75, "key": "MM2"},
                "control_conductors": {"size": 1.5, "key": "MM2"},
                }
    result = test_class.to_dict()
    assert result == expected


def test_cls_conductor_cable_run_from_dict():
    test_class = cable.ConductorCableRun(active_size=4, active_unit="mm2", neutral_size=4, neutral_unit="mm2",
                                         earth_size=1.5, earth_unit="mm2", instrumentation_size=1.5,
                                         instrumentation_unit="mm2", control_size=1.5, control_unit="mm2",
                                         data_size=0.75, data_unit="mm2", communication_size=1.5,
                                         communication_unit="mm2")
    expected = (4, "MM2", 4, "MM2", 1.5, "MM2", 1.5, "MM2", 1.5, "MM2", 0.75, "MM2", 1.5, "MM2")
    details = {"active_conductors": {"size": 4, "key": "mm2"},
               "neutral_conductors": {"size": 4, "key": "mm2"},
               "earth_conductors": {"size": 1.5, "key": "mm2"},
               "instrumentation_conductors": {"size": 1.5, "key": "mm2"},
               "communication_conductors": {"size": 1.5, "key": "mm2"},
               "data_conductors": {"size": 0.75, "key": "mm2"},
               "control_conductors": {"size": 1.5, "key": "mm2"},
               }
    test_class.from_dict(details)
    result = (test_class.activeConductors.size, test_class.activeConductors.unit, test_class.neutralConductors.size,
              test_class.neutralConductors.unit, test_class.earthConductors.size, test_class.earthConductors.unit,
              test_class.instrumentationConductors.size, test_class.instrumentationConductors.unit,
              test_class.communicationConductors.size, test_class.communicationConductors.unit,
              test_class.dataConductors.size, test_class.dataConductors.unit, test_class.controlConductors.size,
              test_class.controlConductors.unit)
    assert result == expected


def test_cls_conductor_cable_run_size_unit_getter():
    test_class = cable.ConductorCableRun(0, 'mm2', 4, 'mm2', 1.5, 'mm2')
    expected = ('MM2', 'MM2', 'MM2')
    result = (test_class.activeConductors.unit, test_class.neutralConductors.unit, test_class.earthConductors.unit)
    assert result == expected


def test_cls_conductor_cable_run_size_unit_setter():
    test_class = cable.ConductorCableRun()
    test_class.active_size = 4
    test_class.neutral_size = 4
    test_class.earth_size = 1.5
    expected = (4.0, 4.0, 1.5)
    result = (test_class.active_size, test_class.neutral_size, test_class.earth_size)
    assert result == expected


def test_cls_contracts():
    test_class = cable.Contracts("gc-12", "gc-14", "ic-89")
    expected = ("GC-12", "GC-14", "IC-89")
    result = (test_class.supply, test_class.install, test_class.connect)
    assert result == expected


def test_cls_contracts_to_dict():
    test_class = cable.Contracts("gc-12", "gc-14", "ic-89")
    expected = {"supply": "GC-12", "install": "GC-14", "connect": "IC-89"}
    result = test_class.to_dict()
    assert result == expected


def test_cls_contracts_from_dict():
    test_class = cable.Contracts()
    expected = ("GC-12", "GC-14", "IC-89")
    details = {"supply": "GC-12", "install": "GC-14", "connect": "IC-89"}
    test_class.from_dict(details)
    result = (test_class.supply, test_class.install, test_class.connect)
    assert result == expected


def test_cls_core_details():
    test_class = cable.CoreDetails()
    test_class.size = 2.5
    test_class.unit = "mm2"
    test_class.number = 4
    test_class.name = "core"
    expected = (2.5, "MM2", 4, "CORE")
    result = (test_class.size, test_class.unit, test_class.number, test_class.name)
    assert result == expected


def test_cls_core_details_to_dict():
    test_class = cable.CoreDetails(35, "mm2", 4, "core")
    expected = {"size": 35, "key": "MM2", "number": 4, "name": "CORE"}
    result = test_class.to_dict()
    assert result == expected


def test_cls_core_details_from_dict():
    test_class = cable.CoreDetails()
    expected = (35, "MM2", 4, "CORE")
    details = {"size": 35, "key": "mm2", "number": 4, "name": "core"}
    test_class.from_dict(details)
    result = (test_class.size, test_class.unit, test_class.number, test_class.name)
    assert result == expected


def test_cls_frequency():
    test_class = cable.Frequency(50, 'hz', 'dc')
    expected = (50, "HZ", "DC")
    result = (test_class.frequency, test_class.unit, test_class.waveform)
    assert result == expected


def test_cls_frequency_dict():
    test_class = cable.Frequency(50, 'hz', 'dc')
    expected = {"frequency": 50, "key": "HZ", "waveform": "DC"}
    result = test_class.to_dict()
    assert result == expected


def test_cls_impedance_mvam_setter():
    test_class = cable.Impedance()
    test_class.mvam = 0.1
    expected = 0.1
    result = test_class.mvam
    assert result == expected


def test_cls_impedance_mvam_getter():
    test_class = cable.Impedance(mvam=0.2)
    expected = 0.2
    result = test_class.mvam
    assert result == expected


def test_cls_impedance_ohm_setter():
    test_class = cable.Impedance()
    test_class.r = 0.1
    test_class.r_unit = "ohms"
    test_class.x = 0.2
    test_class.x_unit = "oHms"
    test_class.z = 0.3
    test_class.z_unit = "OHMS"
    expected = (0.1, "OHMS", 0.2, "OHMS", 0.3, "OHMS")
    result = (test_class.r, test_class.r_unit, test_class.x, test_class.x_unit, test_class.z, test_class.z_unit)
    assert result == expected


def test_cls_impedance_ohm_getter():
    test_class = cable.Impedance(r=0.2, r_unit='ohms', x=0.4, x_unit='ohms', z=0.6, z_unit='ohms')
    expected = (0.2, "OHMS", 0.4, "OHMS", 0.6, "OHMS")
    result = (test_class.r, test_class.r_unit, test_class.x, test_class.x_unit, test_class.z, test_class.z_unit)
    assert result == expected


def test_cls_impedance_resistance():
    test_class = cable.Impedance(r=0.8, r_unit='ohms')
    expected = (0.8, "OHMS")
    result = test_class.resistance()
    assert result == expected


def test_cls_impedance_reactance():
    test_class = cable.Impedance(x=0.08, x_unit='ohms')
    expected = (0.08, "OHMS")
    result = test_class.reactance()
    assert result == expected


def test_cls_impedance_impedance():
    test_class = cable.Impedance(z=0.2, z_unit='ohms')
    expected = (0.2, "OHMS")
    result = test_class.impedance()
    assert result == expected


def test_cls_impedance_to_dict():
    test_class = cable.Impedance(mvam=0.2, r=0.8, r_unit='ohms', x=0.08, x_unit='ohms', z=0.2, z_unit='ohms')
    expected = {"mvam": 0.2, "r": 0.8, "r_unit": "OHMS",  "x": 0.08, "x_unit": "OHMS",  "z": 0.2, "z_unit": "OHMS"}
    result = test_class.to_dict()
    assert result == expected


def test_cls_impedance_from_dict():
    test_class = cable.Impedance()
    expected = (0.2, 0.8, "OHMS", 0.08, "OHMS", 0.2, "OHMS")
    details = {"mvam": 0.2, "r": 0.8, "r_unit": "ohms",  "x": 0.08, "x_unit": "ohms",  "z": 0.2, "z_unit": "ohms"}
    test_class.from_dict(details)
    result = (test_class.mvam, test_class.r, test_class.r_unit, test_class.x, test_class.x_unit, test_class.z,
              test_class.z_unit)
    assert result == expected


def test_cls_installation_method():
    test_class = cable.InstallationMethod(installation="touching", arrangement='trefoil')
    expected = ("TOUCHING", "TREFOIL")
    result = (test_class.physical_installation, test_class.cable_arrangement)
    assert result == expected


def test_cls_installation_to_dict():
    test_class = cable.InstallationMethod("touching", "trefoil")
    expected = {"installation": "TOUCHING", "arrangement": "TREFOIL"}
    result = test_class.to_dict()
    assert result == expected


def test_cls_installation_from_dict():
    test_class = cable.InstallationMethod()
    expected = ("TOUCHING", "TREFOIL")
    test_class.from_dict({"installation": "TOUCHING", "arrangement": "TREFOIL"})
    result = (test_class.physical_installation, test_class.cable_arrangement)
    assert result == expected


def test_cls_insulation():
    test_class = cable.Insulation()
    test_class.material = "xlpe"
    test_class.code = "x-90"
    test_class.op_temp = 73
    test_class.max_temp = 90
    expected = ("XLPE", "X-90", 73, 90)
    result = (test_class.material, test_class.code, test_class.op_temp, test_class.max_temp)
    assert result == expected


def test_cls_load_current():
    test_class = cable.Circuit(load_current=5.5)
    expected = 6.0
    test_class.load_current = 6.0
    result = test_class.load_current
    assert result == expected


def test_cls_manufacturer():
    test_class = cable.Manufacturer()
    test_class.name = "olex"
    test_class.part_number = "p2134"
    expected = ("OLEX", "P2134")
    result = (test_class.name, test_class.part_number)
    assert result == expected


def test_cls_manufacturer_to_dict():
    test_class = cable.Manufacturer("olex", "p1234")
    expected = {"name": "OLEX", "part_number": "P1234"}
    result = test_class.to_dict()
    assert result == expected


def test_cls_manufacturer_from_dict():
    test_class = cable.Manufacturer()
    expected = ("OLEX", "P1234")
    test_class.from_dict({"name": "olex", "part_number": "p1234"})
    result = (test_class.name, test_class.part_number)
    assert result == expected


@pytest.mark.parametrize("k_factor, amp_time, expected",
                         [(141, [(10000, 0.1)], (141, [(10000, 0.1)])),
                          (141, (10000, 0.1), (141, [(10000, 0.1)])),
                          (165, [], (165, [])),
                          (210, None, (210, []))
                          ])
def test_cls_i2t(k_factor, amp_time, expected):
    test_class = cable.I2T()
    test_class.k_factor = k_factor
    test_class.amp_time = amp_time
    result = (test_class.k_factor, test_class.amp_time)
    assert result == expected


def test_cls_i2t_to_dict():
    test_class = cable.I2T(141, [(10000, 0.1)])
    expected = {"k_factor": 141, "amp_time": [(10000, 0.1)]}
    result = test_class.to_dict()
    assert result == expected


def test_cls_i2t_from_dict():
    test_class = cable.I2T()
    expected = 141, [(10000, 0.1)]
    test_class.from_dict({"k_factor": 141, "amp_time": [(10000, 0.1)]})
    result = (test_class.k_factor, test_class.amp_time)
    assert result == expected


def test_cls_insulation_to_dict():
    test_class = cable.Insulation("pvc", "v-90", 90, 250)
    expected = {"material": "PVC", "code": "V-90", "op_temp": 90, "max_temp": 250}
    result = test_class.to_dict()
    assert result == expected


def test_cls_insulation_from_dict():
    test_class = cable.Insulation()
    expected = ("PVC", "V-90", 90, 250)
    details = {"material": "pvc", "code": "v-90", "op_temp": 90, "max_temp": 250}
    test_class.from_dict(details)
    result = (test_class.material, test_class.code, test_class.op_temp, test_class.max_temp)
    assert result == expected


def test_cls_revision_detail_number_setter():
    test_class = cable.RevisionDetail()
    test_class.number = 'a'
    expected = 'A'
    result = test_class.number
    assert result == expected


def test_cls_revision_detail_number_getter():
    test_class = cable.RevisionDetail()
    test_class.number = 'a'
    expected = 'A'
    result = test_class.number
    assert result == expected


def test_cls_revision_detail_date_setter():
    test_class = cable.RevisionDetail()
    test_class.date = dt.datetime(1, 1, 1)
    expected = dt.datetime(1, 1, 1)
    result = test_class.date
    assert result == expected


def test_cls_revision_detail_date_getter():
    test_class = cable.RevisionDetail()
    expected = None
    result = test_class.date
    assert result == expected


def test_cls_revision():
    test_class = cable.RevisionDetail("A", dt.datetime(20, 3, 20))
    expected = ("A", dt.datetime(20, 3, 20))
    result = (test_class.number, test_class.date)
    assert result == expected


def test_cls_revision_to_dict():
    test_class = cable.RevisionDetail("A", dt.datetime(20, 3, 20))
    expected = {"number": "A", "date": dt.datetime(20, 3, 20)}
    result = test_class.to_dict()
    assert result == expected


def test_cls_revision_from_dict():
    test_class = cable.RevisionDetail()
    expected = ("A", dt.datetime(20, 3, 20))
    details = {"number": "a", "date": dt.datetime(20, 3, 20)}
    test_class.from_dict(details)
    result = (test_class.number, test_class.date)
    assert result == expected


def test_cls_screen():
    test_class = cable.Screen()
    test_class.name = "os"
    test_class.fault_withstand = 10000000
    expected = ("OS", 10000000)
    result = (test_class.name, test_class.fault_withstand)
    assert result == expected


def test_cls_screen_to_dict():
    test_class = cable.Screen("os", 27000000)
    expected = {"name": "OS", "fault_withstand": 27000000}
    result = test_class.to_dict()
    assert result == expected


def test_cls_screen_from_dict():
    test_class = cable.Screen()
    expected = ("OS", 27000000)
    test_class.from_dict({"name": "os", "fault_withstand": 27000000})
    result = (test_class.name, test_class.fault_withstand)
    assert result == expected


def test_cls_vector():
    test_class = cable.Vector()
    test_class.magnitude = 415
    test_class.unit = 'VAC'
    expected = (415, 'VAC')
    result = (test_class.magnitude, test_class.unit)
    assert result == expected


def test_cls_vector_magnitude_getter():
    test_class = cable.Vector(33, 'kV')
    expected = (33, 'KV')
    result = (test_class.magnitude, test_class.unit)
    assert result == expected


def test_cls_vector_to_dict():
    test_class = cable.Vector(33, 'kV')
    expected = {"magnitude": 33, "key": "KV"}
    result = test_class.to_dict()
    assert result == expected


def test_cls_vector_from_dict():
    test_class = cable.Vector()
    expected = (33, "KV")
    details = {"magnitude": 33, "key": "kv"}
    test_class.from_dict(details)
    result = (test_class.magnitude, test_class.unit)
    assert result == expected


def test_cls_voltage():
    test_class = cable.Voltage()
    test_class.phases = 3
    test_class.v = 433
    test_class.unit = "vac"
    test_class.neutral_required = True
    expected = (3, 433, "VAC", True)
    result = (test_class.phases, test_class.v, test_class.unit, test_class.neutral_required)
    assert result == expected


def test_cls_voltage_to_dict():
    test_class = cable.Voltage(433, "vac", 3, True)
    expected = {"phases": 3, "v": 433, "key": "VAC", "neutral_required": True}
    result = test_class.to_dict()
    assert result == expected


def test_cls_voltage_from_dict():
    test_class = cable.Voltage()
    expected = (433, "VAC", 3, True)
    details = {"phases": 3, "v": 433, "key": "vac", "neutral_required": True}
    test_class.from_dict(details)
    result = (test_class.v, test_class.unit, test_class.phases, test_class.neutral_required)
    assert result == expected
