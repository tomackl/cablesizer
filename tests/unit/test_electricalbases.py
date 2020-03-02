import pytest
import electricallibrary.electricalbases as eb


def test_electricalbase__init__():
    test_obj = eb.ElectricalBase(50, 'Hz')
    result = (50, 'Hz')
    assert tuple([test_obj._freq, test_obj._freq_unit]) == result


def test_electricalbase_scalar():
    test_obj = eb.ElectricalBase()
    test_obj.scalar = 415
    result = 415
    assert test_obj.scalar == result


def test_electricalbase_scalar_unit():
    test_obj = eb.ElectricalBase()
    test_obj.scalar = 'V'
    result = 'V'
    assert test_obj.scalar == result


def test_electricalbase_freq():
    test_obj = eb.ElectricalBase()
    test_obj.freq = 50
    result = 50
    assert test_obj.freq == result


def test_electricalbase_freq_unit():
    test_obj = eb.ElectricalBase()
    test_obj.freq_unit = 'Hz'
    result = 'Hz'
    assert test_obj.freq_unit == result


def test_volt__init__():
    test_obj = eb.Volt(550, 'V', 40, 'hz')
    result = (550, 'V', 40, 'hz')
    assert tuple([test_obj._volt,
                  test_obj._volt_unit,
                  test_obj._freq,
                  test_obj.freq_unit]) == result


def test_volt__add__obj():
    test_obj_a = eb.Volt(240, 'v', 50, 'hz')
    test_obj_b = eb.Volt(240, 'v', 50, 'hz')
    result = 480
    test_obj_c = test_obj_a + test_obj_b
    assert test_obj_c.volts == result


def test_volt__add__int_float():
    test_obj_a = eb.Volt(240, 'v', 50, 'hz')
    test_obj_b = 60
    result = 300
    test_obj_c = test_obj_a + test_obj_b
    assert test_obj_c.volts == result


def test_volt__sub__obj():
    test_obj_a = eb.Volt(240, 'v', 50, 'hz')
    test_obj_b = eb.Volt(240, 'v', 50, 'hz')
    result = 0
    test_obj_c = test_obj_a - test_obj_b
    assert test_obj_c.volts == result


def test_volt__sub__int_float():
    test_obj_a = eb.Volt(240, 'v', 50, 'hz')
    test_obj_b = 60
    result = 180
    test_obj_c = test_obj_a - test_obj_b
    assert test_obj_c.volts == result


def test_volt__mul__obj():
    test_obj_a = eb.Volt(10, 'volts', 50, 'hz')
    test_obj_b = eb.Volt(24, 'volts', 50, 'hz')
    result = 240
    test_obj_c = test_obj_a * test_obj_b
    assert test_obj_c.volts == result


def test_volt__mul__int_float():
    test_obj_a = eb.Volt(120, 'volts', 50, 'hz')
    test_obj_b = 3
    result = 360
    test_obj_c = test_obj_a * test_obj_b
    assert test_obj_c.volts == result


def test_volt__truediv__obj():
    test_obj_a = eb.Volt(240, 'volts', 50, 'hz')
    test_obj_b = eb.Volt(10, 'volts', 50, 'hz')
    result = 24
    test_obj_c = test_obj_a / test_obj_b
    assert test_obj_c.volts == result


def test_volt__truediv__int_float():
    test_obj_a = eb.Volt(360, 'volts', 50, 'hz')
    test_obj_b = 3
    result = 120
    test_obj_c = test_obj_a / test_obj_b
    assert test_obj_c.volts == result


def test_volt_freq():
    test_obj = eb.Volt(freq=40)
    result = 40
    assert test_obj.freq == result


def test_volt_freq_unit():
    test_obj = eb.Volt(freq_unit='Hz')
    result = 'Hz'
    assert test_obj.freq_unit == result


def test_volt_scalar():
    test_obj = eb.Volt()
    test_obj.scalar = 275
    test_obj.scalar_unit = 'Turns per inch'
    result = (275, 'Turns per inch')
    assert tuple([test_obj.scalar,
                  test_obj.scalar_unit]) == result


def test_amp__init__():
    test_obj = eb.Amp(10, 'A', 40, 'A')
    result = (10, 'A', 40, 'A')
    assert tuple([test_obj._amp,
                  test_obj._amp_unit,
                  test_obj._freq,
                  test_obj.freq_unit]) == result


def test_amp__add__obj():
    test_obj_a = eb.Amp(0.3, 'amps', 50, 'hz')
    test_obj_b = eb.Amp(0.7, 'amps', 50, 'hz')
    result = 1
    test_obj_c = test_obj_a + test_obj_b
    assert test_obj_c.amps == result


