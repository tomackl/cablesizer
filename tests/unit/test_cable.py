import pytest
import CableSizer.cable as cable
import datetime as dt

test_cls_cable_run = cable.CableRun
test_cls_revision_detail = cable.RevisionDetail

test_cls_impedance = cable.Impedance
test_cls_contracts = cable.Contracts
test_cls_circuit = cable.Circuit


def test_conductor_detail_size_setter():
    test_cls_conductor_detail = cable.ConductorDetail()
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
    test_cls_impedance.x = 0.2
    test_cls_impedance.z = 0.3
    expected = (0.1, 0.2, 0.3)
    result = (test_cls_impedance.r, test_cls_impedance.x, test_cls_impedance.z)
    assert result == expected


def test_impedance_ohm_getter():
    test_cls_impedance = cable.Impedance(r_ohms=0.2, x_ohms=0.4, z_ohms=0.6)
    expected = (0.2, 0.4, 0.6)
    result = (test_cls_impedance.r, test_cls_impedance.x, test_cls_impedance.z)
    assert result == expected

