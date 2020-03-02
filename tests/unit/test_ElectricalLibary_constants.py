"""
The test functions for the electricallibrary/cable.config library.
"""

from ElectricalLibrary import constants as uc
import pytest


@pytest.mark.parametrize('kw, result',
                        [(1, 1.34102209),
                         (1.0, 1.34102209),
                         ])
def test_kw_to_hp(kw, result):
    """
    The function should return a float.
    """
    t_hp = uc.convert_kw_to_hp(kw)
    expected = result
    assert t_hp == expected


@pytest.mark.parametrize('hp, result',
                        [(1, 0.74569987),
                         (1.0, 0.74569987),
                         ])
def test_hp_to_kw_int(hp, result):
    """
    The function should return a float.
    """
    t_kw = uc.convert_hp_to_kw(hp)
    expected = result
    assert t_kw == expected
