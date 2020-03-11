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
    def __init__(self, cable: list = [], tag: str = '', length: float = 0.0, description: str = '', supply: str = '',
                 load: str = '', notes: str = '', required_ccc: float = 0.0, derating_run: float = 1.0):
        """
        The base class for a cable run.
        :param cable: Instance of Cable() class that contains the cables that make up the cable run.
        :param tag: The cable run's tag.
        :param length: Length of the cable run.
        :param description: Description of the cable run.
        :param supply: The point of electrical supply for the cable run. The point of physical connection.
        :param load: The load being supplied via the cable run.
        :param notes: Any notes associated with the cable run.
        :param required_ccc: The required current carrying capacity of the cable run. This is load current derated to
        allow for installation conditions. The current carrying capacity of individual cables will be determined from
        this values and other installation factors.
        :param derating_run: The current carrying capacity derating factor to be applied to the cable run, based on
        installation conditions and other factors.
        """
        self.cables = Cable()
        self.circuit_details = Circuit()
        self.conductor = ConductorDetail()
        self.impedance = Impedance()
        self.tag: str = tag
        self.length: float = length
        self.description: str = description
        self.supply: str = supply
        self.load: str = load
        self.notes: str = notes
        self.contracts = Contracts()
        self.revision = RevisionDetail()
        self.required_ccc: float = required_ccc
        self.derate_run: float = derating_run

    def derate_ccc(self):
        """
        Calculate the required current carrying capacity for the cable run.
        """
        self.required_ccc = self.circuit_details.load_current / self.derate_run

    @property
    def required_ccc(self) -> float:
        return self._ccc

    @required_ccc.setter
    def required_ccc(self, ccc: float):
        if ccc < 0.0:
            raise ValueError(f"Current carrying capacity must be greater than 0.0.")
        self._ccc = ccc

    @property
    def derate_run(self) -> float:
        return self._derate_run

    @derate_run.setter
    def derate_run(self, value: float):
        if value < 0.0:
            raise ValueError(f"Derating value must be in the range 0.0 to 1.0")
        if value > 1.0:
            raise ValueError(f"Derating value must be in the range 0.0 to 1.0")
        self._derate_run = value


class CableSpec:
    """
    A class to store the cable requirements.
    """
    def __init__(self, run_type: str = '', max_parallel: int = 1, allow_parallel_multicore: bool = True,
                 shape: str = '', conductor_material: str = '', min_size: float = 0.0, core_arrangement: str = '',
                 sheath: str = '', insulation_material: str = '', insulation_code: str = '',
                 max_operating_temp: int = 0, armour: str = '', screen_cable: str = '', screen_core: str = '',
                 volt_rating: str = '', flexible: bool = False, vd_max: float = 0.0, vd: float = 0.0):
        """

        :param run_type: A description of the material of cable run
        :param max_parallel: The maximum number of cables that can be installed in parallel to meet the electrical
        requirements of the run.
        :param allow_parallel_multicore: Are multicore cables allowed to be installed in parallel.
        :param shape: Shape of the cable conductor.
        :param conductor_material: The conductor materials to be used.
        :param min_size: The minimum cross sectional size of the cables installed in the cable run.
        :param core_arrangement: The installation arrangement of single core cables.
        :param sheath: Cable sheath insulation_material.
        :param insulation_material: The cable insulation insulation_material.
        :param insulation_code: The cable insulation insulation_code.
        :param max_operating_temp: The maximum continuous conductor operating temperature.
        :param armour: Description of the cable armouring.
        :param screen_cable: Description of the cable's screen.
        :param screen_core: Description of the cable core's screen.
        :param volt_rating: Description of the cable's voltage rating.
        :param flexible: Is the cable flexible
        :param vd_max: The maximum allowable voltage drop, in volts, for the cable run.
        :param vd: The actual voltage drop, in volts, across the the cable run.
        """
        self.type: str = run_type
        self.max_parallel: int = max_parallel
        self.allow_parallel_multicore: bool = allow_parallel_multicore
        self.shape: str = shape
        self.conductor_material: str = conductor_material
        self.min_size: float = min_size
        self.core_arrangement: str = core_arrangement
        self.sheath: str = sheath
        self.insulation = Insulation()
        self.insulation_material: str = insulation_material
        self.insulation_code: str = insulation_code
        self.maximum_operating_temp: int = max_operating_temp
        self.armour: str = armour
        self.screen_cable: str = screen_cable
        self.screen_core: str = screen_core
        self.volt_rating: str = volt_rating
        self.flexible: bool = flexible
        self.vd_max: float = vd_max
        self.vd: float = vd

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str):
        self._type = value.upper()

    @property
    def max_parallel(self) -> int:
        return self._max_parallel

    @max_parallel.setter
    def max_parallel(self, value: int):
        if value < 1:
            raise ValueError(f"Value must be greater than 0.")
        self._max_parallel = value

    @property
    def allow_parallel_multicore(self) -> bool:
        return self._allow_parallel_multicore

    @allow_parallel_multicore.setter
    def allow_parallel_multicore(self, value: bool):
        self._allow_parallel_multicore = value

    @property
    def shape(self) -> str:
        return self._shape

    @shape.setter
    def shape(self, value: str):
        self._shape = value.upper()

    @property
    def conductor_material(self) -> str:
        return self._conductor_material

    @conductor_material.setter
    def conductor_material(self, value: str):
        self._conductor_material = value.upper()

    @property
    def min_size(self) -> float:
        return self._min_size

    @min_size.setter
    def min_size(self, value: float):
        if value < 0.0:
            raise ValueError(f"min_size needs to be a positive value.")
        self._min_size = value

    @property
    def core_arrangement(self) -> str:
        return self._core_arrangement

    @core_arrangement.setter
    def core_arrangement(self, value: str):
        self._core_arrangement = value.upper()

    @property
    def sheath(self) -> str:
        return self._sheath

    @sheath.setter
    def sheath(self, value: str):
        self._sheath = value.upper()

    @property
    def insulation_material(self) -> str:
        return self.insulation.material

    @insulation_material.setter
    def insulation_material(self, value):
        self.insulation.material = value.upper()

    @property
    def insulation_code(self) -> str:
        return self.insulation.code

    @insulation_code.setter
    def insulation_code(self, value: str):
        self.insulation.code = value.upper()

    @property
    def maximum_operating_temp(self) -> int:
        return self.insulation.max_temp

    @maximum_operating_temp.setter
    def maximum_operating_temp(self, value):
        self.insulation.max_temp = value

    @property
    def armour(self) -> str:
        return self._armour

    @armour.setter
    def armour(self, value: str):
        self._armour = value.upper()

    @property
    def screen_cable(self) -> str:
        return self._scn_cable

    @screen_cable.setter
    def screen_cable(self, value: str):
        self._scn_cable = value.upper()

    @property
    def screen_core(self) -> str:
        return self._scn_core

    @screen_core.setter
    def screen_core(self, value: str):
        self._scn_core = value.upper()

    @property
    def volt_rating(self) -> str:
        return self._volt_rating

    @volt_rating.setter
    def volt_rating(self, value: str):
        self._volt_rating = value.upper()

    @property
    def flexible(self) -> bool:
        return self._flex

    @flexible.setter
    def flexible(self, value: bool):
        self._flex = value

    @property
    def vd_max(self) -> float:
        return self._vd_max

    @vd_max.setter
    def vd_max(self, value: float):
        if value < 0.0:
            raise ValueError(f"vd_max must be positive number.")
        self._vd_max = value

    @property
    def vd(self) -> float:
        return self._vd

    @vd.setter
    def vd(self, value: float):
        if value < 0.0:
            raise ValueError(f"vd_max must be positive number.")
        self._vd = value


