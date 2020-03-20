#
#
import json


def import_json_config(path: str) -> dict:
    """
    Import the cable_list configuration values. These configuration values are user settable.
    :param path: Path to the json config file.
    :return:
    """
    with open(path) as fp:
        cable_data = json.load(fp)
    return cable_data


