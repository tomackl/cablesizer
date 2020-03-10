import pytest
import CableSizer.cable as cable
import datetime as dt

test_cls_cable_run = cable.CableRun


def test_cable_run_cls():
    test_cls_cable_run = cable.CableRun(required_ccc=10, derating_run=0.8)
    expected = (10.0, 0.8)
    result = (test_cls_cable_run.required_ccc, test_cls_cable_run.derate_run)
    assert result == expected


def test_conductor_detail_size_setter():
    test_cls_conductor_detail = cable.ConductorDetail
    test_cls_conductor_detail.size = 1.5
    expected = 1.5
    result = test_cls_conductor_detail.size
    assert result == expected


def test_conductor_detail_size_getter():
    test_cls_conductor_detail = cable.ConductorDetail(size=1.5)
    expected = 1.5
    result = test_cls_conductor_detail.size
    assert result == expected


def test_conductor_detail_size_unit_setter():
    test_cls_conductor_detail = cable.ConductorDetail()
    test_cls_conductor_detail.size_unit = 'mm2'
    expected = 'MM2'
    result = test_cls_conductor_detail.size_unit
    assert result == expected


def test_conductor_detail_size_unit_getter():
    test_cls_conductor_detail = cable.ConductorDetail(size_unit='mm2')
    expected = 'MM2'
    result = test_cls_conductor_detail.size_unit
    assert result == expected


def test_conductor_cable_run_size_getter():
    test_cls_conductor_cable_run = cable.ConductorCableRun(4, '', 4, '', 1.5, '')
    expected = (4.0, 4.0, 1.5)
    result = (test_cls_conductor_cable_run.active_size,
              test_cls_conductor_cable_run.neutral_size,
              test_cls_conductor_cable_run.earth_size)
    assert result == expected


def test_conductor_cable_run_size_setter():
    test_cls_conductor_cable_run = cable.ConductorCableRun()
    test_cls_conductor_cable_run.active_size = 4
    test_cls_conductor_cable_run.neutral_size = 4
    test_cls_conductor_cable_run.earth_size = 1.5
    expected = (4.0, 4.0, 1.5)
    result = (test_cls_conductor_cable_run.active_size,
              test_cls_conductor_cable_run.neutral_size,
              test_cls_conductor_cable_run.earth_size)
    assert result == expected


def test_conductor_cable_run_size_unit_getter():
    test_cls_conductor_cable_run = cable.ConductorCableRun(0, 'mm2', 4, 'mm2', 1.5, 'mm2')
    expected = ('MM2', 'MM2', 'MM2')
    result = (test_cls_conductor_cable_run.active_size_unit,
              test_cls_conductor_cable_run.neutral_size_unit,
              test_cls_conductor_cable_run.earth_size_unit)
    assert result == expected


def test_conductor_cable_run_size_unit_setter():
    test_cls_conductor_cable_run = cable.ConductorCableRun()
    test_cls_conductor_cable_run.active_size = 4
    test_cls_conductor_cable_run.neutral_size = 4
    test_cls_conductor_cable_run.earth_size = 1.5
    expected = (4.0, 4.0, 1.5)
    result = (test_cls_conductor_cable_run.active_size,
              test_cls_conductor_cable_run.neutral_size,
              test_cls_conductor_cable_run.earth_size)
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
    test_cls_impedance = cable.Impedance()
    test_cls_impedance.mvam = 0.1
    expected = 0.1
    result = test_cls_impedance.mvam
    assert result == expected


def test_impedance_mvam_getter():
    test_cls_impedance = cable.Impedance(mvam=0.2)
    expected = 0.2
    result = test_cls_impedance.mvam
    assert result == expected


def test_impedance_ohm_setter():
    test_cls_impedance = cable.Impedance()
    test_cls_impedance.r = 0.1
    test_cls_impedance.r_unit = "ohms"
    test_cls_impedance.x = 0.2
    test_cls_impedance.x_unit = "oHms"
    test_cls_impedance.z = 0.3
    test_cls_impedance.z_unit = "OHMS"
    expected = (0.1, "OHMS", 0.2, "OHMS", 0.3, "OHMS")
    result = (test_cls_impedance.r, test_cls_impedance.r_unit,
              test_cls_impedance.x, test_cls_impedance.x_unit,
              test_cls_impedance.z, test_cls_impedance.z_unit)
    assert result == expected


