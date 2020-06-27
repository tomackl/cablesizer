import pathlib as path
import json as json


class CableRun:
    """
    A class to store the default values for the cable_list run. The default values are stored in the "cable.json" file
    as a JSON object.
    """
    def __init__(self, fp):
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