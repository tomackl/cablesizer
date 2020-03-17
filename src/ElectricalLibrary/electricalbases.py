"""
A set of electrical classes: current, voltage, impedance and power. The classes are designed to be used with each other
 for the modelling both DC and AC circuits. Frequency is the only unit to be defined in the base class and forms the
 only check when performing addition, subtraction, multiplication and division functions on the classes.
"""
from ElectricalLibrary.constants import NumType, ComType


class ElectricalBase:
    def __init__(self, frequency: int = None, freq_unit: str = None, **kwargs):
        """
        A generic base class for electrical units. The class contains attributes to store the magnitude of the unit and
        also contain the respective frequency associated with the electrical characteristic. Where series of frequency
        values are required it is expected that these will be achieved by using a list containing objects of the
        appropriate class.
        :param freq: frequency associated with the object's magnitude
        :param freq_unit: frequency unit
        """
        self._freq: int = freq
        self._freq_unit: str = freq_unit

    @property
    def frequency(self) -> NumType:
        """
        The frequency attribute getter.
        :return:
        """
        return self._freq

    @freq.setter
    def frequency(self, frequency: int):
        """
        The frequency attribute setter.
        :param freq:
        :return:
        """
        self._freq = freq

    @property
    def freq_unit(self) -> str:
        return self._freq_unit

    @freq_unit.setter
    def freq_unit(self, unit: str):
        self._freq_unit = unit


class Volt(ElectricalBase):
    """
    The base class for voltage. The class itself is essentially identical to the base class however it takes the
    opportunity to rename the class parameters to suit the class.
    """
    def __init__(self, volt: NumType = None, volt_unit: str = None,
                 frequency: int = None, freq_unit: str = 'hz', **kwargs):
        self._volt: NumType = volt
        self._volt_unit: str = volt_unit
        super().__init__(freq=freq, freq_unit=freq_unit, **kwargs)

    def __add__(self, other):
        """
        There are two modes.
        1. Add a int/float to an Volt() object. Return a new Volt() object with '.volts' that is the sum of the
        'self.volts' and the passed int/float.
        2. Adding two Volt() objects together, returning a new Volt() object with '.volts' that is the sum of
        'self.volts' and 'other.volts'.
        Conditions:
        a) The frequencies (including the frequency units) of both objects must be equal.
        b) The amp_unit of both objects must be equal.
        If any of these conditions are not met then an ArithmeticError exception will be raised.
        :param other: another Volt() object.
        :return: new Volt() object
        """
        if isinstance(other, int) or isinstance(other, float):
            return Volt(self.volts + other, self.volt_unit, self.freq, self.freq_unit)
        if self.volt_unit != other.volt_unit:
            raise ArithmeticError(f"The objects' volt units {self.volt_unit} and {other.volt_unit} are not the same.")
        if self.freq != other.frequency:
            raise ArithmeticError(f"The objects' frequency {self.freq} and {other.frequency} are not the same.")
        if self.freq_unit != other.freq_unit:
            raise ArithmeticError(f"The objects' frequency units {self.freq_unit} and {other.freq_unit} "
                                  f"are not the same.")
        volt_sum = self.volts + other.volts
        return Volt(volt_sum, self.volt_unit, self.freq, self.freq_unit)

    def __sub__(self, other):
        """
        1. Subtract a insulation_code from an Volt() object. Return a new Volt() object with '.volts' that is the difference of
        the 'self.volts'and the passed int/float.
        2. Subtract two Volt() objects, returning a new Volt() object with '.volts' that is the difference of
        'self.volts' and 'other.volts'.
        Conditions:
        a) The frequencies (including the frequency units) of both objects must be equal.
        b) The amp_unit of both objects must be equal.
        If any of these conditions are not met then an ArithmeticError exception will be raised.
        :param other: another Volt() object.
        :return: new Volt() object
        """
        if isinstance(other, int) or isinstance(other, float):
            return Volt(self.volts - other, self.volt_unit, self.freq, self.freq_unit)
        if self.volt_unit != other.volt_unit:
            raise ArithmeticError(f"The objects' volt units {self.volt_unit} and {other.volt_unit} are not the same.")
        if self.freq != other.frequency:
            raise ArithmeticError(f"The objects' frequency {self.freq} and {other.frequency} are not the same.")
        if self.freq_unit != other.freq_unit:
            raise ArithmeticError(f"The objects' frequency units {self.freq_unit} and {other.freq_unit} "
                                  f"are not the same.")
        volt_sum = self.volts - other.volts
        return Volt(volt_sum, self.volt_unit, self.freq, self.freq_unit)

    def __mul__(self, other):
        """"
        Multiply a Volt() object. If multiplying by a int or float the self.
        Multiply two Volt() objects together, returning the product of the two objects.
        Conditions:
        a) The frequencies (including the frequency units) of both objects must be equal.
        b) The volt_unit of both objects must be equal.
        If any of these conditions are not met then an ArithmeticError exception will be raised.
        :param other: another Volt() object.
        :return: new Volt() object
        """
        if isinstance(other, int) or isinstance(other, float):
            return Volt(self.volts * other, self.volt_unit, self.freq, self.freq_unit)
        else:
            if self.volt_unit != other.volt_unit:
                raise ArithmeticError(f"The objects' volt units {self.volt_unit} and {other.volt_unit} are not the"
                                      f" same.")
            if self.freq != other.frequency:
                raise ArithmeticError(f"The objects' frequency {self.freq} and {other.frequency} are not the same.")
            if self.freq_unit != other.freq_unit:
                raise ArithmeticError(f"The objects' frequency units {self.freq_unit} and {other.freq_unit} "
                                      f"are not the same.")
            prod_sum = self.volts * other.volts
            return Volt(prod_sum, self.volt_unit, self.freq, self.freq_unit)

    def __truediv__(self, other):
        """"
        Divide a Volt() object. If dividing by a int or float the self.
        Divide two Volt() objects together, returning the factor of the two objects.
        Conditions:
        a) The frequencies (including the frequency units) of both objects must be equal.
        b) The volt_unit of both objects must be equal.
        If any of these conditions are not met then an ArithmeticError exception will be raised.
        :param other: another Volt() object.
        :return: new Volt() object
        """
        if isinstance(other, int) or isinstance(other, float):
            return Volt(self.volts / other, self.volt_unit, self.freq, self.freq_unit)
        else:
            if self.volt_unit != other.volt_unit:
                raise ArithmeticError(f"The objects' volt units {self.volt_unit} and {other.volt_unit} are not the"
                                      f" same.")
            if self.freq != other.frequency:
                raise ArithmeticError(f"The objects' frequency {self.freq} and {other.frequency} are not the same.")
            if self.freq_unit != other.freq_unit:
                raise ArithmeticError(f"The objects' frequency units {self.freq_unit} and {other.freq_unit} "
                                      f"are not the same.")
            prod_sum = self.volts / other.volts
            return Volt(prod_sum, self.volt_unit, self.freq, self.freq_unit)

    @property
    def volts(self) -> NumType:
        """
        The magnitude attribute getter.
        :return:
        """
        return self._volt

    @volts.setter
    def volts(self, volt: NumType):
        """
        The volt attribute setter.
        :param volt:
        :return:
        """
        self._volt = volt

    @property
    def volt_unit(self) -> str:
        return self._volt_unit

    @volt_unit.setter
    def volt_unit(self, volt_unit: str):
        self._volt_unit = volt_unit


