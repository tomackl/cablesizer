#
#
import json
import pathlib as path

def import_cable_config():
    """
    Import the cable configuration values. These configuration values are user settable.
    :return:
    """
    cable_config = {}
    print(f'File directory !!! - {path.Path.cwd()}')
    with open("./cable.config") as fp:
        cable_config = json.load(fp)
    return cable_config

