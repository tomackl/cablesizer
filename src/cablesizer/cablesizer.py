#
#
import json


def determine_electrical_load(load, unit, voltage, phases):
    """
    Calculate the cable_list's current (amps) load.
    :param load:
    :param unit:
    :return:

    if key == current:
        return load
    elif key == volt_amps':
        return kva_to_current(load, voltage, phases)
    elif key == watts:
        return kW_to_current(load, voltage, phases)
    """
    pass


def select_cable_from_database():
    """

    runType: string
    cableArmour: string
    cableArrangement: string
    cableFlexible: bool
    cableInsulationCode: string
    cableMultiCoreMax: string
    cableMultiCoreMin: string
    cableMaxParallelRuns: bool
    cableScreen: string
    cableShape: string
    cableSheath: string
    cableSingleCoreMin: string
    cableSingleCoreMax: string
    cableType: string
    cableVoltRating: string
    conductorMaterial: string
    coreArrangement: string
    allowSingleCore: bool
    allowParallelMulti: bool
    coreScreen: string
    manufacturerName: string
    neutralSize: float
    runDerating

    :return:
    """
