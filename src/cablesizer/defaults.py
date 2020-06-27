import pathlib as path
import json as json


class CableRun:
    """
    A class to store the default values for the cable_list run. The default values are stored in the "cable.json" file
    as a JSON object.
    """
    def __init__(self, fp, single_phase_arrangement: list = [], single_phase_name: str = None,
                 single_phase_abbreviation: str = None, single_phase_default: str = None,
                 multi_phase_arrangement: list = [], multi_phase_name: str = None, multi_phase_abbreviation: str = None,
                 multi_phase_default: str = None, control_arrangement: list = [], control_name: str = None,
                 control_abbreviation: str = None, control_default: str = None, instrument_pair_arrangement: list = [],
                 instrument_pair_name: str = None, instrument_pair_abbreviation: str = None,
                 instrument_pair_default: str = None, instrument_triple_arrangement: list = [],
                 instrument_triple_name: str = None, instrument_triple_abbreviation: str = None,
                 instrument_triple_default: str = None, shape_description: list = [], shape_default: str = None,
                 conductor_material_description: list = [], conductor_material_default: str = None):
        """

        :param fp:
        :param single_phase_arrangement:
        :param single_phase_name:
        :param single_phase_abbreviation:
        :param single_phase_default:
        :param multi_phase_arrangement:
        :param multi_phase_name:
        :param multi_phase_abbreviation:
        :param multi_phase_default:
        :param control_arrangement:
        :param control_name:
        :param control_abbreviation:
        :param control_default:
        :param instrument_pair_arrangement:
        :param instrument_pair_name:
        :param instrument_pair_abbreviation:
        :param instrument_pair_default:
        :param instrument_triple_arrangement:
        :param instrument_triple_name:
        :param instrument_triple_abbreviation:
        :param instrument_triple_default:
        """
        self.single_phase = CoreArrangement(single_phase_arrangement, single_phase_name, single_phase_abbreviation,
                                            single_phase_default)
        self.multi_phase = CoreArrangement(multi_phase_arrangement, multi_phase_name, multi_phase_abbreviation,
                                           multi_phase_default)
        self.control = CoreArrangement(control_arrangement, control_name, control_abbreviation, control_default)
        self.instrument_pair = CoreArrangement(instrument_pair_arrangement, instrument_pair_name,
                                               instrument_pair_abbreviation, instrument_pair_default)
        self.instrument_triplex = CoreArrangement(instrument_triple_arrangement, instrument_triple_name,
                                                  instrument_triple_abbreviation, instrument_triple_default)
        self.shape = BasicDefaults(shape_description, shape_default)
        self.conductor_material = BasicDefaults(conductor_material_description, conductor_material_default)
        self._cable = None
        self._cct = None
        self._install_method = None
        self._pwr_unit = None
        self._json = None
        self.load_file(fp)
        self.load_data()

    def load_file(self, fp):
        """
        Load a .json file.
        :param fp:
        """
        fp = path.Path(fp)
        with open(fp, newline='', encoding='utf-8-sig') as jsonfile:
            self._json = json.load(jsonfile)

    def load_data(self):
        self.cable = self._json["cable"]
        self.circuit = self._json["circuit"]
        self.installation = self._json["install_method"]
        self.power_unit = self._json["power_unit"]
        self._json = None

    @property
    def cable(self) -> dict:
        return self._cable

    @cable.setter
    def cable(self, value: dict):
        self._cable = value

    @property
    def circuit(self) -> dict:
        return self._cct

    @circuit.setter
    def circuit(self, value: dict):
        self._cct = value

    @property
    def installation(self) -> dict:
        return self._install_method

    @installation.setter
    def installation(self, value: dict):
        self._install_method = value

    @property
    def power_unit(self) -> dict:
        return self._pwr_unit

    @power_unit.setter
    def power_unit(self, value: dict):
        self._pwr_unit = value


class CoreArrangement:
    def __init__(self, description: list = "", name: str = None, abbreviation: str = None, default: str = None):
        """

        :param description:
        :param name:
        :param abbreviation:
        :param default:
        """
        self.description = description
        self.name = name
        self.abbreviation = abbreviation
        self.default = default

    @property
    def description(self) -> list:
        return self._descrip

    @description.setter
    def description(self, value: list):
        self._descrip = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if value is not None:
            self._name = value.upper()
        else:
            self._name = value

    @property
    def abbreviation(self) -> str:
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, value: str):
        if value is not None:
            self._abbreviation = value.upper()
        else:
            self._abbreviation = value

    @property
    def default(self) -> str:
        return self._default.upper()

    @default.setter
    def default(self, value: str):
        if value is None:
            self._default = value
        elif value.upper() in self.description:
            self._default = value.upper()
        # elif value is None:
        #     self._default = value
        else:
            raise ValueError(f"Value ({value}) not contained in description list")

    def to_dict(self) -> dict:
        """
        Return the class as a dictionary.
        :return:
        """
        return {"description": self.description,
                "name": self.name,
                "abbreviation": self.abbreviation,
                "default": self.default
                }

    def from_dict(self, value: dict):
        """
        Populate the class via a dictionary
        :param value:
        :return:
        """
        self.description = value["description"]
        self.name = value["name"]
        self.abbreviation = value["abbreviation"]
        self.default = value["default"]


class BasicDefaults:
    def __init__(self, description: list = [], default: str = None):
        self.description = description
        self.default = default

    @property
    def description(self) -> list:
        return self._descrip

    @description.setter
    def description(self, value: list):
        if value is not None:
            self._descrip = value

    @property
    def default(self) -> str:
        return self._default.upper()

    @default.setter
    def default(self, value: str):
        if value is None:
            self._default = value
        elif value.upper() in self.description:
            self._default = value.upper()
        else:
            raise ValueError(f"Value ({value}) not contained in description list")

    def to_dict(self) -> dict:
        """
        Return the class as a dictionary.
        :return:
        """
        return {"description": self.description,
                "default": self.default
                }

    def from_dict(self, value: dict):
        """
        Populate the class via a dictionary
        :param value:
        :return:
        """
        self.description = value["description"]
        self.default = value["default"]