def test_amp__add__int_float():
    test_obj_a = eb.Amp(1.3, 'amps', 50, 'hz')
    test_obj_b = 0.7
    result = 2
    test_obj_c = test_obj_a + test_obj_b
    assert test_obj_c.amps == result


def test_amp__sub__obj():
    test_obj_a = eb.Amp(3, 'amps', 50, 'hz')
    test_obj_b = eb.Amp(7, 'amps', 50, 'hz')
    result = -4
    test_obj_c = test_obj_a - test_obj_b
    assert test_obj_c.amps == result


def test_amp__sub__int_float():
    test_obj_a = eb.Amp(1.3, 'amps', 50, 'hz')
    test_obj_b = 0.3
    result = 1
    test_obj_c = test_obj_a - test_obj_b
    assert test_obj_c.amps == result


def test_amp__mul__obj():
    test_obj_a = eb.Amp(2, 'amps', 50, 'hz')
    test_obj_b = eb.Amp(4, 'amps', 50, 'hz')
    result = 8
    test_obj_c = test_obj_a * test_obj_b
    assert test_obj_c.amps == result


def test_amp__mul__int_float():
    test_obj_a = eb.Amp(60.0, 'amps', 50, 'hz')
    test_obj_b = 4
    result = 240
    test_obj_c = test_obj_a * test_obj_b
    assert test_obj_c.amps == result


def test_truediv__mul__obj():
    test_obj_a = eb.Amp(4, 'amps', 50, 'hz')
    test_obj_b = eb.Amp(2, 'amps', 50, 'hz')
    result = 2
    test_obj_c = test_obj_a / test_obj_b
    assert test_obj_c.amps == result


def test_amp__truediv__int_float():
    test_obj_a = eb.Amp(240.0, 'amps', 50, 'hz')
    test_obj_b = 6
    result = 40
    test_obj_c = test_obj_a / test_obj_b
    assert test_obj_c.amps == result


def test_amp_scalar_unit():
    test_obj = eb.Amp()
    test_obj.amp_unit = 'A'
    result = 'A'
    assert test_obj.amp_unit == result


def test_amp_freq():
    test_obj = eb.Amp(freq=40)
    result = 40
    assert test_obj.freq == result


def test_amp_freq_unit():
    test_obj = eb.Amp(freq_unit='Hz')
    result = 'Hz'
    assert test_obj.freq_unit == result


def test_amp_scalar():
    test_obj = eb.Amp()
    test_obj.scalar = 275
    test_obj.scalar_unit = 'Turns per inch'
    result = (275, 'Turns per inch')
    assert tuple([test_obj.scalar,
                  test_obj.scalar_unit]) == result


def test_ohm__init__():
    test_obj = eb.Ohm(complex(0.3, 0.4), 'ohm', 50, 'hz')
    result = ((0.3+0.4j), 'ohm', 50, 'hz')
    assert tuple([test_obj.ohm,
                  test_obj.ohm_unit,
                  test_obj.freq,
                  test_obj.freq_unit]) == result


def test_ohm__add__obj():
    test_obj_a = eb.Ohm(complex(0.3, 0.4), 'ohm', 50, 'hz')
    test_obj_b = eb.Ohm(complex(0.7, 0.6), 'ohm', 50, 'hz')
    result = (1+1j)
    test_obj_c = test_obj_a + test_obj_b
    assert test_obj_c.ohm == result


def test_ohm__add__int_float():
    test_obj_a = eb.Ohm(complex(0.3, 0.4), 'ohm', 50, 'hz')
    test_obj_b = complex(1.7, 1.6)
    result = (2+2j)
    test_obj_c = test_obj_a + test_obj_b
    assert test_obj_c.ohm == result


def test_ohm__sub__obj():
    test_obj_a = eb.Ohm(complex(3, 4), 'ohm', 50, 'hz')
    test_obj_b = eb.Ohm(complex(7, 6), 'ohm', 50, 'hz')
    result = (-4-2j)
    test_obj_c = test_obj_a - test_obj_b
    assert test_obj_c.ohm == result


def test_ohm__sub__int_float():
    test_obj_a = eb.Ohm(complex(3, 4), 'ohm', 50, 'hz')
    test_obj_b = complex(1.7, 1.6)
    result = (1.3+2.4j)
    test_obj_c = test_obj_a - test_obj_b
    assert test_obj_c.ohm == result


