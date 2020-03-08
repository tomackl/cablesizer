import datetime
import decimal
import cmath
from typing import Tuple
#
class CableRunDefaultValues:
    """
    A class to store the default values for the cable run
    """
    def __init__(self):
        pass


class CableRun:
    """
    Base class for cable runs.
    """
    def __init__(self):
        """

        """
        # Set the context for the decimal object
        self.cables = []
        self.circuit_details
        self.conductor = ConductorDetail
        self.impedance = Impedance
        self.tag: str = ''
        self.length: float = 0.0
        self.description: str = ''
        self.load: str = ''
        self.notes: str = ''
        self.contracts = Contracts
        self.revision = RevisionDetail


class ConductorDetail:
    """
    A simple class to allow conductor characteristics to be defined/
    """
    def __init__(self, size: float = 0.0, size_unit: str = '', **kwargs):
        self.size = size
        self.size_unit = size_unit
        self.kwargs = kwargs

    @property
    def size(self) -> float:
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    @property
    def size_unit(self) -> str:
        return self._size_unit

    @size_unit.setter
    def size_unit(self, unit: str):
        self._size_unit = unit.upper()


class ConductorCableRun:
    def __init__(self, active_size: float = 0.0, active_unit: str = '', neutral_size: float = 0.0,
                 neutral_unit: str = '', earth_size: float = 0.0, earth_unit: str = ''):
        self._active = ConductorDetail(active_size, active_unit)
        self._neutral = ConductorDetail(neutral_size, neutral_unit)
        self._earth = ConductorDetail(earth_size, earth_unit)

    @property
    def active_size(self) -> float:
        return self._active.size

    @active_size.setter
    def active_size(self, size: float):
        self._active.size = size

    @property
    def active_size_unit(self) -> str:
        return self._active.size_unit

    @active_size_unit.setter
    def active_size_unit(self, unit: str):
        self._active.size_unit = unit.upper()

    @property
    def neutral_size(self) -> float:
        return self._neutral.size

    @neutral_size.setter
    def neutral_size(self, size: float):
        self._neutral.size = size

    @property
    def neutral_size_unit(self) -> str:
        return self._neutral.size_unit

    @neutral_size_unit.setter
    def neutral_size_unit(self, unit: str):
        self._neutral.size_unit = unit.upper()

    @property
    def earth_size(self) -> float:
        return self._earth.size

    @earth_size.setter
    def earth_size(self, size: float):
        self._earth.size = size

    @property
    def earth_size_unit(self) -> str:
        return self._earth.size_unit

    @earth_size_unit.setter
    def earth_size_unit(self, unit: str):
        self._earth.size_unit = unit.upper()


class RevisionDetail:
    def __init__(self, number: str = '', date: datetime.datetime = None):
        self.number = number
        self.date = date

    @property
    def number(self) -> str:
        return self._number

    @number.setter
    def number(self, value: str):
        self._number = value.upper()

    @property
    def date(self) -> [None, datetime.datetime]:
        return self._date

    @date.setter
    def date(self, date: [None, datetime.datetime]):
        if date is None:
            self._date = date
        else:
            self._date = date


class Impedance:
    def __init__(self, mvam: float = 0.0,
                 r: float = 0.0, r_unit: str = '',
                 x: float = 0.0, x_unit: str = '',
                 z: float = 0.0, z_unit: str = ''):
        self.mvam = mvam
        self._r = Vector()
        self._x = Vector()
        self._z = Vector()
        self.r = r
        self.r_unit = r_unit
        self.x = x
        self.x_unit = x_unit
        self.z = z
        self.z_unit = z_unit

    @property
    def mvam(self) -> float:
        return self._mvam

    @mvam.setter
    def mvam(self, value: float):
        self._mvam = value

    @property
    def r(self) -> float:
        return self._r.magnitude

    @r.setter
    def r(self, value: float):
        self._r.magnitude = value

    @property
    def r_unit(self) -> str:
        return self._r.unit

    @r_unit.setter
    def r_unit(self, unit: str):
        self._r.unit = unit.upper()

    @property
    def x(self) -> float:
        return self._x.magnitude

    @x.setter
    def x(self, value: float):
        self._x.magnitude = value

    @property
    def x_unit(self) -> str:
        return self._x.unit

    @x_unit.setter
    def x_unit(self, unit: str):
        self._x.unit = unit.upper()

    @property
    def z(self) -> float:
        return self._z.magnitude

    @z.setter
    def z(self, value: float):
        self._z.magnitude = value

    @property
    def z_unit(self) -> str:
        return self._z.unit.upper()

    @z_unit.setter
    def z_unit(self, unit: str):
        self._z.unit = unit

    def resistance(self) -> tuple:
        return self.r, self.r_unit

    def reactance(self) -> tuple:
        return self.x, self.x_unit

    def impedance(self) -> tuple:
        return self.z, self.z_unit


