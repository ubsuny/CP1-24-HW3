# resistance.py

def resistance(length, area, resistivity):
    """
    Calculate the resistance of a wire.

    Parameters:
    length (float): Length of the wire in meters.
    area (float): Cross-sectional area of the wire in square meters.
    resistivity (float): Resistivity of the material in ohm meters.

    Returns:
    float: Resistance in ohms.
    """
    return resistivity * (length / area)

def batch_resistances(lengths, areas, resistivities):
    """
    Calculate resistances for a list of lengths, areas, and resistivities using map and lambda.

    Parameters:
    lengths (list of float): List of wire lengths.
    areas (list of float): List of cross-sectional areas.
    resistivities (list of float): List of resistivities of materials.

    Returns:
    list of float: List of resistances for the given lengths, areas, and resistivities.
    """
    return list(map(lambda l, A, r: resistance(l, A, r), lengths, areas, resistivities))