def test_ohm__mul__obj():
    test_obj_a = eb.Ohm(complex(1, 2), 'ohm', 50, 'hz')
    test_obj_b = eb.Ohm(complex(3, 4), 'ohm', 50, 'hz')
    result = (-5+10j)
    test_obj_c = test_obj_a * test_obj_b
    assert test_obj_c.ohm == result


def test_ohm__mul__int_float():
    test_obj_a = eb.Ohm(complex(1, 4), 'ohm', 50, 'hz')
    test_obj_b = 3
    result = complex(3, 12)
    test_obj_c = test_obj_a * test_obj_b
    assert test_obj_c.ohm == result


def test_ohm__mul__complex():
    test_obj_a = eb.Ohm(complex(1, 4), 'ohm', 50, 'hz')
    test_obj_b = complex(3, 3)
    result = complex(-9, 15)
    test_obj_c = test_obj_a * test_obj_b
    assert test_obj_c.ohm == result


def test_ohm__truediv__obj():
    test_obj_a = eb.Ohm(complex(3, 4), 'ohm', 50, 'hz')
    test_obj_b = eb.Ohm(complex(1, 1), 'ohm', 50, 'hz')
    result = (3.5+0.5j)
    test_obj_c = test_obj_a / test_obj_b
    assert test_obj_c.ohm == result


def test_ohm__truediv__int_float():
    test_obj_a = eb.Ohm(complex(3, 12), 'ohm', 50, 'hz')
    test_obj_b = 3
    result = complex(1, 4)
    test_obj_c = test_obj_a / test_obj_b
    assert test_obj_c.ohm == result


def test_ohm__truediv__complex():
    test_obj_a = eb.Ohm(complex(3, 4), 'ohm', 50, 'hz')
    test_obj_b = complex(2, 2)
    result = complex(1.75, 0.25)
    test_obj_c = test_obj_a / test_obj_b
    assert test_obj_c.ohm == result


def test_ohm_scalar_unit():
    test_obj = eb.Ohm()
    test_obj.ohm_unit = 'ohm'
    result = 'ohm'
    assert test_obj.ohm_unit == result


def test_ohm_freq():
    test_obj = eb.Ohm(freq=50)
    result = 50
    assert test_obj.freq == result


def test_ohm_freq_unit():
    test_obj = eb.Ohm(freq_unit='Hz')
    result = 'Hz'
    assert test_obj.freq_unit == result


def test_ohm_scalar():
    test_obj = eb.Ohm()
    test_obj.scalar = 275
    test_obj.scalar_unit = 'Turns per inch'
    result = (275, 'Turns per inch')
    assert tuple([test_obj.scalar,
                  test_obj.scalar_unit]) == result


def test_ohm_r():
    test_obj = eb.Ohm()
    test_obj.r = 0.6
    result = 0.6
    assert test_obj.r == result


def test_ohm_x():
    test_obj = eb.Ohm()
    test_obj.x = 1.5
    result = 1.5
    assert test_obj.x == result


def test_ohm_z():
    test_obj = eb.Ohm()
    test_obj.z = complex(0.3, 0.4)
    result = 0.5
    assert test_obj.z == result


def test_pwr__init__():
    test_obj = eb.Power(complex(110, 10), 'VA', 50, 'hz')
    result = ((110+10j), 'VA', 50, 'hz')
    assert tuple([test_obj.power,
                  test_obj.power_unit,
                  test_obj.freq,
                  test_obj.freq_unit]) == result


def test_pwr__add__obj():
    test_obj_a = eb.Power(complex(100, 9), 'VA', 50, 'hz')
    test_obj_b = eb.Power(complex(50, 5), 'VA', 50, 'hz')
    result = (150+14j)
    test_obj_c = test_obj_a + test_obj_b
    assert test_obj_c.power == result


def test_pwr__add__complex():
    test_obj_a = eb.Power(complex(10.5, 0.5), 'VA', 50, 'hz')
    test_obj_b = complex(1.5, 1.5)
    result = (12+2j)
    test_obj_c = test_obj_a + test_obj_b
    assert test_obj_c.power == result


def test_pwr__sub__obj():
    test_obj_a = eb.Power(complex(150, 15), 'VA', 50, 'hz')
    test_obj_b = eb.Power(complex(50, 5), 'VA', 50, 'hz')
    result = (100+10j)
    test_obj_c = test_obj_a - test_obj_b
    assert test_obj_c.power == result


def test_pwr__sub__int_float():
    test_obj_a = eb.Power(complex(150, 15), 'VA', 50, 'hz')
    test_obj_b = complex(20, 5)
    result = (130+10j)
    test_obj_c = test_obj_a - test_obj_b
    assert test_obj_c.power == result


