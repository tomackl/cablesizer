import datetime
from typing import Tuple, List, Union


class CableRun:
    """
    Base class for cable_list runs.
    """
    def __init__(self, cable_list=None, tag: str = '', length: float = 0.0, description: str = '',
                 supply: str = '', load: str = '', notes: str = '', required_ccc: float = 0.0,
                 derating_run: float = 1.0):
        """
        The base class for a cable run.
        :param cable_list: Instance of Cable() class that contains the cables that make up the cable run.
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
        if cable_list is None:
            cable_list = []
        self.cables: list = []
        self.add_cable(cable_list)
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

    def to_dict(self):
        return {
            "cables": self.cables,
            "circuit_details": self.circuit_details,
            "conductor": self.conductor,
            "impedance": self.impedance,
            "tag": self.tag,
            "length": self.length,
            "description": self.description,
            "supply": self.supply,
            "load": self.load,
            "notes": self.notes,
            "contracts": self.contracts,
            "revision": self.revision,
            "derate_run": self.derate_run,
        }

    def from_dict(self, cable: dict):
        self.cables = cable["cables"]
        self.circuit_details.from_dict(cable["circuit_details"])
        self.conductor.from_dict(cable["conductor"])
        self.impedance.from_dict(cable["impedance"])
        self.tag = cable["tag"] = self.tag
        self.length = cable["length"]
        self.description = cable["description"]
        self.supply = cable["supply"]
        self.load = cable["load"]
        self.notes = cable["notes"]
        self.contracts.from_dict(cable["contracts"])
        self.revision.from_dict(cable["revision"])
        self.derate_run = cable["derate_run"]

    def add_cable(self, cable):
        self.cables.append(cable)

    def derate_ccc(self):
        """
        Calculate the required current carrying capacity for the cable_list run.
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

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str):
        self._description = value


