"""
This module calculates the capacitance of a spherical capacitor 
with optionally specified dielectrics (up to 2 layers).

Functions:
- calculate_spherical_capacitance(inner_r, outer_r, dielectrics): 
  Calculates the capacitance with specified dielectrics.

Functional programming concepts used:
- Lambda functions
- The `reduce` function
"""
from functools import reduce
import numpy as np

EPSILON_0 = 8.854187817e-12  # Vacuum permittivity (F/m)


def calculate_spherical_capacitance(inner_r, outer_r, dielectrics):
    '''
    Calculate the capacitance of a spherical capacitor with specified dielectrics.

    Parameters:
    - inner_r: Inner radius (meters), inner_r > 0
    - outer_r: Outer radius (meters), outer_r > inner_r
    - dielectrics: List of dictionaries, each containing:
        - 'epsilon_r': Relative permittivity (dimensionless)
        - 'inner_r': Inner radius of the dielectric layer (meters)
        - 'outer_r': Outer radius of the dielectric layer (meters)
    Returns:
    - Capacitance (farads)
    '''
    if inner_r <= 0 or outer_r <= 0:
        raise ValueError("Radii must be positive numbers.")
    if outer_r <= inner_r:
        raise ValueError("Outer radius must be greater than inner radius.")
    if len(dielectrics) > 2:
        raise ValueError("At most 2 dielectrics are supported.")

    # If no dielectrics are specified, assume vacuum
    if not dielectrics:
        capacitance = 4 * np.pi * EPSILON_0 * (inner_r * outer_r) / (outer_r - inner_r)
        return capacitance

    # Validate and calculate capacitance for each dielectric layer
    capacitances = []

    for dielectric in dielectrics:
        epsilon_r = dielectric.get('epsilon_r', 1.0)
        r1 = dielectric.get('inner_r')
        r2 = dielectric.get('outer_r')

        if r1 is None or r2 is None:
            raise ValueError("Dielectric layers must have 'inner_r' and 'outer_r'.")
        if r1 <= 0 or r2 <= 0:
            raise ValueError("Dielectric layer radii must be positive numbers.")
        if r2 <= r1:
            raise ValueError("Dielectric layer outer radius must be greater than inner radius.")
        if r1 < inner_r or r2 > outer_r:
            raise ValueError("Dielectric layers must be within the capacitor radii.")

        # Capacitance of the dielectric layer
        capacitance_i = 4 * np.pi * EPSILON_0 * epsilon_r * (r1 * r2) / (r2 - r1)
        capacitances.append(capacitance_i)

    # Combine the capacitances in series using reduce and a lambda function
    reciprocal_total = reduce(lambda acc, capacitance_i: acc + (1 / capacitance_i), capacitances, 0)
    capacitance_total = 1 / reciprocal_total

    return capacitance_total


if __name__ == "__main__":
    # Example usage
    INNER_R = 0.05  # Inner radius (m)
    OUTER_R = 0.1   # Outer radius (m)

    # No dielectric
    dielectric_layers = []
    capacitance_value = calculate_spherical_capacitance(INNER_R, OUTER_R, dielectric_layers)
    print(f"Capacitance with no dielectric: {capacitance_value:.6e} F")

    # One dielectric layer
    dielectric_layers = [
        {'epsilon_r': 2.0, 'inner_r': INNER_R, 'outer_r': OUTER_R}
    ]
    capacitance_value = calculate_spherical_capacitance(INNER_R, OUTER_R, dielectric_layers)
    print(f"Capacitance with one dielectric layer: {capacitance_value:.6e} F")

    # Two dielectric layers
    dielectric_layers = [
        {'epsilon_r': 2.0, 'inner_r': INNER_R, 'outer_r': 0.075},
        {'epsilon_r': 3.0, 'inner_r': 0.075, 'outer_r': OUTER_R}
    ]
    capacitance_value = calculate_spherical_capacitance(INNER_R, OUTER_R, dielectric_layers)
    print(f"Capacitance with two dielectric layers: {capacitance_value:.6e} F")
