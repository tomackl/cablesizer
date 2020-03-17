import datetime
import decimal
import cmath
from typing import Tuple, List
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
    def __init__(self, cable_type: str = "", active_size: float = 0.0, active_number: int = 0,
                 active_unit: str = "", active_name: str = "", neutral_size: float = 0.0, neutral_number: int = 0,
                 neutral_unit: str = "", neutral_name: str = "", earth_size: float = 0.0, earth_number: int = 0,
                 earth_unit: str = "", earth_name: str = "", instrument_size: float = 0.0,
                 instrument_number: int = 0, instrument_unit: str = "", instrument_name: str = "",
                 control_size: float = 0.0, control_number: int = 0, control_unit: str = "", control_name: str = "",
                 communication_size: float = 0.0, communication_number: int = 0, communication_unit: str = "",
                 communication_name: str = "", data_size: float = 0.0, data_number: int = 0, data_unit: str = "",
                 data_name: str = "", core_arrangement: str = "", cable_shape: str = "",
                 conductor_material: str = "", cross_sectional_area: int = 0, cable_sheath: str = "",
                 insulation_material: str = "", insulation_code: str = "", max_conductor_temp: int = 0,
                 ccc: float = 0.0, circuit_type: str = "", volt_rating: str = "", armour: [None, str] = None,
                 description: str = "", flexible: bool = False):
        self.type: str = cable_type
        self.activeCores = CoreDetails()
        self.activeCores.size = active_size
        self.activeCores.unit = active_unit
        self.activeCores.number = active_number
        self.activeCores.name = active_name
        self.neutralCores = CoreDetails()
        self.neutralCores.size = neutral_size
        self.neutralCores.unit = neutral_unit
        self.neutralCores.number = neutral_number
        self.neutralCores.name = neutral_name
        self.earthCores = CoreDetails()
        self.earthCores.size = earth_size
        self.earthCores.unit = earth_unit
        self.earthCores.number = earth_number
        self.earthCores.name = earth_name
        self.controlCores = CoreDetails()
        self.controlCores.size = control_size
        self.controlCores.unit = control_unit
        self.controlCores.number = control_number
        self.controlCores.name = control_name
        self.instrumentCores = CoreDetails()
        self.instrumentCores.size = instrument_size
        self.instrumentCores.unit = instrument_unit
        self.instrumentCores.number = instrument_number
        self.instrumentCores.name = instrument_name
        self.communicationCores = CoreDetails()
        self.communicationCores.size = communication_size
        self.communicationCores.unit = communication_unit
        self.communicationCores.number = communication_number
        self.communicationCores.name = communication_name
        self.dataCores = CoreDetails()
        self.dataCores.size = data_size
        self.dataCores.unit = data_unit
        self.dataCores.number = data_number
        self.dataCores.name = data_name
        self.installMethod = CableInstallationMethod()
        self.impedance = Impedance()
        self.cableScreen = Screen()
        self.coreScreen = Screen()
        self.insulation = Insulation()
        self.insulation.material = insulation_material
        self.insulation.code = insulation_code
        self.sheath = cable_sheath
        self.voltage_rating: str = volt_rating
        self.flexible: bool = flexible
        self.armour: [None, bool] = armour
        self.rev = RevisionDetail()
        self.description = description
        self.circuit_type = circuit_type
        self.conductor_material = conductor_material
        self.core_arrangement = core_arrangement
        self.shape = cable_shape
        self.cross_sectional_area = cross_sectional_area
        self.insulation.max_temp = max_conductor_temp
        self.ccc: float = ccc

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

    def find_ccc(self):
        pass

    def find_mvam(self):
        pass

    def has_active(self):
        if self.active_cores.number > 0:
            return True
        else:
            False

    def has_neutral(self):
        if self.neutral_cores.number > 0:
            return True
        else:
            False

    def has_earth(self):
        if self.earth_cores.number > 0:
            return True
        else:
            False

    @property
    def ccc(self) -> float:
        return self._ccc

    @ccc.setter
    def ccc(self, value: float):
        if value < 0:
            raise ValueError(f"value must be greater than 0.")
        else:
            self._ccc = value


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
    def __init__(self, insulation_material: str = "", insulation_code: str = '', op_temp: int = 0, max_temp: int = 0):
        """
        :param insulation_material: The cable's insulation material.
        :param insulation_code: The insulation code.
        :param max_temp: The maximum continuous operating temperature of the cable conductor.
        """
        self.material = insulation_material
        self.code: str = insulation_code
        self.op_temp: int = op_temp
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
    def op_temp(self) -> int:
        return self._op_temp

    @op_temp.setter
    def op_temp(self, temp: int):
        if temp < 0:
            raise ValueError(f"Value must be a value greater than 0.")
        self._op_temp = temp

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
        return self._voltage.unit

    @v_unit.setter
    def v_unit(self, unit: str):
        self._voltage.unit = unit.upper()

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
        return self._waveform.frequency

    @frequency.setter
    def frequency(self, value: int):
        self._waveform.frequency = value

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
    A simple class to represent a magnitude, unit vector pair.
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
        self._unit = unit.upper()

    def to_dict(self):
        x = dict()
        x["magnitude"] = self.magnitude
        x["unit"] = self.unit
        return x