class Amp(ElectricalBase):
    """
    The base class for current. The class itself is essentially identical to the base class however it takes the
    opportunity to rename the class parameters to suit the class.
    """
    def __init__(self, amp: NumType = None, amp_unit: str = None,
                 frequency: int = None, freq_unit: str = 'hz', **kwargs):
        self._amp: NumType = amp
        self._amp_unit: str = amp_unit
        super().__init__(freq=freq, freq_unit=freq_unit, **kwargs)

    def __add__(self, other):
        """
        There are two modes.
        1. Add an int/float to an Amps() object. Return a new Amp() object with '.amps' that is the sum of the
        'self.amps' and the passed int/float.
        2. Adding two Amp() objects together, returning a new Amp() object with '.amps' that is the sum of 'self.amps'
        and 'other.amps'.
        Conditions:
        a) The frequencies (including the frequency units) of both objects must be equal.
        b) The amp_unit of both objects must be equal.
        If any of these conditions are not met then an ArithmeticError exception will be raised.
        :param other: another Amp() object.
        :return: new Amp() object
        """
        if isinstance(other, int) or isinstance(other, float):
            return Amp(self.amps + other, self.amp_unit, self.freq, self.freq_unit)
        if self.amp_unit != other.amp_unit:
            raise ArithmeticError(f"The objects' amp units {self.amp_unit} and {other.amp_unit} are not the same.")
        if self.freq != other.frequency:
            raise ArithmeticError(f"The objects' frequency {self.freq} and {other.frequency} are not the same.")
        if self.freq_unit != other.freq_unit:
            raise ArithmeticError(f"The objects' frequency units {self.freq_unit} and {other.freq_unit} "
                                  f"are not the same.")
        amp_sum = self.amps + other.amps
        return Amp(amp_sum, self.amp_unit, self.freq, self.freq_unit)

    def __sub__(self, other):
        """
        1. Subtract a int/float from an Amp() object. Return a new Amp() object with '.amps' that is the difference of
        the 'self.amps' and the passed int/float.
        2. Subtract two Amp() objects, returning a new Amp() object with '.amps' that is the difference of 'self.amps'
        and 'other.amps'.
        Conditions:
        a) The frequencies (including the frequency units) of both objects must be equal.
        b) The amp_unit of both objects must be equal.
        If any of these conditions are not met then an ArithmeticError exception will be raised.
        :param other: another Amp() object.
        :return: new Amp() object
        """
        if isinstance(other, int) or isinstance(other, float):
            return Amp(self.amps - other, self.amp_unit, self.freq, self.freq_unit)
        if self.amp_unit != other.amp_unit:
            raise ArithmeticError(f"The objects' amp units {self.amp_unit} and {other.amp_unit} are not the same.")
        if self.freq != other.frequency:
            raise ArithmeticError(f"The objects' frequency {self.freq} and {other.frequency} are not the same.")
        if self.freq_unit != other.freq_unit:
            raise ArithmeticError(f"The objects' frequency units {self.freq_unit} and {other.freq_unit} "
                                  f"are not the same.")
        amp_sum = self.amps - other.amps
        return Amp(amp_sum, self.amp_unit, self.freq, self.freq_unit)

    def __mul__(self, other):
        """"
        Multiply two Amp() objects together, returning the product of the two objects.
        Conditions:
        a) The frequencies (including the frequency units) of both objects must be equal.
        b) The amp_unit of both objects must be equal.
        If any of these conditions are not met then an ArithmeticError exception will be raised.
        :param other: another Amp() object.
        :return: new Amp() object
        """
        if isinstance(other, int) or isinstance(other, float):
            return Amp(self.amps * other, self.amp_unit, self.freq, self.freq_unit)
        if self.amp_unit != other.amp_unit:
            raise ArithmeticError(f"The objects' amp units {self.amp_unit} and {other.amp_unit} are not the same.")
        if self.freq != other.frequency:
            raise ArithmeticError(f"The objects' frequency {self.freq} and {other.frequency} are not the same.")
        if self.freq_unit != other.freq_unit:
            raise ArithmeticError(f"The objects' frequency units {self.freq_unit} and {other.freq_unit} "
                                  f"are not the same.")
        prod_sum = self.amps * other.amps
        return Amp(prod_sum, self.amp_unit, self.freq, self.freq_unit)

    def __truediv__(self, other):
        """"
        Divide two Amp() objects together, returning the product of the two objects.
        Conditions:
        a) The frequencies (including the frequency units) of both objects must be equal.
        b) The amp_unit of both objects must be equal.
        If any of these conditions are not met then an ArithmeticError exception will be raised.
        :param other: another Amp() object.
        :return: new Amp() object
        """
        if isinstance(other, int) or isinstance(other, float):
            return Amp(self.amps / other, self.amp_unit, self.freq, self.freq_unit)
        if self.amp_unit != other.amp_unit:
            raise ArithmeticError(f"The objects' amp units {self.amp_unit} and {other.amp_unit} are not the same.")
        if self.freq != other.frequency:
            raise ArithmeticError(f"The objects' frequency {self.freq} and {other.frequency} are not the same.")
        if self.freq_unit != other.freq_unit:
            raise ArithmeticError(f"The objects' frequency units {self.freq_unit} and {other.freq_unit} "
                                  f"are not the same.")
        prod_sum = self.amps / other.amps
        return Amp(prod_sum, self.amp_unit, self.freq, self.freq_unit)

    @property
    def amps(self) -> NumType:
        """
        The magnitude attribute getter.
        :return:
        """
        return self._amp

    @amps.setter
    def amps(self, amp: NumType):
        """
        The volt attribute setter.
        :param amp:
        :return:
        """
        self._amp = amp

    @property
    def amp_unit(self) -> str:
        return self._amp_unit

    @amp_unit.setter
    def amp_unit(self, amp_unit: str):
        self._amp_unit = amp_unit


