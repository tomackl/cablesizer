import pytest
import CableSizer.cable as cable
import datetime as dt


def test_cls_cable_run():
    test_class = cable.CableRun(required_ccc=10, derating_run=0.8)
    expected = (10.0, 0.8)
    result = (test_class.required_ccc, test_class.derate_run)
    assert result == expected


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


def test_cls_conductor_detail_dict():
    test_class = cable.ConductorDetail(95, "mm2")
    expected = {"size": 95, "unit": "MM2"}
    result = test_class.to_dict()
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


def test_cls_conductor_cable_run_dict():
    test_class = cable.ConductorCableRun(active_size=4, active_unit="mm2", neutral_size=4, neutral_unit="mm2",
                                         earth_size=1.5, earth_unit="mm2", instrumentation_size=1.5,
                                         instrumentation_unit="mm2", control_size=1.5, control_unit="mm2",
                                         data_size=0.75, data_unit="mm2", communication_size=1.5,
                                         communication_unit="mm2")
    expected = {"activeConductors": {"size": 4, "unit": "MM2"},
                "neutralConductors": {"size": 4, "unit": "MM2"},
                "earthConductors": {"size": 1.5, "unit": "MM2"},
                "instrumentationConductors": {"size": 1.5, "unit": "MM2"},
                "communicationConductors": {"size": 1.5, "unit": "MM2"},
                "dataConductors": {"size": 0.75, "unit": "MM2"},
                "controlConductors": {"size": 1.5, "unit": "MM2"},
                }
    result = test_class.to_dict()
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


def test_cls_contracts_getter():
    test_class = cable.Contracts('Contract_supply', 'contract_install', 'contract_connect')
    expected = ('CONTRACT_SUPPLY', 'CONTRACT_INSTALL', 'CONTRACT_CONNECT')
    result = (test_class.supply, test_class.install, test_class.connect)
    assert result == expected


def test_cls_contracts_setter():
    test_class = cable.Contracts()
    test_class.install = 'contract_install'
    test_class.supply = 'contract_supply'
    test_class.connect = 'contract_connect'
    expected = ('CONTRACT_SUPPLY', 'CONTRACT_INSTALL', 'CONTRACT_CONNECT')
    result = (test_class.supply, test_class.install, test_class.connect)
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
    expected = {"phases": 3, "v": 433, "unit": "VAC", "neutral_required": True}
    result = test_class.to_dict()
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


def test_cls_vector_dict():
    test_class = cable.Vector(33, 'kV')
    expected = {"magnitude": 33, "unit": "KV"}
    result = test_class.to_dict()
    assert result == expected


def test_cls_circuit_type():
    test_class = cable.Circuit(circuit_type='power')
    expected = "POWER"
    result = test_class.circuit_type
    assert result == expected


def test_cls_circuit_voltage():
    test_class = cable.Circuit(voltage=22, voltage_unit='kv', phases=4, neutral_required=True)
    expected = (22, 'KV', 4, True)
    result = (test_class.v, test_class.v_unit, test_class.phases, test_class.neutral_required)
    assert result == expected


def test_cls_circuit_dict():
    test_class = cable.Circuit(circuit_type="power", voltage=22, voltage_unit='kv', frequency=50, frequency_unit="hz",
                               waveform="ac", phases=4, neutral_required=True, physical_method="buried_direct",
                               cable_arrangement="trefoil", load_current=150)
    expected = {"circuit_type": "POWER",
                "voltage": {"v": 22, "unit": "KV", "phases": 4, "neutral_required": True},
                "frequency": {"frequency": 50, "unit": "HZ", "waveform": "AC"},
                "installation_method": {"installation": "BURIED_DIRECT", "arrangement": "TREFOIL"},
                "load_current": 150
                }
    result = test_class.to_dict()
    assert result == expected


def test_cls_frequency():
    test_class = cable.Frequency(50, 'hz', 'dc')
    expected = (50, "HZ", "DC")
    result = (test_class.frequency, test_class.unit, test_class.waveform)
    assert result == expected


def test_cls_frequency_dict():
    test_class = cable.Frequency(50, 'hz', 'dc')
    expected = {"frequency": 50, "unit": "HZ", "waveform": "DC"}
    result = test_class.to_dict()
    assert result == expected


def test_cls_installation_method():
    test_class = cable.InstallationMethod(installation="touching", arrangement='trefoil')
    expected = ("TOUCHING", "TREFOIL")
    result = (test_class.physical_installation, test_class.cable_arrangement)
    assert result == expected


def test_cls_circuit_installation_method():
    test_class = cable.Circuit(physical_method="touching", cable_arrangement='trefoil')
    expected = ("TOUCHING", "TREFOIL")
    result = (test_class.physical_installation, test_class.cable_arrangement)
    assert result == expected