def test_pwr__mul__obj():
    test_obj_a = eb.Power(complex(10, 20), 'VA', 50, 'hz')
    test_obj_b = eb.Power(complex(3, 4), 'VA', 50, 'hz')
    result = (-50+100j)
    test_obj_c = test_obj_a * test_obj_b
    assert test_obj_c.power == result


def test_pwr__mul__int_float():
    test_obj_a = eb.Power(complex(20, 20), 'VA', 50, 'hz')
    test_obj_b = 3
    result = complex(60, 60)
    test_obj_c = test_obj_a * test_obj_b
    assert test_obj_c.power == result


def test_pwr__mul__complex():
    test_obj_a = eb.Power(complex(20, 20), 'VA', 50, 'hz')
    test_obj_b = complex(3, 4)
    result = complex(-20, 140)
    test_obj_c = test_obj_a * test_obj_b
    assert test_obj_c.power == result


def test_pwr__truediv__obj():
    test_obj_a = eb.Power(complex(150, 50), 'VA', 50, 'hz')
    test_obj_b = eb.Power(complex(1, 1), 'VA', 50, 'hz')
    result = (100-50j)
    test_obj_c = test_obj_a / test_obj_b
    assert test_obj_c.power == result


def test_pwr__truediv__int_float():
    test_obj_a = eb.Power(complex(150, 30), 'VA', 50, 'hz')
    test_obj_b = 3
    result = complex(50, 10)
    test_obj_c = test_obj_a / test_obj_b
    assert test_obj_c.power == result


def test_pwr__truediv__complex():
    test_obj_a = eb.Power(complex(150, 50), 'VA', 50, 'hz')
    test_obj_b = complex(2, 2)
    result = complex(50, -25)
    test_obj_c = test_obj_a / test_obj_b
    assert test_obj_c.power == result


def test_pwr_scalar_unit():
    test_obj = eb.Power()
    test_obj.power_unit = 'VA'
    result = 'VA'
    assert test_obj.power_unit == result


def test_pwr_freq():
    test_obj = eb.Power(freq=50)
    result = 50
    assert test_obj.freq == result


def test_pwr_freq_unit():
    test_obj = eb.Power(freq_unit='Hz')
    result = 'Hz'
    assert test_obj.freq_unit == result


def test_pwr_p():
    test_obj = eb.Power()
    test_obj.p = 0.6
    result = 0.6
    assert test_obj.p == result


def test_pwr_q():
    test_obj = eb.Power()
    test_obj.q = 1.5
    result = 1.5
    assert test_obj.q == result


def test_pwr_s():
    test_obj = eb.Power()
    test_obj.s = complex(0.3, 0.4)
    result = 0.5
    assert test_obj.s == result


def test_electrical_calc__init__():
    test_obj_a = eb.Amp()
    test_obj_b = eb.Volt()
    test_obj_c = eb.ElectricalCalc(test_obj_a, test_obj_b)
    result = False
    assert test_obj_c._ohm_exists == result


def test_electrical_calc_determine_diff_obj():
    test_obj_a = eb.Amp()
    test_obj_b = eb.Volt()
    test_obj_c = eb.ElectricalCalc(test_obj_a, test_obj_b)
    result = True
    assert test_obj_c._amp_exists == result


def test_electrical_calc_determine_same_obj():
    test_obj_a = eb.Amp()
    test_obj_b = eb.Amp()
    test_obj_c = eb.ElectricalCalc(test_obj_a, test_obj_b)
    result = False
    assert test_obj_c._amp_exists == result


def test_electrical_calc_compare_bases():
    test_obj_a = eb.Amp(10, 'A', 50, 'Hz')
    test_obj_b = eb.Volt(240, 'V', 50, 'Hz')
    test_obj_c = eb.ElectricalCalc(test_obj_a, test_obj_b)
    result = True
    assert test_obj_c._freq_equal == result


def test_electrical_calc_power_volt_amp():
    test_obj_a = eb.Amp(10, 'A', 50, 'Hz')
    test_obj_b = eb.Amp(240, 'A', 50, 'Hz')
    test_obj_c = eb.ElectricalCalc(test_obj_b, test_obj_a)
    power_obj = test_obj_c.calc_power()
    result = None
    assert power_obj == result