class CableSpec:
    """
    A class to store the cable_list requirements. This class is intended to define the specification criteria used to
    select cables.
    """
    def __init__(self, run_type: str = "", max_parallel: int = 1, allow_parallel_multicore: bool = True,
                 shape: str = "", conductor_material: str = "", min_size: float = 0.0, core_arrangement: str = "",
                 sheath: str = "", insulation_material: str = "", insulation_code: str = "", operating_temp: int = 0,
                 max_operating_temp: int = 0, armour: str = "", screen_cable: str = "", screen_core: str = "",
                 volt_rating: str = "", flexible: bool = False, vd_max: float = 0.0, vd: float = 0.0):
        """

        :param run_type: A description of the material of cable_list run
        :param max_parallel: The maximum number of cables that can be installed in parallel to meet the electrical
        requirements of the run.
        :param allow_parallel_multicore: Are multicore cables allowed to be installed in parallel.
        :param shape: Shape of the cable_list conductor.
        :param conductor_material: The conductor materials to be used.
        :param min_size: The minimum cross sectional size of the cables installed in the cable_list run.
        :param core_arrangement: The installation arrangement of single core cables.
        :param sheath: Cable sheath insulation_material.
        :param insulation_material: The cable_list insulation insulation_material.
        :param insulation_code: The cable_list insulation insulation_code.
        :param operating_temp: The operating temperature of the cable under a constant steady load.
        :param max_operating_temp: The maximum continuous conductor operating temperature.
        :param armour: Description of the cable_list armouring.
        :param screen_cable: Description of the cable_list's screen.
        :param screen_core: Description of the cable_list core's screen.
        :param volt_rating: Description of the cable_list's voltage rating.
        :param flexible: Is the cable_list flexible
        :param vd_max: The maximum allowable voltage drop, in volts, for the cable_list run.
        :param vd: The actual voltage drop, in volts, across the the cable_list run.
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
        self.operating_temp: int = operating_temp
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
    def operating_temp(self) -> int:
        return self.insulation.op_temp

    @operating_temp.setter
    def operating_temp(self, value):
        self.insulation.op_temp = value

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
    def vd(self, value: [int, float]):
        if value < 0.0:
            raise ValueError(f"vd_max must be positive number.")
        self._vd = value

    def to_dict(self) -> dict:
        return {"cable_type": self.type,
                "max_parallel": self.max_parallel,
                "allow_parallel_multicore": self.allow_parallel_multicore,
                "shape": self.shape,
                "conductor_material": self.conductor_material,
                "min_size": self.min_size,
                "core_arrangement": self.core_arrangement,
                "sheath": self.sheath,
                "insulation_material": self.insulation_material,
                "insulation_code": self.insulation_code,
                "operating_temp": self.operating_temp,
                "maximum_operating_temp": self.maximum_operating_temp,
                "armour": self.armour,
                "screen_cable": self.screen_cable,
                "screen_core": self.screen_core,
                "volt_rating": self.volt_rating,
                "flexible": self.flexible,
                "vd_max": self.vd_max,
                "vd": self.vd,
                }

    def from_dict(self, details: dict):
        self.type = details["cable_type"]
        self.max_parallel = details["max_parallel"]
        self.allow_parallel_multicore = details["allow_parallel_multicore"]
        self.shape = details["shape"]
        self.conductor_material = details["conductor_material"]
        self.min_size = details["min_size"]
        self.core_arrangement = details["core_arrangement"]
        self.sheath = details["sheath"]
        self.insulation_material = details["insulation_material"]
        self.insulation_code = details["insulation_code"]
        self.operating_temp = details["operating_temp"]
        self.maximum_operating_temp = details["maximum_operating_temp"]
        self.armour = details["armour"]
        self.screen_cable = details["screen_cable"]
        self.screen_core = details["screen_core"]
        self.volt_rating = details["volt_rating"]
        self.flexible = details["flexible"]
        self.vd_max = details["vd_max"]
        self.vd = details["vd"]


class Cable:
    def __init__(self, cable_type: str = "", active_size: float = 0.0, active_number: int = 0,
                 active_unit: str = "", active_name: str = "", neutral_size: float = 0.0, neutral_number: int = 0,
                 neutral_unit: str = "", neutral_name: str = "", earth_size: float = 0.0, earth_number: int = 0,
                 earth_unit: str = "", earth_name: str = "", instrument_size: float = 0.0,
                 instrument_number: int = 0, instrument_unit: str = "", instrument_name: str = "",
                 control_size: float = 0.0, control_number: int = 0, control_unit: str = "", control_name: str = "",
                 communication_size: float = 0.0, communication_number: int = 0, communication_unit: str = "",
                 communication_name: str = "", data_size: float = 0.0, data_number: int = 0, data_unit: str = "",
                 data_name: str = "", unenclosed_spaced_ccc: int = 0, unenclosed_spaced_install_temp: int = 0,
                 unenclosed_spaced_arrangement: str = "", unenclosed_surface_ccc: int = 0,
                 unenclosed_surface_install_temp: int = 0, unenclosed_surface_arrangement: str = "",
                 unenclosed_touching_ccc: int = 0, unenclosed_touching_install_temp: int = 0,
                 unenclosed_touching_arrangement: str = "", enclosed_conduit_ccc: int = 0,
                 enclosed_conduit_install_temp: int = 0, enclosed_conduit_arrangement: str = "",
                 enclosed_partial_ccc: int = 0, enclosed_partial_install_temp: int = 0,
                 enclosed_partial_arrangement: str = "", enclosed_complete_ccc: int = 0,
                 enclosed_complete_install_temp: int = 0, enclosed_complete_arrangement: str = "",
                 buried_direct_ccc: int = 0, buried_direct_install_temp: int = 0, buried_direct_arrangement: str = "",
                 ducts_single_ccc: int = 0, ducts_single_install_temp: int = 0, ducts_single_arrangement: str = "",
                 ducts_per_cable_ccc: int = 0, ducts_per_cable_install_temp: int = 0,
                 ducts_per_cable_arrangement: str = "", mvam: float = 0.0, r: float = 0.0, r_unit: str = "",
                 x: float = 0.0, x_unit: str = "", z: float = 0.0, z_unit: str = "", cable_screen_type: str = "",
                 cable_screen_withstand: int = 0, core_screen_type: str = "", core_screen_withstand: int = 0,
                 insulation_material: str = "", insulation_code: str = "", cont_conductor_temp: int = 0,
                 max_conductor_temp: int = 0, cable_sheath: str = "", volt_rating: str = "", flexible: bool = False,
                 armour: [None, str] = None, rev_number: str = "", rev_date: datetime = None, description: str = "",
                 core_arrangement: str = "", cable_shape: str = "", conductor_material: str = "",
                 circuit_type: str = ""
                 ):
        """
        :param cable_type:
        :param active_size: Cross sectional area of the active conductor(s). All active conductors are assumed to be
        the same size.
        :param active_number: The number of active cores.
        :param active_unit: The key of measurement associate with active_size.
        :param active_name: The type of earth core.
        :param neutral_size: Cross sectional area of the neutral conductor(s). All active conductors are assumed to be
        the same size.
        :param neutral_number: The number of neutral cores.
        :param neutral_unit: The key of measurement associate with neutral_size.
        :param neutral_name: The type of earth core
        :param earth_size: Cross sectional area of the earth conductor(s). All active conductors are assumed to be the
        same size.
        :param earth_number: The number of earth cores.
        :param earth_unit: The key of measurement associate with earth_size.
        :param earth_name: The type of earth core.
        :param instrument_size: Cross sectional area of the instrumentation conductor(s). All active conductors are
        assumed to be the same size.
        :param instrument_number: The number of instrumentation cores.
        :param instrument_unit: The key of measurement associate with instrument_size.
        :param instrument_name: The type of instrument core.
        :param control_size: Cross sectional area of the control conductor(s). All active conductors are assumed to be
        the same size.
        :param control_number: The number of control cores.
        :param control_unit: The key of measurement associate with control_size.
        :param control_name: The type of control core.
        :param communication_size: Cross sectional area of the communication conductor(s). All active conductors are
        assumed to be the same size.
        :param communication_number: The number of communication cores.
        :param communication_unit: The key of measurement associate with communication_size.
        :param communication_name: The type of communication core.
        :param data_size: The number of data cores.
        :param data_number: Cross sectional area of the data conductor(s). All active conductors are assumed to be the
        same size.
        :param data_unit: The key of measurement associate with data_size.
        :param data_name: The type of data core.
        :param unenclosed_spaced_ccc: The current carrying capacity for the cable based on this installation
        methodology.
        :param unenclosed_spaced_install_temp: The ambient temperature associated with the cable installation CCC.
        :param unenclosed_spaced_arrangement: The single core cable_list arrangement associated with this installation
        method.
        :param unenclosed_surface_ccc: The current carrying capacity for the cable based on this installation
        methodology.
        :param unenclosed_surface_install_temp: The ambient temperature associated with the cable installation CCC.
        :param unenclosed_surface_arrangement: The single core cable_list arrangement associated with this installation
        method.
        :param unenclosed_touching_ccc: The current carrying capacity for the cable based on this installation
        methodology.
        :param unenclosed_touching_install_temp: The ambient temperature associated with the cable installation CCC.
        :param unenclosed_touching_arrangement: The single core cable_list arrangement associated with this installation
        method.
        :param enclosed_conduit_ccc: The current carrying capacity for the cable based on this installation methodology.
        :param enclosed_conduit_install_temp: The ambient temperature associated with the cable installation CCC.
        :param enclosed_conduit_arrangement: The single core cable_list arrangement associated with this installation
        method.
        :param enclosed_partial_ccc: The current carrying capacity for the cable based on this installation methodology.
        :param enclosed_partial_install_temp: The ambient temperature associated with the cable installation CCC.
        :param enclosed_partial_arrangement: The single core cable_list arrangement associated with this installation
        method.
        :param enclosed_complete_ccc: The current carrying capacity for the cable based on this installation
        methodology.
        :param enclosed_complete_install_temp: The ambient temperature associated with the cable installation CCC.
        :param enclosed_complete_arrangement: The single core cable_list arrangement associated with this installation
        method.
        :param buried_direct_ccc: The current carrying capacity for the cable based on this installation methodology.
        :param buried_direct_install_temp: The ambient temperature associated with the cable installation CCC.
        :param buried_direct_arrangement: The single core cable_list arrangement associated with this installation
        method.
        :param ducts_single_ccc: The current carrying capacity for the cable based on this installation methodology.
        :param ducts_single_install_temp: The ambient temperature associated with the cable installation CCC.
        :param ducts_single_arrangement: The single core cable_list arrangement associated with this installation
        method.
        :param ducts_per_cable_ccc: The current carrying capacity for the cable based on this installation methodology.
        :param ducts_per_cable_install_temp: The ambient temperature associated with the cable installation CCC.
        :param ducts_per_cable_arrangement: The single core cable_list arrangement associated with this installation
        method.
        :param mvam: Milli-volt per amp-metre resistance value.
        :param r: Resistance value for the cable_list.
        :param r_unit: Resistance value key.
        :param x: Reactance value for the cable_list.
        :param x_unit: Reactance value key.
        :param z: Impedance value for the cable_list.
        :param z_unit: Impedance value key.
        :param cable_screen_type:
        :param cable_screen_withstand:
        :param core_screen_type:
        :param core_screen_withstand:
        :param insulation_material:
        :param insulation_code:
        :param cont_conductor_temp:
        :param max_conductor_temp:
        :param cable_sheath:
        :param volt_rating:
        :param flexible:
        :param armour:
        :param rev_number:
        :param rev_date:
        :param description:
        :param core_arrangement:
        :param cable_shape:
        :param conductor_material:
        :param circuit_type:
        """
        self.cable_type: str = cable_type
        self.activeCores = CoreDetails(active_size, active_unit, active_number, active_name)
        self.neutralCores = CoreDetails(neutral_size, neutral_unit, neutral_number, neutral_name)
        self.earthCores = CoreDetails(earth_size, earth_unit, earth_number, earth_name)
        self.controlCores = CoreDetails(control_size, control_unit, control_number, control_name)
        self.instrumentCores = CoreDetails(instrument_size, instrument_unit, instrument_number, instrument_name)
        self.communicationCores = CoreDetails(communication_size, communication_unit, communication_number,
                                              communication_name)
        self.dataCores = CoreDetails(data_size, data_unit, data_number, data_name)
        self.impedance = Impedance(mvam, r, r_unit, x, x_unit, z, z_unit)
        self.cableScreen = Screen(cable_screen_type, cable_screen_withstand)
        self.coreScreen = Screen(core_screen_type, core_screen_withstand)
        self.insulation = Insulation(insulation_material, insulation_code, cont_conductor_temp, max_conductor_temp)
        self.unenclosedSpaced = CableInstallationMethod(unenclosed_spaced_ccc, unenclosed_spaced_install_temp,
                                                        unenclosed_spaced_arrangement)
        self.unenclosedSurface = CableInstallationMethod(unenclosed_surface_ccc, unenclosed_surface_install_temp,
                                                         unenclosed_surface_arrangement)
        self.unenclosedTouching = CableInstallationMethod(unenclosed_touching_ccc, unenclosed_touching_install_temp,
                                                          unenclosed_touching_arrangement)
        self.enclosedConduit = CableInstallationMethod(enclosed_conduit_ccc, enclosed_conduit_install_temp,
                                                       enclosed_conduit_arrangement,)
        self.enclosedPartial = CableInstallationMethod(enclosed_partial_ccc, enclosed_partial_install_temp,
                                                       enclosed_partial_arrangement)
        self.enclosedComplete = CableInstallationMethod(enclosed_complete_ccc, enclosed_complete_install_temp,
                                                        enclosed_complete_arrangement)
        self.buriedDirect = CableInstallationMethod(buried_direct_ccc, buried_direct_install_temp,
                                                    buried_direct_arrangement)
        self.ductsSingle = CableInstallationMethod(ducts_single_ccc, ducts_single_install_temp,
                                                   ducts_single_arrangement)
        self.ductsPerCable = CableInstallationMethod(ducts_per_cable_ccc, ducts_per_cable_install_temp,
                                                     ducts_per_cable_arrangement)
        self.sheath = cable_sheath
        self.voltage_rating: str = volt_rating
        self.flexible: bool = flexible
        self.armour: [None, bool] = armour
        self.revision = RevisionDetail(rev_number, rev_date)
        self.description = description
        self.circuit_type = circuit_type
        self.conductor_material = conductor_material
        self.core_arrangement = core_arrangement
        self.shape = cable_shape

    @property
    def cable_type(self) -> str:
        return self._cable_type

    @cable_type.setter
    def cable_type(self, value: str):
        self._cable_type = value.upper()

    @property
    def circuit_type(self) -> str:
        return self._circuit_type

    @circuit_type.setter
    def circuit_type(self, value: str):
        self._circuit_type = value.upper()

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
    def sheath(self) -> str:
        return self._sheath

    @sheath.setter
    def sheath(self, value: str):
        self._sheath = value.upper()

    @property
    def csa(self) -> dict:
        """
        A simple getter for the CSA of each conductor in the cable. THERE IS NO SIMILAR GETTER PROPERTY FOR
        CROSS-SECTIONAL AREA.
        :return: dict containing the CSA details
        """
        return {"POWER": self.activeCores.size,
                "NEUTRAL": self.neutralCores.size,
                "EARTH": self.earthCores.size,
                "CONTROL": self.controlCores.size,
                "INSTRUMENT": self.instrumentCores.size,
                "DATA": self.dataCores.size,
                "COMMUNICATION": self.communicationCores.size
                }

    def installation_ccc(self, install_method: str) -> Union[float, int]:
        """
        Find the current carrying capacity for the cable for a given installation method.
        :param install_method: The cable installation method associated with the current carrying capacity.
        :return:
        """
        if install_method.upper() in ["UNENCLOSED_SPACED", "UNENCLOSEDSPACED"]:
            return self.unenclosedSpaced.ccc
        elif install_method.upper() in ["UNENCLOSED_SURFACE", "UNENCLOSEDSURFACE"]:
            return self.unenclosedSurface.ccc
        elif install_method.upper() in ["UNENCLOSED_TOUCHING", "UNENCLOSEDTOUCHING"]:
            return self.unenclosedTouching.ccc
        elif install_method.upper() in ["ENCLOSED_CONDUIT", "ENCLOSEDCONDUIT"]:
            return self.enclosedConduit.ccc
        elif install_method.upper() in ["ENCLOSED_PARTIAL", "ENCLOSEDPARTIAL"]:
            return self.enclosedPartial.ccc
        elif install_method.upper() in ["ENCLOSED_COMPLETE", "ENCLOSEDCOMPLETE"]:
            return self.enclosedComplete.ccc
        elif install_method.upper() in ["BURIED_DIRECT", "BURIEDDIRECT"]:
            return self.buriedDirect.ccc
        elif install_method.upper() in ["DUCTS_SINGLE", "DUCTSSINGLE"]:
            return self.ductsSingle.ccc
        elif install_method.upper() in ["DUCTS_PER_CABLE", "DUCTSPERCABLE"]:
            return self.ductsPerCable.ccc

    @property
    def mvam(self) -> float:
        return self.impedance.mvam

    @mvam.setter
    def mvam(self, value: float):
        self.impedance.mvam = value

    def has_active(self):
        return self.activeCores.number > 0

    def has_neutral(self):
        return self.neutralCores.number > 0

    def has_earth(self):
        return self.earthCores.number > 0

    def to_dict(self):
        return {"cable_type": self.cable_type,
                "active_cores": self.activeCores.to_dict(),
                "neutral_cores": self.neutralCores.to_dict(),
                "earth_cores": self.earthCores.to_dict(),
                "instrument_cores": self.instrumentCores.to_dict(),
                "control_cores": self.controlCores.to_dict(),
                "communication_cores": self.communicationCores.to_dict(),
                "data_cores": self.dataCores.to_dict(),
                "unenclosed_spaced": self.unenclosedSpaced.to_dict(),
                "unenclosed_surface": self.unenclosedSurface.to_dict(),
                "unenclosed_touching": self.unenclosedTouching.to_dict(),
                "enclosed_conduit": self.enclosedConduit.to_dict(),
                "enclosed_partial": self.enclosedPartial.to_dict(),
                "enclosed_complete": self.enclosedComplete.to_dict(),
                "buried_direct": self.buriedDirect.to_dict(),
                "ducts_single": self.ductsSingle.to_dict(),
                "ducts_per_cable": self.ductsPerCable.to_dict(),
                "impedance": self.impedance.to_dict(),
                "cable_screen": self.cableScreen.to_dict(),
                "core_screen": self.coreScreen.to_dict(),
                "insulation": self.insulation.to_dict(),
                "sheath": self.sheath,
                "volt_rating": self.voltage_rating,
                "flexible": self.flexible,
                "armour": self.armour,
                "revision": self.revision.to_dict(),
                "description": self.description,
                "circuit_type": self.circuit_type,
                "conductor_material": self.conductor_material,
                "core_arrangement": self.core_arrangement,
                "cable_shape": self.shape,
                }

    def from_dict(self, cable_dict: dict):
        self.cable_type = cable_dict["cable_type"]
        self.activeCores.from_dict(cable_dict["active_cores"])
        self.neutralCores.from_dict(cable_dict["neutral_cores"])
        self.earthCores.from_dict(cable_dict["earth_cores"])
        self.instrumentCores.from_dict(cable_dict["instrument_cores"])
        self.controlCores.from_dict(cable_dict["control_cores"])
        self.communicationCores.from_dict(cable_dict["communication_cores"])
        self.dataCores.from_dict(cable_dict["data_cores"])
        self.unenclosedSpaced.from_dict(cable_dict["unenclosed_spaced"])
        self.unenclosedSurface.from_dict(cable_dict["unenclosed_surface"])
        self.unenclosedTouching.from_dict(cable_dict["unenclosed_touching"])
        self.enclosedConduit.from_dict(cable_dict["enclosed_conduit"])
        self.enclosedPartial.from_dict(cable_dict["enclosed_partial"])
        self.enclosedComplete.from_dict(cable_dict["enclosed_complete"])
        self.buriedDirect.from_dict(cable_dict["buried_direct"])
        self.ductsSingle.from_dict(cable_dict["ducts_single"])
        self.ductsPerCable.from_dict(cable_dict["ducts_per_cable"])
        self.impedance.from_dict(cable_dict["impedance"])
        self.cableScreen.from_dict(cable_dict["cable_screen"])
        self.coreScreen.from_dict(cable_dict["core_screen"])
        self.insulation.from_dict(cable_dict["insulation"])
        self.sheath = cable_dict["sheath"]
        self.voltage_rating = cable_dict["volt_rating"]
        self.flexible = cable_dict["flexible"]
        self.armour = cable_dict["armour"]
        self.revision.from_dict(cable_dict["revision"])
        self.description = cable_dict["description"]
        self.circuit_type = cable_dict["circuit_type"]
        self.conductor_material = cable_dict["conductor_material"]
        self.core_arrangement = cable_dict["core_arrangement"]
        self.shape = cable_dict["cable_shape"]


class ConductorDetail:
    """
    A simple class to allow conductor characteristics to be defined.
    """
    def __init__(self, size: float = 0.0, unit: str = '', **kwargs):
        self.size = size
        self.unit = unit
        self.kwargs = kwargs

    @property
    def size(self) -> float:
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    @property
    def unit(self) -> str:
        return self._size_unit

    @unit.setter
    def unit(self, unit: str):
        self._size_unit = unit.upper()

    def to_dict(self):
        return {'size': self.size, 'key': self.unit}

    def from_dict(self, details: dict):
        self.size = details["size"]
        self.unit = details["key"]


class ConductorCableRun:
    def __init__(self, active_size: float = 0.0, active_unit: str = '', neutral_size: float = 0.0,
                 neutral_unit: str = '', earth_size: float = 0.0, earth_unit: str = '',
                 instrumentation_size: float = 0.0, instrumentation_unit: str = '', control_size: float = 0.0,
                 control_unit: str = '', data_size: float = 0.0, data_unit: str = '', communication_size: float = 0.0,
                 communication_unit: str = ""):
        self.activeConductors = ConductorDetail(active_size, active_unit)
        self.neutralConductors = ConductorDetail(neutral_size, neutral_unit)
        self.earthConductors = ConductorDetail(earth_size, earth_unit)
        self.instrumentationConductors = ConductorDetail(instrumentation_size, instrumentation_unit)
        self.controlConductors = ConductorDetail(control_size, control_unit)
        self.dataConductors = ConductorDetail(data_size, data_unit)
        self.communicationConductors = ConductorDetail(communication_size, communication_unit)

    def to_dict(self):
        return {"active_conductors": self.activeConductors.to_dict(),
                "neutral_conductors": self.neutralConductors.to_dict(),
                "earth_conductors": self.earthConductors.to_dict(),
                "communication_conductors": self.communicationConductors.to_dict(),
                "instrumentation_conductors": self.instrumentationConductors.to_dict(),
                "data_conductors": self.dataConductors.to_dict(),
                "control_conductors": self.controlConductors.to_dict(),
                }

    def from_dict(self, details: dict):
        self.activeConductors.from_dict(details["active_conductors"])
        self.neutralConductors.from_dict(details["neutral_conductors"])
        self.earthConductors.from_dict(details["earth_conductors"])
        self.communicationConductors.from_dict(details["communication_conductors"])
        self.instrumentationConductors.from_dict(details["instrumentation_conductors"])
        self.dataConductors.from_dict(details["data_conductors"])
        self.controlConductors.from_dict(details["control_conductors"])


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
            self._date = None
        else:
            self._date = date

    def to_dict(self) -> dict:
        return {'number': self.number, 'date': self.date}

    def from_dict(self, details: dict):
        self.number = details["number"]
        self.date = details["date"]


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

    def to_dict(self):
        return {
            "mvam": self.mvam,
            "r": self.r,
            "r_unit": self.r_unit,
            "x": self.x,
            "x_unit": self.x_unit,
            "z": self.z,
            "z_unit": self.z_unit,
        }

    def from_dict(self, details: dict):
        self.mvam = details["mvam"]
        self.r = details["r"]
        self.r_unit = details["r_unit"]
        self.x = details["x"]
        self.x_unit = details["x_unit"]
        self.z = details["z"]
        self.z_unit = details["z_unit"]


class Insulation:
    def __init__(self, insulation_material: str = "", insulation_code: str = '', op_temp: int = 0, max_temp: int = 0):
        """
        :param insulation_material: The cable_list's insulation material.
        :param insulation_code: The insulation code.
        :param max_temp: The maximum continuous operating temperature of the cable_list conductor.
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

    def to_dict(self):
        return {
            'material': self.material,
            'code': self.code,
            'op_temp': self.op_temp,
            'max_temp': self.max_temp,
        }

    def from_dict(self, details: dict):
        self.material = details["material"]
        self.code = details["code"]
        self.op_temp = details["op_temp"]
        self.max_temp = details["max_temp"]


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

    def to_dict(self) -> dict:
        return {'supply': self.supply,
                'install': self.install,
                'connect': self.connect
                }

    def from_dict(self, details: dict):
        self.supply = details["supply"]
        self.install = details["install"]
        self.connect = details["connect"]