class Cable:
    def __init__(self, cable_type: str = "", core_arrangement: str = "", cable_shape: str = "",
                 conductor_material: str = "", cross_sectional_area: int = 0, cable_sheath: str = "",
                 insulation_material: str = "", insulation_code: str = "", max_conductor_temp: int = 0):
        self.type = cable_type
        self.core_arrangement = core_arrangement
        self.shape = cable_shape
        self.conductor_material = conductor_material
        self.cross_sectional_area = cross_sectional_area
        self.sheath = cable_sheath
        self.insulation = Insulation()
        self.insulation.material = insulation_material
        self.insulation.code = insulation_code
        self.insulation.max_temp = max_conductor_temp

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str):
        self._type = value.upper()

    @property
    def core_arrangement(self) -> str:
        return self._c_arrangement

    @core_arrangement.setter
    def core_arrangement(self, value: str):
        self._c_arrangement = value.upper()

    @property
    def shape(self) -> str:
        return self._shape

    @shape.setter
    def shape(self, value):
        self._shape = value.upper()

    @property
    def conductor_material(self) -> str:
        return self._c_material

    @conductor_material.setter
    def conductor_material(self, value):
        self._c_material = value.upper()

    @property
    def cross_sectional_area(self) -> int:
        return self._csa

    @cross_sectional_area.setter
    def cross_sectional_area(self, value):
        if value < 0:
            raise ValueError(f"The value must be greater than 0.")
        self._csa = value

    @property
    def sheath(self) -> str:
        return self._sheath

    @sheath.setter
    def sheath(self, value: str):
        self._sheath = value.upper()


class ConductorDetail:
    """
    A simple class to allow conductor characteristics to be defined.
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
        """
        :param mvam: Milli-volts per amp metre
        :param r: Resistance magnitude.
        :param r_unit: Resistance units.
        :param x: Reactance magnitude.
        :param x_unit: Reactance units.
        :param z: Impedance magnitude.
        :param z_unit: Impedance units.
        """
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


class Insulation:
    def __init__(self, insulation_material: str = "", insulation_code: str = '', max_temp: int = 0):
        """
        :param insulation_material: The cable's insulation material.
        :param insulation_code: The insulation code.
        :param max_temp: The maximum continuous operating temperature of the cable conductor.
        """
        self.material = insulation_material
        self.code: str = insulation_code
        self.max_temp: int = max_temp

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        self._material = value.upper()

    @property
    def code(self) -> str:
        return self._code

    @code.setter
    def code(self, code: str):
        self._code = code.upper()

    @property
    def max_temp(self) -> int:
        return self._max_temp

    @max_temp.setter
    def max_temp(self, temp: int):
        if temp < 0:
            raise ValueError(f"Value must be a value greater than 0.")
        self._max_temp = temp


class Contracts:
    def __init__(self, supply: str = '', install: str = '', connect: str = ''):
        """
        :param supply:
        :param install:
        :param connect:
        """
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
                 physical_method: str = '', cable_arrangement: str = '', load_current: float = 0.0):
        """
        :param circuit_type:
        :param voltage:
        :param voltage_unit:
        :param frequency:
        :param frequency_unit:
        :param waveform:
        :param phases:
        :param neutral_required:
        :param physical_method:
        :param cable_arrangement:
        :param load_current:
        """
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
        return self._voltage.v

    @v.setter
    def v(self, value: int):
        self._voltage.v = value

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