def test_electrical_calc_power_volt_amp():
    test_obj_a = eb.Amp(10, 'A', 50, 'Hz')
    test_obj_b = eb.Volt(240, 'V', 50, 'Hz')
    test_obj_c = eb.ElectricalCalc(test_obj_b, test_obj_a)
    power_obj = test_obj_c.calc_power()
    result = (2400, 'V*A')
    assert (power_obj.power, power_obj.power_unit) == result


def test_electrical_calc_power_amp_ohms():
    test_obj_a = eb.Amp(10, 'A', 50, 'Hz')
    test_obj_b = eb.Ohm(complex(2, 2), 'Ohms', 50, 'Hz')
    test_obj_c = eb.ElectricalCalc(test_obj_b, test_obj_a)
    power_obj = test_obj_c.calc_power()
    result = ((200+200j), 'A^2*Ohms')
    assert (power_obj.power, power_obj.power_unit) == result


def test_electrical_calc_power_volts_ohms():
    test_obj_a = eb.Volt(110, 'V', 50, 'Hz')
    test_obj_b = eb.Ohm(complex(2, 2), 'Ohms', 50, 'Hz')
    test_obj_c = eb.ElectricalCalc(test_obj_b, test_obj_a)
    power_obj = test_obj_c.calc_power()
    result = ((3025-3025j), 'V^2/Ohms')
    assert (power_obj.power, power_obj.power_unit) == result


def test_electrical_calc_current_volt_volt():
    test_obj_a = eb.Volt(10, 'V', 50, 'Hz')
    test_obj_b = eb.Volt(240, 'V', 50, 'Hz')
    test_obj_c = eb.ElectricalCalc(test_obj_b, test_obj_a)
    power_obj = test_obj_c.calc_current()
    result = None
    assert power_obj == result


def test_electrical_calc_current_power_volt():
    test_obj_a = eb.Power(complex(1000, 2), 'W', 50, 'Hz')
    test_obj_b = eb.Volt(25, 'Ohms', 50, 'Hz')
    test_obj_c = eb.ElectricalCalc(test_obj_b, test_obj_a)
    current_obj = test_obj_c.calc_current()
    result = ((40+0.08j), 'Amps (W/Ohms)')
    assert (current_obj.amps, current_obj.amp_unit) == result


def test_electrical_calc_current_volts_ohms():
    test_obj_a = eb.Volt(1000, 'V', 50, 'Hz')
    test_obj_b = eb.Ohm(complex(2, 2), 'Ohms', 50, 'Hz')
    test_obj_c = eb.ElectricalCalc(test_obj_b, test_obj_a)
    current_obj = test_obj_c.calc_current()
    result = ((250-250j), 'Amps (V/Ohms)')
    assert (current_obj.amps, current_obj.amp_unit) == result


def test_electrical_calc_voltage_amp_ohms():
    test_obj_a = eb.Amp(100, 'A', 50, 'Hz')
    test_obj_b = eb.Ohm(complex(2, 2), 'Ohms', 50, 'Hz')
    test_obj_c = eb.ElectricalCalc(test_obj_b, test_obj_a)
    current_obj = test_obj_c.calc_voltage()
    result = ((200+200j), 'Volts (A*Ohms)')
    assert (current_obj.volts, current_obj.volt_unit) == result


def test_electrical_calc_voltage_amp_power():
    test_obj_a = eb.Amp(75, 'A', 50, 'Hz')
    test_obj_b = eb.Power(complex(75, 75), 'W', 50, 'Hz')
    test_obj_c = eb.ElectricalCalc(test_obj_b, test_obj_a)
    current_obj = test_obj_c.calc_voltage()
    result = ((1+1j), 'Volts (W/A)')
    assert (current_obj.volts, current_obj.volt_unit) == result


def test_electrical_calc_impedance_volt_amp():
    test_obj_a = eb.Amp(110, 'A', 50, 'Hz')
    test_obj_b = eb.Volt(110, 'V', 50, 'Hz')
    test_obj_c = eb.ElectricalCalc(test_obj_b, test_obj_a)
    current_obj = test_obj_c.calc_impedance()
    result = (1.0, 'Ohms (V/A)')
    assert (current_obj.ohm, current_obj.ohm_unit) == result


def test_electrical_calc_impedance_amp_power():
    test_obj_a = eb.Amp(10, 'A', 50, 'Hz')
    test_obj_b = eb.Power(complex(100, 100), 'W', 50, 'Hz')
    test_obj_c = eb.ElectricalCalc(test_obj_b, test_obj_a)
    current_obj = test_obj_c.calc_impedance()
    result = ((1 + 1j), 'Ohms (W/A^2)')
    assert (current_obj.ohm, current_obj.ohm_unit) == result