def test_impedance_ohm_getter():
    test_cls_impedance = cable.Impedance(r=0.2, r_unit='ohms', x=0.4, x_unit='ohms', z=0.6, z_unit='ohms')
    expected = (0.2, "OHMS", 0.4, "OHMS", 0.6, "OHMS")
    result = (test_cls_impedance.r, test_cls_impedance.r_unit,
              test_cls_impedance.x, test_cls_impedance.x_unit,
              test_cls_impedance.z, test_cls_impedance.z_unit)
    assert result == expected


def test_impedance_resistance():
    test_cls_impedance = cable.Impedance(r=0.8, r_unit='ohms')
    expected = (0.8, "OHMS")
    result = test_cls_impedance.resistance()
    assert result == expected


def test_impedance_reactance():
    test_cls_impedance = cable.Impedance(x=0.08, x_unit='ohms')
    expected = (0.08, "OHMS")
    result = test_cls_impedance.reactance()
    assert result == expected


def test_impedance_impedance():
    test_cls_impedance = cable.Impedance(z=0.2, z_unit='ohms')
    expected = (0.2, "OHMS")
    result = test_cls_impedance.impedance()
    assert result == expected


def test_contracts_getter():
    test_cls_contracts = cable.Contracts('Contract_supply', 'contract_install', 'contract_connect')
    expected = ('CONTRACT_SUPPLY', 'CONTRACT_INSTALL', 'CONTRACT_CONNECT')
    result = (test_cls_contracts.supply,
              test_cls_contracts.install,
              test_cls_contracts.connect)
    assert result == expected


def test_contracts_setter():
    test_cls_contracts = cable.Contracts()
    test_cls_contracts.install = 'contract_install'
    test_cls_contracts.supply = 'contract_supply'
    test_cls_contracts.connect = 'contract_connect'
    expected = ('CONTRACT_SUPPLY', 'CONTRACT_INSTALL', 'CONTRACT_CONNECT')
    result = (test_cls_contracts.supply,
              test_cls_contracts.install,
              test_cls_contracts.connect)
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
    test_cls_circuit = cable.Circuit(physical_method="touching", cable_arrangement='trefoil')
    expected = ("TOUCHING", "TREFOIL")
    result = (test_cls_circuit.physical_installation, test_cls_circuit.cable_arrangement)
    assert result == expected


def test_load_current():
    test_cls_circuit = cable.Circuit(load_current=5.5)
    expected = 6.0
    test_cls_circuit.load_current = 6.0
    result = test_cls_circuit.load_current
    assert result == expected


def test_cls_cablespec():
    test_cls_cable_run = cable.CableSpec(run_type='multi', max_parallel=2, allow_parallel_multicore=True,
                                         shape="circular", conductor_material="CU", min_size=4.0,
                                         core_arrangement='multi', sheath='none', insulation_material='xlpe',
                                         insulation_code='x-90', maximum_operating_temp=90, armour='dwa',
                                         screen_cable='nil', screen_core='is', volt_rating='0.6/1kv', flexible=False)
    expected = ("MULTI", 2, True, "CIRCULAR", "CU", 4.0, "MULTI", "NONE", "XLPE", "X-90", 90, "DWA", "NIL", "IS",
                "0.6/1KV", False)
    result = (test_cls_cable_run.type, test_cls_cable_run.max_parallel, test_cls_cable_run.allow_parallel_multicore,
              test_cls_cable_run.shape, test_cls_cable_run.conductor_material, test_cls_cable_run.min_size,
              test_cls_cable_run.core_arrangement, test_cls_cable_run.sheath, test_cls_cable_run.insulation_material,
              test_cls_cable_run.insulation_code, test_cls_cable_run.maximum_operating_temp, test_cls_cable_run.armour,
              test_cls_cable_run.screen_cable, test_cls_cable_run.screen_core, test_cls_cable_run.volt_rating,
              test_cls_cable_run.flexible)
    assert result == expected
