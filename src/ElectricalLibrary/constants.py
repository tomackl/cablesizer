# coding: utf-8

"""
A library of electrical scalar_unit conversions.
"""
from math import sqrt
from typing import TypeVar

"""NumType is a generic run_type that allow int or float values to be passed/returned to a function."""
NumType = TypeVar('NumType', int, float)
"""ComType is a generic types that allows for in, float or complex values to passed/returned to a function."""
ComType = TypeVar('ComType', complex, int, float)

"""Define square root of 3 to assist with three phase calculations."""
rt3 = sqrt(3)

_kw_to_hp = 1.34102209
_hp_to_kw = 0.74569987


def convert_kw_to_hp(kw: NumType) -> NumType:
    """
    Convert kw to horse-power.
    :param kw: The value of kilo-watts to be converted to hp.
    :return Horsepower :
    """
    return kw * _kw_to_hp


def convert_hp_to_kw(hp: NumType) -> NumType:
    """
    Convert horse-power to kW.
    :param hp: The value of horse power to be converted to kilo-watts.
    :return kilo-watts:
    """
    return hp * _hp_to_kw
