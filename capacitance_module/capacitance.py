"""
capacitance.py
This module provides functions to calculate the capacitance of a parallel plate
capacitor based on the physical properties of the plates and the material
between them. The capacitance depends on the area of the plates, the distance
between the plates, and the permittivity of the material (e.g., air or a
dielectric).

Functions:
- calculate_capacitance(area, distance): Calculates the capacitance based on
  the area of the plates and the distance between them in a vacuum (or air).
- calculate_capacitance_with_dielectric(area, distance, permittivity): 
  Calculates the capacitance when a dielectric material is present.
- calculate_total_capacitance_series(capacitors): Calculates the total 
  capacitance for capacitors connected in series.
- calculate_total_capacitance_parallel(capacitors): Calculates the total
  capacitance for capacitors connected in parallel.

The module also handles special cases such as calculating parasitic capacitance,
which can affect the overall performance of high-frequency circuits.
"""

# Constant: Permittivity of free space (F/m)
EPSILON_0 = 8.854e-12


def calculate_capacitance(area, distance):
    """
    Calculate the capacitance (C) of a parallel plate capacitor in a vacuum or
    air, using the plate area and distance between the plates.

    Args:
        area (float): The area of the plates in square meters (m^2).
        distance (float): The distance between the plates in meters (m).

    Returns:
        float: The capacitance in Farads (F).

    Example:
        >>> calculate_capacitance(1.0, 0.01)
        8.854e-10
    """
    capacitance = (EPSILON_0 * area) / distance
    return capacitance


def calculate_capacitance_with_dielectric(area, distance, permittivity):
    """
    Calculate the capacitance of a parallel plate capacitor when a dielectric
    material is present between the plates.

    Args:
        area (float): The area of the plates in square meters (m^2).
        distance (float): The distance between the plates in meters (m).
        permittivity (float): The permittivity of the dielectric material.

    Returns:
        float: The capacitance in Farads (F).

    Example:
        >>> calculate_capacitance_with_dielectric(1.0, 0.01, 5)
        4.427e-9
    """
    capacitance = (permittivity * EPSILON_0 * area) / distance
    return capacitance


def calculate_total_capacitance_series(capacitors):
    """
    Calculate the total capacitance for capacitors connected in series.

    Args:
        capacitors (list of float): List of capacitances in Farads (F).

    Returns:
        float: The total capacitance in series.

    Example:
        >>> calculate_total_capacitance_series([1e-6, 2e-6, 3e-6])
        5e-7
    """
    return 1 / sum(1 / c for c in capacitors)


def calculate_total_capacitance_parallel(capacitors):
    """
    Calculate the total capacitance for capacitors connected in parallel.

    Args:
        capacitors (list of float): List of capacitances in Farads (F).

    Returns:
        float: The total capacitance in parallel.

    Example:
        >>> calculate_total_capacitance_parallel([1e-6, 2e-6, 3e-6])
        6e-6
    """
    return sum(capacitors)


def calculate_parasitic_capacitance(area, distance):
    """
    Calculate the parasitic capacitance between components or wiring segments
    in a circuit, based on the geometry and separation of the conductors.

    Args:
        area (float): The effective area of the conductors (m^2).
        distance (float): The separation between the conductors (m).

    Returns:
        float: The parasitic capacitance in Farads (F).

    Example:
        >>> calculate_parasitic_capacitance(0.001, 0.01)
        8.854e-14
    """
    capacitance = (EPSILON_0 * area) / distance
    return capacitance