class Circuit:
    def __init__(self, circuit_type: str = '', voltage: int = 0, voltage_unit: str = '', frequency: int = 0,
                 frequency_unit: str = '', waveform: str = '', phases: int = 0, neutral_required: bool = True,
                 physical_method: str = '', cable_arrangement: str = '', load_current: float = 0.0):
        """
        :param circuit_type: The cable_type of circuit.
        :param voltage: The circuit's voltage.
        :param voltage_unit: Circuit voltage key
        :param frequency: frequency of the circuit 0 = DC
        :param frequency_unit: Unit of frequency measurement.
        :param waveform: Is the circuit AC or DC
        :param phases: The number of phases for the circuit
        :param neutral_required: Does the circuit require a neutral?
        :param physical_method: How the cable_list is intended to be physically installed
        :param cable_arrangement: How the cables are to be arranged when installed.
        :param load_current: The circuit's load current.
        """
        self.circuit_type = circuit_type
        self.voltage = Voltage(voltage, voltage_unit, phases, neutral_required)
        self.frequency = Frequency(frequency, frequency_unit, waveform)
        self.installation = InstallationMethod(physical_method, cable_arrangement)
        self.load_current = load_current

    @property
    def circuit_type(self) -> str:
        return self._type

    @circuit_type.setter
    def circuit_type(self, value: str):
        self._type = value.upper()

    @property
    def load_current(self) -> float:
        return self._load_current

    @load_current.setter
    def load_current(self, amps: float):
        self._load_current = amps

    def to_dict(self):
        return {"circuit_type": self.circuit_type, "voltage": self.voltage.to_dict(),
                "frequency": self.frequency.to_dict(), "installation_name": self.installation.to_dict(),
                "load_current": self.load_current}

    def from_dict(self, details: dict):
        self.circuit_type = details["circuit_type"]
        self.voltage.from_dict(details["voltage"])
        self.frequency.from_dict(details["frequency"])
        self.installation.from_dict(details["installation_name"])
        self.load_current = details["load_current"]


