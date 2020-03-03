import datetime
import decimal
import cmath
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
    def __init__(self, mvam: float = 0.0, r_ohms: float = 0.0, x_ohms: float = 0.0, z_ohms: float = 0.0):
        self.mvam = mvam
        self.r = r_ohms
        self.x = x_ohms
        self.z = z_ohms

    @property
    def mvam(self) -> float:
        return self._mvam

    @mvam.setter
    def mvam(self, value: float):
        self._mvam = value

    @property
    def r(self) -> float:
        return self._r

    @r.setter
    def r(self, value: float):
        self._r = value

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value: float):
        self._x = value

    @property
    def z(self) -> float:
        return self._z

    @z.setter
    def z(self, value: float):
        self._z = value


class Contracts:
    def __init__(self):
        self.supply: str = ''
        self.install: str = ''
        self.connect: str = ''


class Circuit:
    def __init__(self):
        self.voltage: int = 0
        self.phases: int = 0
        self.ccc: int = 0
        self.load_current: float = 0.0
        self.derating: float = 0.0
        self.installation_method: str = ''
        self.requires_neutral: bool = True
        self.vd_max: float = 0.0
        self.vd: float = 0.0