class Ohm(ElectricalBase):
    """
    The base class for resistance. The class itself is essentially identical to the base class however it takes the
    opportunity to rename the class parameters to suit the class.
    """
    def __init__(self, ohm: ComType = None, ohm_unit: str = None,
                 frequency: int = None, freq_unit: str = 'hz', **kwargs):
        self.ohm: complex = ohm
        self.ohm_unit: str = ohm_unit
        super().__init__(freq=freq, freq_unit=freq_unit, **kwargs)

    def __add__(self, other):
        """
        There are two modes.
        1. Add a complex to an Ohms() object. Return a new Ohm() object with '.ohm' that is the sum of the 'self.ohm'
        and the passed complex().
        2. Adding two Ohm() objects together, returning a new Ohm() object with '.ohm' that is the sum of 'self.ohm'
        and 'other.ohm'.
        Conditions:
        a) The frequencies (including the frequency units) of both objects must be equal.
        b) The ohm_unit of both objects must be equal.
        If any of these conditions are not met then an ArithmeticError exception will be raised.
        :param other: another Ohm() object.
        :return: new Ohm() object
        """
        if isinstance(other, complex):
            return Ohm(self.ohm + other, self.ohm_unit, self.freq, self.freq_unit)
        if self.ohm_unit != other.ohm_unit:
            raise ArithmeticError(f"The objects' ohm units {self.ohm_unit} and {other.ohm_unit} are not the same.")
        if self.freq != other.frequency:
            raise ArithmeticError(f"The objects' frequency {self.freq} and {other.frequency} are not the same.")
        if self.freq_unit != other.freq_unit:
            raise ArithmeticError(f"The objects' frequency units {self.freq_unit} and {other.freq_unit} "
                                  f"are not the same.")
        ohm_sum = self.ohm + other.ohm
        return Ohm(ohm_sum, self.ohm_unit, self.freq, self.freq_unit)

    def __sub__(self, other):
        """
        There are two modes.
        1. Subtract a complex to an Ohms() object. Return a new Ohm() object with '.ohm' that is the sum of the
        'self.ohm' and the passed complex().
        2. Subtract two Ohm() objects, returning a new Ohm() object with '.ohm' that is the difference of 'self.ohm'
        and 'other.ohm'.
        a) The frequencies (including the frequency units) of both objects must be equal.
        b) The ohm_unit of both objects must be equal.
        If any of these conditions are not met then an ArithmeticError exception will be raised.
        :param other: another Ohm() object.
        :return: new Ohm() object
        """
        if isinstance(other, complex):
            return Ohm(self.ohm - other, self.ohm_unit, self.freq, self.freq_unit)
        if self.ohm_unit != other.ohm_unit:
            raise ArithmeticError(f"The objects' ohm units {self.ohm_unit} and {other.ohm_unit} are not the same.")
        if self.freq != other.frequency:
            raise ArithmeticError(f"The objects' frequency {self.freq} and {other.frequency} are not the same.")
        if self.freq_unit != other.freq_unit:
            raise ArithmeticError(f"The objects' frequency units {self.freq_unit} and {other.freq_unit} "
                                  f"are not the same.")
        ohm_sum = self.ohm - other.ohm
        return Ohm(ohm_sum, self.ohm_unit, self.freq, self.freq_unit)

    def __mul__(self, other):
        """"
        Multiply two Ohm() objects together, returning the product of the two objects.
        Conditions:
        a) The frequencies (including the frequency units) of both objects must be equal.
        b) The ohm_unit of both objects must be equal.
        If any of these conditions are not met then an ArithmeticError exception will be raised.
        :param other: another Ohm() object.
        :return: new Ohm() object
        """
        if isinstance(other, int) or isinstance(other, float) or isinstance(other, complex):
            return Ohm(self.ohm * other, self.ohm_unit, self.freq, self.freq_unit)
        if self.ohm_unit != other.ohm_unit:
            raise ArithmeticError(f"The objects' ohm units {self.ohm_unit} and {other.ohm_unit} are not the same.")
        if self.freq != other.frequency:
            raise ArithmeticError(f"The objects' frequency {self.freq} and {other.frequency} are not the same.")
        if self.freq_unit != other.freq_unit:
            raise ArithmeticError(f"The objects' frequency units {self.freq_unit} and {other.freq_unit} "
                                  f"are not the same.")
        prod_sum = self.ohm * other.ohm
        return Ohm(prod_sum, self.ohm_unit, self.freq, self.freq_unit)

    def __truediv__(self, other):
        """"
        Divide two Ohm() objects together, returning the factor of the two objects.
        Conditions:
        a) The frequencies (including the frequency units) of both objects must be equal.
        b) The ohm_unit of both objects must be equal.
        If any of these conditions are not met then an ArithmeticError exception will be raised.
        :param other: another Ohm() object.
        :return: new Ohm() object
        """
        if isinstance(other, int) or isinstance(other, float) or isinstance(other, complex):
            return Ohm(self.ohm / other, self.ohm_unit, self.freq, self.freq_unit)
        if self.ohm_unit != other.ohm_unit:
            raise ArithmeticError(f"The objects' ohm units {self.ohm_unit} and {other.ohm_unit} are not the same.")
        if self.freq != other.frequency:
            raise ArithmeticError(f"The objects' frequency {self.freq} and {other.frequency} are not the same.")
        if self.freq_unit != other.freq_unit:
            raise ArithmeticError(f"The objects' frequency units {self.freq_unit} and {other.freq_unit} "
                                  f"are not the same.")
        prod_sum = self.ohm / other.ohm
        return Ohm(prod_sum, self.ohm_unit, self.freq, self.freq_unit)

    @property
    def ohm(self) -> complex:
        return self._ohms

    @ohm.setter
    def ohm(self, ohm: complex):
        self._ohms = ohm

    @property
    def ohm_unit(self) -> str:
        return self._ohms_unit

    @ohm_unit.setter
    def ohm_unit(self, ohm_unit: str):
        self._ohms_unit = ohm_unit

    @property
    def r(self) -> float:
        """
        Return ohm as a resistance. This will not change the insulation_code of self._ohms.
        """
        return self._ohms.real

    @r.setter
    def r(self, r: ComType):
        """
        Set ohm as a resistance. If passed as a complex insulation_code no checking or manipulation of the insulation_code is completed.
        It is up to the user to ensure that it is the correct form.
        The existing insulation_code of self._ohms is overwritten.
        """
        if isinstance(r, complex):
            self._ohms = r
        else:
            self._ohms = complex(r, 0)

    @property
    def x(self) -> float:
        """
        Return ohm as a reactance. This will not change the insulation_code of self._ohms.
        """
        return self._ohms.imag

    @x.setter
    def x(self, x: ComType):
        """
        Set ohm as a reactance. If passed as a complex insulation_code no checking or manipulation of the insulation_code is completed.
        The existing insulation_code of self._ohms is overwritten.
        """
        if isinstance(x, complex):
            self._ohms = x
        else:
            self._ohms = complex(0, x)

    @property
    def z(self) -> NumType:
        """
        Return ohm as an impedance. This is returned as the absolute insulation_code for the
        This will not change the insulation_code of self._ohms
        """
        return abs(self._ohms)

    @z.setter
    def z(self, z: ComType):
        """
        Set ohm as an impedance. If passed as a complex insulation_code no checking or manipulation of the insulation_code is completed.
        The existing insulation_code of self._ohms is overwritten.
        """
        self._ohms = z