class Contracts:
    def __init__(self, supply: str = '', install: str = '', connect: str = ''):
        self.supply = supply
        self.install = install
        self.connect = connect

    @property
    def supply(self) -> str:
        return self._supply

    @supply.setter
    def supply(self, supplier: str):
        self._supply = supplier.upper()

    @property
    def install(self) -> str:
        return self._install

    @install.setter
    def install(self, installer: str):
        self._install = installer.upper()

    @property
    def connect(self) -> str:
        return self._connect

    @connect.setter
    def connect(self, connecter: str):
        self._connect = connecter.upper()


class Circuit:
    def __init__(self, circuit_type: str = '', voltage: int = 0, voltage_unit: str = '', frequency: int = 0,
                 frequency_unit: str = '', waveform: str = '', phases: int = 0, neutral_required: bool = True,
                 physical_method: str = '', cable_arrangement: str = '', ccc: int = 0, load_current: float = 0.0,
                 derating: float = 0.0, vd_max: float = 0.0, vd: float = 0.0):
        self.circuit_type = circuit_type
        self._voltage = Voltage()
        self.v = voltage
        self.v_unit = voltage_unit
        self.phases = phases
        self.neutral_required = neutral_required
        self._waveform = Frequency()
        self.frequency = frequency
        self.frequency_unit = frequency_unit
        self.waveform = waveform
        self._installation = Vector()
        self.physical_installation = physical_method
        self.cable_arrangement = cable_arrangement
        self._load_current = load_current

    @property
    def circuit_type(self) -> str:
        return self._type

    @circuit_type.setter
    def circuit_type(self, value: str):
        self._type = value.upper()

    @property
    def v(self) -> int:
        return self._voltage.magnitude

    @v.setter
    def v(self, value: int):
        self._voltage.magnitude = value

    @property
    def v_unit(self) -> str:
        return self._voltage.v_unit

    @v_unit.setter
    def v_unit(self, unit: str):
        self._voltage.v_unit = unit.upper()

    @property
    def phases(self):
        return self._voltage.phases

    @phases.setter
    def phases(self, phases):
        self._voltage.phases = phases

    @property
    def neutral_required(self) -> bool:
        return self._voltage.neutral_required

    @neutral_required.setter
    def neutral_required(self, neutral_req: bool):
        self._voltage.neutral_required = neutral_req

    @property
    def frequency(self) -> int:
        return self._waveform.freq

    @frequency.setter
    def frequency(self, value: int):
        self._waveform.freq = value

    @property
    def frequency_unit(self) -> str:
        return self._waveform.unit

    @frequency_unit.setter
    def frequency_unit(self, unit: str):
        self._waveform.unit = unit.upper()

    @property
    def waveform(self) -> str:
        return self._waveform.waveform

    @waveform.setter
    def waveform(self, value: str):
        self._waveform.waveform = value.upper()

    @property
    def physical_installation(self) -> str:
        return self._installation.unit

    @physical_installation.setter
    def physical_installation(self, value: str):
        self._installation.unit = value.upper()

    @property
    def cable_arrangement(self) -> str:
        return self._installation.magnitude

    @cable_arrangement.setter
    def cable_arrangement(self, value: str):
        self._installation.magnitude = value.upper()

    @property
    def load_current(self) -> float:
        return self._load_current

    @load_current.setter
    def load_current(self, amps: float):
        self._load_current = amps


class Vector:
    """
    A simple class to represent a magnitude, v_unit vector pair.
    """
    def __init__(self, magnitude=None, unit: str = ''):
        self.magnitude = magnitude
        self.unit = unit

    @property
    def magnitude(self):
        return self._scalar

    @magnitude.setter
    def magnitude(self, magnitude):
        self._scalar = magnitude

    @property
    def unit(self) -> str:
        return self._unit

    @unit.setter
    def unit(self, unit: str):
        self._unit = unit


class Frequency:
    """
    A simple class for freq details.
    """
    def __init__(self, freq: int = None, unit: str = '', waveform: str = ''):
        self.waveform: str = waveform
        self.freq: int = freq
        self.unit: str = unit

    @property
    def waveform(self) -> str:
        return self._wf

    @waveform.setter
    def waveform(self, wf: str):
        self._wf = wf.upper()

    @property
    def freq(self) -> int:
        return self._scalar

    @freq.setter
    def freq(self, freq: int):
        self._scalar = freq

    @property
    def unit(self) -> str:
        return self._unit

    @unit.setter
    def unit(self, unit: str):
        self._unit = unit.upper()


class Voltage:
    """
    A simple class for voltage details.
    """
    def __init__(self, volts: int = None, unit: str = '', phases: int = 0, neutral_required: bool = True):
        self.phases: str = phases
        self.v: int = volts
        self.v_unit: str = unit
        self.neutral_required: bool = neutral_required

    @property
    def phases(self) -> str:
        return self._phases

    @phases.setter
    def phases(self, phases: str):
        self._phases = phases

    @property
    def v(self) -> int:
        return self._volts

    @v.setter
    def v(self, v: int):
        self._volts = v

    @property
    def v_unit(self) -> str:
        return self._unit

    @v_unit.setter
    def v_unit(self, unit: str):
        self._unit = unit.upper()

    @property
    def neutral_required(self) -> bool:
        return self._neutral_req

    @neutral_required.setter
    def neutral_required(self, neutral: bool):
        self._neutral_req = neutral
