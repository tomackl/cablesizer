import pytest
import CableSizer.cable as cable
import datetime as dt


def test_cable_run_cls():
    test_class = cable.CableRun(required_ccc=10, derating_run=0.8)
    expected = (10.0, 0.8)
    result = (test_class.required_ccc, test_class.derate_run)
    assert result == expected


def test_conductor_detail_size_setter():
    test_class = cable.ConductorDetail()
    test_class.size = 1.5
    expected = 1.5
    result = test_class.size
    assert result == expected


def test_conductor_detail_size_getter():
    test_class = cable.ConductorDetail(size=1.5)
    expected = 1.5
    result = test_class.size
    assert result == expected


def test_conductor_detail_size_unit_setter():
    test_class = cable.ConductorDetail()
    test_class.size_unit = 'mm2'
    expected = 'MM2'
    result = test_class.size_unit
    assert result == expected


def test_conductor_detail_size_unit_getter():
    test_class = cable.ConductorDetail(size_unit='mm2')
    expected = 'MM2'
    result = test_class.size_unit
    assert result == expected


def test_conductor_cable_run_size_getter():
    test_class = cable.ConductorCableRun(4, '', 4, '', 1.5, '')
    expected = (4.0, 4.0, 1.5)
    result = (test_class.active_size, test_class.neutral_size, test_class.earth_size)
    assert result == expected


def test_conductor_cable_run_size_setter():
    test_class = cable.ConductorCableRun()
    test_class.active_size = 4
    test_class.neutral_size = 4
    test_class.earth_size = 1.5
    expected = (4.0, 4.0, 1.5)
    result = (test_class.active_size, test_class.neutral_size, test_class.earth_size)
    assert result == expected


def test_conductor_cable_run_size_unit_getter():
    test_class = cable.ConductorCableRun(0, 'mm2', 4, 'mm2', 1.5, 'mm2')
    expected = ('MM2', 'MM2', 'MM2')
    result = (test_class.active_size_unit, test_class.neutral_size_unit, test_class.earth_size_unit)
    assert result == expected


def test_conductor_cable_run_size_unit_setter():
    test_class = cable.ConductorCableRun()
    test_class.active_size = 4
    test_class.neutral_size = 4
    test_class.earth_size = 1.5
    expected = (4.0, 4.0, 1.5)
    result = (test_class.active_size, test_class.neutral_size, test_class.earth_size)
    assert result == expected


def test_revision_detail_number_setter():
    test_cls_revision_detail = cable.RevisionDetail()
    test_cls_revision_detail.number = 'a'
    expected = 'A'
    result = test_cls_revision_detail.number
    assert result == expected


def test_revision_detail_number_getter():
    test_cls_revision_detail = cable.RevisionDetail()
    test_cls_revision_detail.number = 'a'
    expected = 'A'
    result = test_cls_revision_detail.number
    assert result == expected


def test_revision_detail_date_setter():
    test_cls_revision_detail = cable.RevisionDetail()
    test_cls_revision_detail.date = dt.datetime(1, 1, 1)
    expected = dt.datetime(1, 1, 1)
    result = test_cls_revision_detail.date
    assert result == expected


def test_revision_detail_date_getter():
    test_cls_revision_detail = cable.RevisionDetail()
    expected = None
    result = test_cls_revision_detail.date
    assert result == expected


def test_impedance_mvam_setter():
    test_class = cable.Impedance()
    test_class.mvam = 0.1
    expected = 0.1
    result = test_class.mvam
    assert result == expected


def test_impedance_mvam_getter():
    test_class = cable.Impedance(mvam=0.2)
    expected = 0.2
    result = test_class.mvam
    assert result == expected


def test_impedance_ohm_setter():
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


def test_impedance_ohm_getter():
    test_class = cable.Impedance(r=0.2, r_unit='ohms', x=0.4, x_unit='ohms', z=0.6, z_unit='ohms')
    expected = (0.2, "OHMS", 0.4, "OHMS", 0.6, "OHMS")
    result = (test_class.r, test_class.r_unit, test_class.x, test_class.x_unit, test_class.z, test_class.z_unit)
    assert result == expected