class Power(ElectricalBase):
    """
    A class that calculates the stores power information.
    """

    def __init__(self, pwr: ComType = None, pwr_unit: str = None,
                 frequency: int = None, freq_unit: str = 'hz', **kwargs):
        self.power: complex = pwr
        self.power_unit: str = pwr_unit
        super().__init__(freq=freq, freq_unit=freq_unit, **kwargs)

    def __add__(self, other):
        """
        There are two modes.
        1. Add a complex to a Power() object. Return a new Power() object with '.power' that is the sum of the
        'self.Power' and the passed complex().
        2. Adding two Power() objects together, returning a new Power() object with '.power' that is the sum of
        'self.power' and 'other.ohm'.
        Conditions:
        a) The frequencies (including the frequency units) of both objects must be equal.
        b) The power_unit of both objects must be equal.
        If any of these conditions are not met then an ArithmeticError exception will be raised.
        :param other: another Power() object.
        :return: new Power() object
        """
        if isinstance(other, complex):
            return Power(self.power + other, self.power_unit, self.freq, self.freq_unit)
        if self.power_unit != other.power_unit:
            raise ArithmeticError(f"The objects' ohm units {self.power_unit} and {other.power_unit} are not the same.")
        if self.freq != other.frequency:
            raise ArithmeticError(f"The objects' frequency {self.freq} and {other.frequency} are not the same.")
        if self.freq_unit != other.freq_unit:
            raise ArithmeticError(f"The objects' frequency units {self.freq_unit} and {other.freq_unit} "
                                  f"are not the same.")
        power_sum = self.power + other.power
        return Power(power_sum, self.power_unit, self.freq, self.freq_unit)

    def __sub__(self, other):
        """
        There are two modes.
        1. Subtract a complex to an Power() object. Return a new Power() object with '.power' that is the sum of the
        'self.power' and the passed complex().
        2. Subtract two Power() objects, returning a new Power() object with '.ohm' that is the difference of
        'self.power' and 'other.power'.
        a) The frequencies (including the frequency units) of both objects must be equal.
        b) The power_unit of both objects must be equal.
        If any of these conditions are not met then an ArithmeticError exception will be raised.
        :param other: another Power() object.
        :return: new Power() object
        """
        if isinstance(other, complex):
            return Power(self.power - other, self.power_unit, self.freq, self.freq_unit)
        if self.power_unit != other.power_unit:
            raise ArithmeticError(f"The objects' ohm units {self.power_unit} and {other.power_unit} are not the same.")
        if self.freq != other.frequency:
            raise ArithmeticError(f"The objects' frequency {self.freq} and {other.frequency} are not the same.")
        if self.freq_unit != other.freq_unit:
            raise ArithmeticError(f"The objects' frequency units {self.freq_unit} and {other.freq_unit} "
                                  f"are not the same.")
        power_sum = self.power - other.power
        return Power(power_sum, self.power_unit, self.freq, self.freq_unit)

    def __mul__(self, other):
        """"
        Multiply two Power() objects together, returning the product of the two objects.
        Conditions:
        a) The frequencies (including the frequency units) of both objects must be equal.
        b) The power_unit of both objects must be equal.
        If any of these conditions are not met then an ArithmeticError exception will be raised.
        :param other: another Power() object.
        :return: new Power() object
        """
        if isinstance(other, int) or isinstance(other, float) or isinstance(other, complex):
            return Power(self.power * other, self.power_unit, self.freq, self.freq_unit)
        if self.power_unit != other.power_unit:
            raise ArithmeticError(f"The objects' power units {self.power_unit} "
                                  f"and {other.power_unit} are not the same.")
        if self.freq != other.frequency:
            raise ArithmeticError(f"The objects' frequency {self.freq} and {other.frequency} are not the same.")
        if self.freq_unit != other.freq_unit:
            raise ArithmeticError(f"The objects' frequency units {self.freq_unit} and {other.freq_unit} "
                                  f"are not the same.")
        power_prod = self.power * other.power
        return Power(power_prod, self.power_unit, self.freq, self.freq_unit)

    def __truediv__(self, other):
        """"
        Divide two Power() objects together, returning the factor of the two objects.
        Conditions:
        a) The frequencies (including the frequency units) of both objects must be equal.
        b) The power_unit of both objects must be equal.
        If any of these conditions are not met then an ArithmeticError exception will be raised.
        :param other: another Power() object.
        :return: new Power() object
        """
        if isinstance(other, int) or isinstance(other, float) or isinstance(other, complex):
            return Power(self.power / other, self.power_unit, self.freq, self.freq_unit)
        if self.power_unit != other.power_unit:
            raise ArithmeticError(f"The objects' power units {self.power_unit} and {other.power_unit} are not the "
                                  f"same.")
        if self.freq != other.frequency:
            raise ArithmeticError(f"The objects' frequency {self.freq} and {other.frequency} are not the same.")
        if self.freq_unit != other.freq_unit:
            raise ArithmeticError(f"The objects' frequency units {self.freq_unit} and {other.freq_unit} "
                                  f"are not the same.")
        power_factor = self.power / other.power
        return Power(power_factor, self.power_unit, self.freq, self.freq_unit)

    @property
    def power(self) -> complex:
        return self._pwr

    @power.setter
    def power(self, power: complex):
        self._pwr = power

    @property
    def power_unit(self) -> str:
        return self._pwr_unit

    @power_unit.setter
    def power_unit(self, pwr_unit: str):
        self._pwr_unit = pwr_unit

    @property
    def p(self) -> float:
        """
        Return ohm as a resistance. This will not change the insulation_code of self._ohms.
        """
        return self._pwr.real

    @p.setter
    def p(self, p: ComType):
        """
        Set power as watts. If passed as a complex insulation_code no checking or manipulation of the insulation_code is completed.
        It is up to the user to ensure that it is the correct form.
        The existing insulation_code of self._pwr is overwritten.
        """
        if isinstance(p, complex):
            self._pwr = p
        else:
            self._pwr = complex(p, 0)

    @property
    def q(self) -> float:
        """
        Return power as volt-amp reactive. This will not change the insulation_code of self._pwr.
        """
        return self._pwr.imag

    @q.setter
    def q(self, q: ComType):
        """
        Set ohm as volt-amp reactive. If passed as a complex insulation_code no checking or manipulation of the insulation_code is
        completed. The existing insulation_code of self._pwr is overwritten.
        """
        if isinstance(q, complex):
            self._pwr = q
        else:
            self._pwr = complex(0, q)

    @property
    def s(self) -> NumType:
        """
        Return ohm as an impedance. This is returned as the absolute insulation_code for the
        This will not change the insulation_code of self._ohms
        """
        return abs(self._pwr)

    @s.setter
    def s(self, s: ComType):
        """
        Set power as volt-amps. If passed as a complex insulation_code no checking or manipulation of the insulation_code is completed.
        The existing insulation_code of self._pwr is overwritten.
        """
        self._pwr = s