class Vector:
    """
    A simple class to represent a magnitude, key vector pair.
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

    def to_dict(self) -> dict:
        return {"magnitude": self.magnitude, "key": self.unit}

    def from_dict(self, details: dict):
        self.magnitude = details["magnitude"]
        self.unit = details["key"]


class InstallationMethod:
    """
    A simple class to represent the physical installation of cables and cable_list run.
    """
    def __init__(self, installation=None, arrangement: str = ''):
        self.physical_installation = installation
        self.cable_arrangement = arrangement

    @property
    def physical_installation(self) -> str:
        return self._physical_installation

    @physical_installation.setter
    def physical_installation(self, installation: str):
        if installation is None:
            self._physical_installation = installation
        else:
            self._physical_installation = installation.upper()

    @property
    def cable_arrangement(self) -> str:
        return self._cable_arrangement

    @cable_arrangement.setter
    def cable_arrangement(self, arrangement: str):
        if arrangement is None:
            self._cable_arrangement = arrangement
        else:
            self._cable_arrangement = arrangement.upper()

    def to_dict(self) -> dict:
        x: dict = dict()
        x["installation"] = self.physical_installation
        x["arrangement"] = self.cable_arrangement
        return x

    def from_dict(self, details: dict):
        self.physical_installation = details["installation"]
        self.cable_arrangement = details["arrangement"]


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
        return {
            'waveform': self.waveform,
            'frequency': self.frequency,
            'key': self.unit,
        }

    def from_dict(self, details: dict):
        self.waveform = details["waveform"]
        self.frequency = details["frequency"]
        self.unit = details["key"]


class Voltage:
    """
    A simple class for voltage details.
    """
    def __init__(self, volts: int = None, unit: str = '', phases: int = 0, neutral_required: bool = True):
        self.v: int = volts
        self.unit: str = unit
        self.phases: int = phases
        self.neutral_required: bool = neutral_required

    @property
    def phases(self) -> int:
        return self._phases

    @phases.setter
    def phases(self, phases: int):
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
        return {
            'v': self.v,
            'key': self.unit,
            'phases': self.phases,
            'neutral_required': self.neutral_required,
        }

    def from_dict(self, details: dict):
        self.v = details["v"]
        self.unit = details["key"]
        self.phases = details["phases"]
        self.neutral_required = details["neutral_required"]


class CoreDetails:
    def __init__(self, csa: float = 0, csa_unit: str = "", number: int = 0, name: str = ""):
        """
        This class defines and checks the details of a cable_list core.
        :param csa: Cross sectional area of the main conductors
        :param csa_unit: The cross-sectional area key of measurement.
        :param number: The number of cable_list cores including earth and neutrals.
        :param name: Description of the cable_list cores.
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
        return {
            'size': self.size,
            'key': self.unit,
            'number': self.number,
            'name': self.name,
        }

    def from_dict(self, details: dict):
        self.size = details["size"]
        self.unit = details["key"]
        self.number = details["number"]
        self.name = details["name"]