class Frequency:
    """
    A simple class for frequency details.
    """
    def __init__(self, freq: int = None, unit: str = '', waveform: str = ''):
        self.waveform: str = waveform
        self.frequency: int = freq
        self.unit: str = unit

    @property
    def waveform(self) -> str:
        return self._wf

    @waveform.setter
    def waveform(self, wf: str):
        self._wf = wf.upper()

    @property
    def frequency(self) -> int:
        return self._scalar

    @frequency.setter
    def frequency(self, freq: int):
        self._scalar = freq

    @property
    def unit(self) -> str:
        return self._unit

    @unit.setter
    def unit(self, unit: str):
        self._unit = unit.upper()

    def to_dict(self) -> dict:
        x = dict()
        x["waveform"] = self.waveform
        x["frequency"] = self.frequency
        x["unit"] = self.unit
        return x


class Voltage:
    """
    A simple class for voltage details.
    """
    def __init__(self, volts: int = None, unit: str = '', phases: int = 0, neutral_required: bool = True):
        self.phases: str = phases
        self.v: int = volts
        self.unit: str = unit
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
    def unit(self) -> str:
        return self._unit

    @unit.setter
    def unit(self, unit: str):
        self._unit = unit.upper()

    @property
    def neutral_required(self) -> bool:
        return self._neutral_req

    @neutral_required.setter
    def neutral_required(self, neutral: bool):
        self._neutral_req = neutral

    def to_dict(self) -> dict:
        x = dict()
        x["phases"] = self.phases
        x["v"] = self.v
        x["unit"] = self.unit
        x["neutral_required"] = self.neutral_required
        return x


class CoreDetails:
    def __init__(self, csa: float = 0, csa_unit: str = "", number: int = 0, name: str = ""):
        """
        This class defines and checks the details of a cable core.
        :param csa: Cross sectional area of the main conductors
        :param csa_unit: The cross-sectional area unit of measurement.
        :param number: The number of cable cores including earth and neutrals.
        :param name: Description of the cable cores.
        """
        self.size: float = csa
        self.unit: str = csa_unit
        self.number: int = number
        self.name: str = name

    @property
    def size(self) -> float:
        return self._csa

    @size.setter
    def size(self, value: float):
        self._csa = value

    @property
    def unit(self) -> str:
        return self._csa_unit

    @unit.setter
    def unit(self, value: str):
        self._csa_unit = value.upper()

    @property
    def number(self) -> int:
        return self._number

    @number.setter
    def number(self, value: int):
        self._number = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value.upper()

    def to_dict(self) -> dict:
        """
        Convert the class to a dictionary.
        :return:
        """
        # todo: add to test
        x = dict()
        x["size"] = self.size
        x["unit"] = self.unit
        x["number"] = self.number
        x["name"] = self.name
        return x


class CableInstallationMethod:
    def __init__(self, name: str = "", ccc: int = 0, install_temp: int = 0, cable_arrangement: str = ""):
        """
        This class defines and checks the details of the cable installation details.
        :param name: The installation method.
        :param ccc: Current carrying capacity  of the cable cable.
        :param install_temp: The ambient temperature for the operational environment.
        :param cable_arrangement: The arrangement of the cable cores. Single core cables only.
        """
        self.name: str = name
        self.ccc: int = ccc
        self.install_temp: int = install_temp
        self.cable_arrangement: str = cable_arrangement

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value.upper()

    @property
    def ccc(self) -> int:
        return self._ccc

    @ccc.setter
    def ccc(self, value: int):
        self._ccc = value

    @property
    def install_temp(self) -> int:
        return self._install_temp

    @install_temp.setter
    def install_temp(self, value: int):
        self._install_temp = value

    @property
    def cable_arrangement(self) -> str:
        return self._cable_arrangement

    @cable_arrangement.setter
    def cable_arrangement(self, value: str):
        self._cable_arrangement = value.upper()

    def convert_to_dict(self) -> dict:
        """
        Convert the class to a dictionary.
        :return:
        """
        # todo: add to test
        x = dict()
        x["name"] = self.name
        x["ccc"] = self.ccc
        x["install_temp"] = self.install_temp
        x["cable_arrangement"] = self.cable_arrangement
        return x


class Screen:
    def __init__(self, name: str = "", fault_withstand: int = 0):
        self.name: str = name
        self.fault_withstand: int = fault_withstand

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value.upper()

    @property
    def fault_withstand(self):
        return self._fault_withstand

    @fault_withstand.setter
    def fault_withstand(self, value: int):
        self._fault_withstand = value


class Manufacturer:
    def __init__(self, name: str = "", part_number: str = ""):
        self.name: str = name
        self.part_number: str = part_number

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value.upper()

    @property
    def part_number(self) -> str:
        return self._number

    @part_number.setter
    def part_number(self, value: str):
        self._number = value.upper()


class I2T:
    def __init__(self, k_factor: int = 0, amp_time: List[Tuple[int]] = None):
        self.k_factor: int = k_factor
        self._amp_time = []
        self.amp_time: list = amp_time
        # self.current: list = current

    @property
    def k_factor(self) -> int:
        return self._kfactor

    @k_factor.setter
    def k_factor(self, value: int):
        self._kfactor = value

    @property
    def amp_time(self) -> List[Tuple[int]]:
        return self._amp_time

    @amp_time.setter
    def amp_time(self, value: (Tuple[int])):
        if value is None:
            pass
        else:
            self._amp_time.append(value)