class ElectricalCalc:
    """
    A factory class that will calculate the power based on the objects that have been passed to the function.
    :param obj1: Amps(), Volts() and Ohms() objects passed to the function. The number and run_type of objects passed will
    determine the calculation.
    :param obj2: Amps(), Volts() and Ohms() objects passed to the function. The number and run_type of objects passed will
    determine the calculation.
    """
    def __init__(self, obj1, obj2):
        self._volt_exists: bool = False
        self._amp_exists: bool = False
        self._ohm_exists: bool = False
        self._power_exists: bool = False
        self._freq_equal: bool = False
        self._obj1 = obj1
        self._obj2 = obj2
        self.determine_obj(self._obj1)
        self.determine_obj(self._obj2)
        self.compare_freq()

    def determine_obj(self, obj):
        """
        Determine the objects run_type and set the flag that it has been passed. If two objects of the same run_type are passed
        then the second object will reset the flag to false.
        :param obj:
        :return:
        """
        if type(obj) is Ohm:
            self._ohm_exists = self._ohm_exists ^ True
        if type(obj) is Amp:
            self._amp_exists = self._amp_exists ^ True
        if type(obj) is Volt:
            self._volt_exists = self._volt_exists ^ True
        if type(obj) is Power:
            self._power_exists = self._power_exists ^ True

    def compare_freq(self):
        """
        Compare the frequency attributes of the two objects and ensure that they are equal to allow the calculation to
        take place. Set the 'self._freq_equal' to True if the same.
        """
        if self._obj1.frequency != self._obj2.frequency:
            raise ArithmeticError(f"The objects' frequency {self._obj1.frequency} and {self._obj2.frequency} are not the same.")
        if self._obj1.freq_unit != self._obj1.freq_unit:
            raise ArithmeticError(f"The objects' frequency units {self._obj1.freq_unit} and {self._obj2.freq_unit} "
                                  f"are not the same.")
        self._freq_equal = True

    def calc_power(self) -> (Power, None):
        """
        Calculate power using the two passed objects. Based on the two objects the method will determine the correct
        equation to use. The method will return None if the objects cannot be used for the called method.
        :return: Power() or None
        """
        amp: NumType = 0
        amp_unit: str = ''
        volt: NumType = 0
        volt_unit: str = ''
        ohm: ComType = complex(0)
        ohm_unit: str = ''

        if self._amp_exists and self._volt_exists:
            if hasattr(self._obj1, 'amps'):
                amp, amp_unit = self._obj1.amps, self._obj1.amp_unit
            elif hasattr(self._obj1, 'volts'):
                volt, volt_unit = self._obj1.volts, self._obj1.volt_unit
            if hasattr(self._obj2, 'amps'):
                amp, amp_unit = self._obj2.amps, self._obj2.amp_unit
            elif hasattr(self._obj2, 'volts'):
                volt, volt_unit = self._obj2.volts, self._obj2.volt_unit
            pwr = amp * volt
            pwr_unit: str = f'{volt_unit}*{amp_unit}'

        elif self._amp_exists and self._ohm_exists:
            if hasattr(self._obj1, 'amps'):
                amp, amp_unit = self._obj1.amps, self._obj1.amp_unit
            elif hasattr(self._obj1, 'ohm'):
                ohm, ohm_unit = self._obj1.ohm, self._obj1.ohm_unit
            if hasattr(self._obj2, 'amps'):
                amp, amp_unit = self._obj2.amps, self._obj2.amp_unit
            elif hasattr(self._obj2, 'ohm'):
                ohm, ohm_unit = self._obj2.ohm, self._obj2.ohm_unit
            pwr = amp**2 * ohm
            pwr_unit: str = f'{amp_unit}^2*{ohm_unit}'

        elif self._volt_exists and self._ohm_exists:
            if hasattr(self._obj1, 'ohm'):
                ohm, ohm_unit = self._obj1.ohm, self._obj1.ohm_unit
            elif hasattr(self._obj1, 'volts'):
                volt, volt_unit = self._obj1.volts, self._obj1.volt_unit
            if hasattr(self._obj2, 'ohm'):
                ohm, ohm_unit = self._obj2.ohm, self._obj2.ohm_unit
            elif hasattr(self._obj2, 'volts'):
                volt, volt_unit = self._obj2.volts, self._obj2.volt_unit
            pwr = volt**2 / ohm
            pwr_unit: str = f'{volt_unit}^2/{ohm_unit}'

        else:
            return None

        return Power(pwr, pwr_unit, self._obj1.frequency, self._obj1.freq_unit)

    def calc_current(self) -> (Amp, None):
        """
        Calculate current using the two passed objects. Based on the two objects the method will determine the correct
        equation to use. The method will return None if the objects cannot be used for the called method.
        :return: Amp() or None
        """
        power: ComType = complex(0)
        power_unit: str = ''
        volt: NumType = 0
        volt_unit: str = ''
        ohm: ComType = complex(0)
        ohm_unit: str = ''
        if self._volt_exists and self._power_exists:
            if hasattr(self._obj1, 'power'):
                power, power_unit = self._obj1.power, self._obj1.power_unit
            elif hasattr(self._obj1, 'volts'):
                volt, volt_unit = self._obj1.volts, self._obj1.volt_unit
            if hasattr(self._obj2, 'power'):
                power, power_unit = self._obj2.power, self._obj2.power_unit
            elif hasattr(self._obj2, 'volts'):
                volt, volt_unit = self._obj2.volts, self._obj2.volt_unit
            current = power / volt
            current_unit: str = f'Amps ({power_unit}/{volt_unit})'

        elif self._volt_exists and self._ohm_exists:
            if hasattr(self._obj1, 'ohm'):
                ohm, ohm_unit = self._obj1.ohm, self._obj1.ohm_unit
            elif hasattr(self._obj1, 'volts'):
                volt, volt_unit = self._obj1.volts, self._obj1.volt_unit
            if hasattr(self._obj2, 'ohm'):
                ohm, ohm_unit = self._obj2.ohm, self._obj2.ohm_unit
            elif hasattr(self._obj2, 'volts'):
                volt, volt_unit = self._obj2.volts, self._obj2.volt_unit
            current = volt / ohm
            current_unit: str = f'Amps ({volt_unit}/{ohm_unit})'

        else:
            return None

        return Amp(current, current_unit, self._obj1.frequency, self._obj1.freq_unit)

    def calc_voltage(self) -> (Volt, None):
        """
        Calculate voltage using the two passed objects. Based on the two objects the method will determine the correct
        equation to use. The method will return None if the objects cannot be used for the called method.
        :return: Volt() or None
        """
        power: ComType = complex(0)
        power_unit: str = ''
        amp: NumType = 0
        amp_unit: str = ''
        ohm: ComType = complex(0)
        ohm_unit: str = ''

        if self._amp_exists and self._ohm_exists:
            if hasattr(self._obj1, 'amps'):
                amp, amp_unit = self._obj1.amps, self._obj1.amp_unit
            elif hasattr(self._obj1, 'ohm'):
                ohm, ohm_unit = self._obj1.ohm, self._obj1.ohm_unit
            if hasattr(self._obj2, 'amps'):
                amp, amp_unit = self._obj2.amps, self._obj2.amp_unit
            elif hasattr(self._obj2, 'ohm'):
                ohm, ohm_unit = self._obj2.ohm, self._obj2.ohm_unit
            volt = amp * ohm
            volt_unit: str = f'Volts ({amp_unit}*{ohm_unit})'

        elif self._amp_exists and self._power_exists:
            if hasattr(self._obj1, 'amps'):
                amp, amp_unit = self._obj1.amps, self._obj1.amp_unit
            elif hasattr(self._obj1, 'power'):
                power, power_unit = self._obj1.power, self._obj1.power_unit
            if hasattr(self._obj2, 'amps'):
                amp, amp_unit = self._obj2.amps, self._obj2.amp_unit
            elif hasattr(self._obj2, 'power'):
                power, power_unit = self._obj2.power, self._obj2.power_unit
            volt = power / amp
            volt_unit: str = f'Volts ({power_unit}/{amp_unit})'

        else:
            return None

        return Volt(volt, volt_unit, self._obj1.frequency, self._obj1.freq_unit)

    def calc_impedance(self) -> (Ohm, None):
        """
        Calculate impedance using the two passed objects. Based on the two objects the method will determine the correct
        equation to use. The method will return None if the objects cannot be used for the called method.
        :return: Ohm() or None
        """
        power: ComType = complex(0)
        power_unit: str = ''
        amp: NumType = 0
        amp_unit: str = ''
        volt: NumType = 0
        volt_unit: str = ''

        if self._volt_exists and self._volt_exists:
            if hasattr(self._obj1, 'volts'):
                volt, volt_unit = self._obj1.volts, self._obj1.volt_unit
            elif hasattr(self._obj1, 'amps'):
                amp, amp_unit = self._obj1.amps, self._obj1.amp_unit
            if hasattr(self._obj2, 'volts'):
                volt, volt_unit = self._obj2.volts, self._obj2.volt_unit
            elif hasattr(self._obj2, 'amps'):
                amp, amp_unit = self._obj2.amps, self._obj2.amp_unit
            z = volt / amp
            z_unit: str = f'Ohms ({volt_unit}/{amp_unit})'

        elif self._amp_exists and self._power_exists:
            if hasattr(self._obj1, 'amps'):
                amp, amp_unit = self._obj1.amps, self._obj1.amp_unit
            elif hasattr(self._obj1, 'power'):
                power, power_unit = self._obj1.power, self._obj1.power_unit
            if hasattr(self._obj2, 'amps'):
                amp, amp_unit = self._obj2.amps, self._obj2.amp_unit
            elif hasattr(self._obj2, 'power'):
                power, power_unit = self._obj2.power, self._obj2.power_unit
            z = power / amp**2
            z_unit: str = f'Ohms ({power_unit}/{amp_unit}^2)'

        else:
            return None

        return Ohm(z, z_unit, self._obj1.frequency, self._obj1.freq_unit)