class CableInstallationMethod:
    def __init__(self, ccc: int = 0, install_temp: int = 0, cable_arrangement: str = ""):
        """
        This class defines and checks the details of the cable_list installation details.
        :param ccc: Current carrying capacity  of the cable_list cable_list.
        :param install_temp: Ambient temperature associated with installation.
        :param cable_arrangement: The arrangement of the cable_list cores. Single core cables only.
        """
        self.ccc: int = ccc
        self.install_temp: int = install_temp
        self.cable_arrangement: str = cable_arrangement

    @property
    def ccc(self) -> int:
        return self._ccc

    @ccc.setter
    def ccc(self, value: int):
        self._ccc = value

    @property
    def install_temp(self) -> int:
        return self._temp

    @install_temp.setter
    def install_temp(self, value: int):
        self._temp = value

    @property
    def cable_arrangement(self) -> str:
        return self._cable_arrangement

    @cable_arrangement.setter
    def cable_arrangement(self, value: str):
        self._cable_arrangement = value.upper()

    def to_dict(self) -> dict:
        """
        Convert the class to a dictionary.
        :return:
        """
        return {
            'ccc': self.ccc,
            'install_temp': self.install_temp,
            'arrangement': self.cable_arrangement,
        }

    def from_dict(self, details: dict):
        self.ccc = details["ccc"]
        self.install_temp = details["install_temp"]
        self.cable_arrangement = details["arrangement"]


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

    def to_dict(self):
        return {'name': self.name, 'fault_withstand': self.fault_withstand}

    def from_dict(self, details: dict):
        self.name = details["name"]
        self.fault_withstand = details["fault_withstand"]


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

    def to_dict(self):
        return {'name': self.name, 'part_number': self.part_number}

    def from_dict(self, details: dict):
        self.name = details["name"]
        self.part_number = details["part_number"]


class I2T:
    def __init__(self, k_factor: int = 0, amp_time: List[Tuple[int, float]] = None):
        self.k_factor: int = k_factor
        self._amp_time = []
        self.amp_time: list = amp_time

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
        elif isinstance(value, list):
            for pair in value:
                self._amp_time.append(pair)
        else:
            self._amp_time.append(value)

    def to_dict(self):
        return {'k_factor': self.k_factor, 'amp_time': self.amp_time}

    def from_dict(self, details: dict):
        self.k_factor = details["k_factor"]
        self.amp_time = details["amp_time"]