def test_cls_load_current():
    test_class = cable.Circuit(load_current=5.5)
    expected = 6.0
    test_class.load_current = 6.0
    result = test_class.load_current
    assert result == expected


def test_cls_cablespec():
    test_class = cable.CableSpec(run_type='multi', max_parallel=2, allow_parallel_multicore=True, shape="circular",
                                 conductor_material="CU", min_size=4.0, core_arrangement='multi', sheath='none',
                                 insulation_material='xlpe', insulation_code='x-90', max_operating_temp=90,
                                 armour='dwa', screen_cable='nil', screen_core='is', volt_rating='0.6/1kv',
                                 flexible=False)
    expected = ("MULTI", 2, True, "CIRCULAR", "CU", 4.0, "MULTI", "NONE", "XLPE", "X-90", 90, "DWA", "NIL", "IS",
                "0.6/1KV", False)
    result = (test_class.type, test_class.max_parallel, test_class.allow_parallel_multicore, test_class.shape,
              test_class.conductor_material, test_class.min_size, test_class.core_arrangement, test_class.sheath,
              test_class.insulation_material, test_class.insulation_code, test_class.maximum_operating_temp,
              test_class.armour, test_class.screen_cable, test_class.screen_core, test_class.volt_rating,
              test_class.flexible)
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


def test_cls_core_details():
    test_class = cable.CoreDetails()
    test_class.size = 2.5
    test_class.unit = "mm2"
    test_class.number = 4
    test_class.name = "core"
    expected = (2.5, "MM2", 4, "CORE")
    result = (test_class.size, test_class.unit, test_class.number, test_class.name)
    assert result == expected


def test_cls_core_details_dict():
    test_class = cable.CoreDetails(35, "mm2", 4, "core")
    expected = {"size": 35, "unit": "MM2", "number": 4, "name": "CORE"}
    result = test_class.to_dict()
    assert result == expected


def test_cls_cable_installation_method():
    test_class = cable.CableInstallationMethod()
    test_class.name = "buried_direct"
    test_class.ccc = 140
    test_class.install_temp = 45
    test_class.cable_arrangement = 'trefoil'
    expected = ("BURIED_DIRECT", 140, 45, "TREFOIL")
    result = (test_class.name, test_class.ccc, test_class.install_temp, test_class.cable_arrangement)
    assert result == expected


def test_cls_cable_installation_method_dict():
    test_class = cable.CableInstallationMethod("buried_direct", 140, 45, "trefoil")
    expected = {"name": "BURIED_DIRECT", "ccc": 140, "install_temp": 45, "arrangement": "TREFOIL"}
    result = test_class.to_dict()
    assert result == expected


def test_cls_cable_screen():
    test_class = cable.Screen()
    test_class.name = "dwt"
    test_class.fault_withstand = int(10e6)
    expected = ("DWT", 10000000)
    result = (test_class.name, test_class.fault_withstand)
    assert result == expected


def test_cls_manufacturer():
    test_class = cable.Manufacturer()
    test_class.name = "olex"
    test_class.part_number = "p2134"
    expected = ("OLEX", "P2134")
    result = (test_class.name, test_class.part_number)
    assert result == expected


def test_cls_manufacturer_dict():
    test_class = cable.Manufacturer("olex", "p1234")
    expected = {"name": "OLEX", "part_number": "P1234"}
    result = test_class.to_dict()
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


def test_cls_i2t_dict():
    test_class = cable.I2T(141, [(10000, 0.1)])
    expected = {"k_factor": 141, "amp_time": [(10000, 0.1)]}
    result = test_class.to_dict()
    assert result == expected


def test_cls_core_details():
    test_class = cable.CoreDetails()
    test_class.unit = "mm2"
    test_class.name = "core"
    test_class.number = 3
    test_class.size = 35
    expected = (35, "MM2", 3, "CORE")
    result = (test_class.size, test_class.unit, test_class.number, test_class.name)
    assert result == expected


def test_cls_core_details_dict():
    test_class = cable.CoreDetails(35, "mm2", 3, "core")
    expected = {"size": 35, "unit": "MM2", "number": 3, "name": "CORE"}
    result = test_class.to_dict()
    assert result == expected


def test_cls_screen():
    test_class = cable.Screen()
    test_class.name = "os"
    test_class.fault_withstand = 10000000
    expected = ("OS", 10000000)
    result = (test_class.name, test_class.fault_withstand)
    assert result == expected


def test_cls_screen_dict():
    test_class = cable.Screen("os", 27000000)
    expected = {"name": "OS", "fault_withstand": 27000000}
    result = test_class.to_dict()
    assert result == expected


# def test_cls_conductor_cable_run():
#     test_class = cable.ConductorCableRun()
#     test_class.