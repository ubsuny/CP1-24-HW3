'''
spherical_capacitor.py

This module calculates the capacitance of a spherical capacitor with specified dielectrics (up to 2 layers).

Functions:
- calculate_spherical_capacitance(a, b, dielectrics): Calculates the capacitance with specified dielectrics.

Functional programming concepts used:
- Lambda functions
- The `reduce` function
'''

import numpy as np
from functools import reduce

EPSILON_0 = 8.854187817e-12  # Vacuum permittivity (F/m)


def calculate_spherical_capacitance(a, b, dielectrics):
    '''
    Calculate the capacitance of a spherical capacitor with specified dielectrics.

    Parameters:
    - a: Inner radius (meters), a > 0
    - b: Outer radius (meters), b > a
    - dielectrics: List of dictionaries, each containing:
        - 'epsilon_r': Relative permittivity (dimensionless)
        - 'inner_radius': Inner radius of the dielectric layer (meters)
        - 'outer_radius': Outer radius of the dielectric layer (meters)

    Returns:
    - Capacitance (farads)
    '''
    if a <= 0 or b <= 0:
        raise ValueError("Radii must be positive numbers.")
    if b <= a:
        raise ValueError("Outer radius must be greater than inner radius.")
    if len(dielectrics) > 2:
        raise ValueError("At most 2 dielectrics are supported.")

    # If no dielectrics are specified, assume vacuum
    if not dielectrics:
        C = 4 * np.pi * EPSILON_0 * (a * b) / (b - a)
        return C

    # Validate and calculate capacitance for each dielectric layer
    capacitances = []

    for dielectric in dielectrics:
        epsilon_r = dielectric.get('epsilon_r', 1.0)
        r1 = dielectric.get('inner_radius')
        r2 = dielectric.get('outer_radius')

        if r1 is None or r2 is None:
            raise ValueError("Dielectric layers must have 'inner_radius' and 'outer_radius'.")
        if r1 <= 0 or r2 <= 0:
            raise ValueError("Dielectric layer radii must be positive numbers.")
        if r2 <= r1:
            raise ValueError("Dielectric layer outer radius must be greater than inner radius.")
        if r1 < a or r2 > b:
            raise ValueError("Dielectric layers must be within the capacitor radii.")

        # Capacitance of the dielectric layer
        C_i = 4 * np.pi * EPSILON_0 * epsilon_r * (r1 * r2) / (r2 - r1)
        capacitances.append(C_i)

    # Combine the capacitances in series using `reduce` and a lambda function
    reciprocal_C_total = reduce(lambda acc, C_i: acc + (1 / C_i), capacitances, 0)
    C_total = 1 / reciprocal_C_total

    return C_total


if __name__ == "__main__":
    # Example usage
    a = 0.05  # Inner radius (m)
    b = 0.1   # Outer radius (m)

    # No dielectric
    dielectrics = []
    C = calculate_spherical_capacitance(a, b, dielectrics)
    print(f"Capacitance with no dielectric: {C:.6e} F")

    # One dielectric layer
    dielectrics = [
        {'epsilon_r': 2.0, 'inner_radius': a, 'outer_radius': b}
    ]
    C = calculate_spherical_capacitance(a, b, dielectrics)
    print(f"Capacitance with one dielectric layer: {C:.6e} F")

    # Two dielectric layers
    dielectrics = [
        {'epsilon_r': 2.0, 'inner_radius': a, 'outer_radius': 0.075},
        {'epsilon_r': 3.0, 'inner_radius': 0.075, 'outer_radius': b}
    ]
    C = calculate_spherical_capacitance(a, b, dielectrics)
    print(f"Capacitance with two dielectric layers: {C:.6e} F")