def test_impedance_resistance():
    test_class = cable.Impedance(r=0.8, r_unit='ohms')
    expected = (0.8, "OHMS")
    result = test_class.resistance()
    assert result == expected


def test_impedance_reactance():
    test_class = cable.Impedance(x=0.08, x_unit='ohms')
    expected = (0.08, "OHMS")
    result = test_class.reactance()
    assert result == expected


def test_impedance_impedance():
    test_class = cable.Impedance(z=0.2, z_unit='ohms')
    expected = (0.2, "OHMS")
    result = test_class.impedance()
    assert result == expected


def test_contracts_getter():
    test_class = cable.Contracts('Contract_supply', 'contract_install', 'contract_connect')
    expected = ('CONTRACT_SUPPLY', 'CONTRACT_INSTALL', 'CONTRACT_CONNECT')
    result = (test_class.supply, test_class.install, test_class.connect)
    assert result == expected


def test_contracts_setter():
    test_class = cable.Contracts()
    test_class.install = 'contract_install'
    test_class.supply = 'contract_supply'
    test_class.connect = 'contract_connect'
    expected = ('CONTRACT_SUPPLY', 'CONTRACT_INSTALL', 'CONTRACT_CONNECT')
    result = (test_class.supply, test_class.install, test_class.connect)
    assert result == expected


def test_vector_cls():
    test_cls_vector = cable.Vector()
    test_cls_vector.magnitude = 415
    test_cls_vector.unit = 'VAC'
    expected = (415, 'VAC')
    result = (test_cls_vector.magnitude, test_cls_vector.unit)
    assert result == expected


def test_vector_magnitude_getter():
    test_cls_vector = cable.Vector(33, 'kV')
    expected = (33, 'kV')
    result = (test_cls_vector.magnitude, test_cls_vector.unit)
    assert result == expected


def test_circuit_type():
    test_cls_circuit = cable.Circuit(circuit_type='power')
    expected = "POWER"
    result = test_cls_circuit.circuit_type
    assert result == expected


def test_circuit_voltage():
    test_cls_circuit = cable.Circuit(voltage=22, voltage_unit='kv', phases=4, neutral_required=True)
    expected = (22, 'KV', 4, True)
    result = (test_cls_circuit.v, test_cls_circuit.v_unit, test_cls_circuit.phases, test_cls_circuit.neutral_required)
    assert result == expected


def test_frequency_cls():
    test_cls_frequency = cable.Frequency(50, 'hz', 'dc')
    expected = (50, "HZ", "DC")
    result = (test_cls_frequency.freq, test_cls_frequency.unit, test_cls_frequency.waveform)
    assert result == expected


def test_installation_method():
    test_class = cable.Circuit(physical_method="touching", cable_arrangement='trefoil')
    expected = ("TOUCHING", "TREFOIL")
    result = (test_class.physical_installation, test_class.cable_arrangement)
    assert result == expected


def test_load_current():
    test_class = cable.Circuit(load_current=5.5)
    expected = 6.0
    test_class.load_current = 6.0
    result = test_class.load_current
    assert result == expected


def test_cls_cablespec():
    test_class = cable.CableSpec(run_type='multi', max_parallel=2, allow_parallel_multicore=True, shape="circular",
                                 conductor_material="CU", min_size=4.0, core_arrangement='multi', sheath='none',
                                 insulation_material='xlpe', insulation_code='x-90', max_operating_temp=90, armour='dwa',
                                 screen_cable='nil', screen_core='is', volt_rating='0.6/1kv', flexible=False)
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
    test_class.csa = 2.5
    test_class.csa_unit = "mm2"
    test_class.number = 4
    test_class.name = "core"
    expected = (2.5, "MM2", 4, "CORE")
    result = (test_class.csa, test_class.csa_unit, test_class.number, test_class.name)
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


def test_cls_i2t():
    test_class = cable.I2T()
    expected = (141, [(10000, 0.1)])
    test_class.k_factor = 141
    test_class.amp_time = (10000, 0.1)
    result = (test_class.k_factor, test_class.amp_time)
    assert result == expected
