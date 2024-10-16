"""
This module calculates the electric field due to a single charge and the net electric field
due to multiple point charges using Coulomb's law.
"""

import numpy as np

# Coulomb constant in Nm^2/C^2
k = 8.99e9

# Lambda functions
separation_vector = lambda p, o: (p[0] - o[0], p[1] - o[1])  # Separation vector between two points
magnitude = lambda v: np.sqrt(v[0]**2 + v[1]**2)  # Magnitude of a 2D vector

def electric_field_single_charge(q, r_vector):
    """
    Calculate the electric field due to a single point charge at a given point.

    Parameters:
    q (float): Charge in Coulombs
    r_vector (tuple or list): The vector from the charge to the point where the field is calculated (x, y)
    
    Returns:
    tuple: The electric field vector (Ex, Ey) in N/C
    """
    r_mag = magnitude(r_vector)  # Calculate the magnitude of the separation vector
    if r_mag == 0:
        raise ValueError("The point cannot be located at the same position as the charge.")

    # Electric field magnitude
    E_magnitude = k * q / r_mag**2
    # Unit vector in the direction of r_vector
    unit_vector = (r_vector[0] / r_mag, r_vector[1] / r_mag)

    # Electric field vector components 
    E_vector = (E_magnitude * unit_vector[0], E_magnitude * unit_vector[1])
    
    return E_vector

def net_electric_field(charges_positions, point_position):
    """
    Calculate the net electric field at a given point due to multiple point charges.
    Parameters:
    charges_positions (list of tuples): A list of tuples, where each tuple contains:
        - charge (q) in Coulombs,
        - position (x, y) in meters of the charge.
    point_position (tuple): The (x, y) position in meters where the net electric field is calculated.
    Returns:
    tuple: The net electric field vector (Ex, Ey) in N/C
    """

    # Use map to calculate the electric field vector for each charge at the target point
    fields = map(
        lambda charge: electric_field_single_charge(
            charge[0], separation_vector(point_position, charge[1])
        ), charges_positions
    )
    # List comprehension to gather x and y components of electric fields from all charges
    fields_x = [field[0] for field in fields]
    fields_y = [field[1] for field in fields]

    # Use sum to sum up all x and y components to get the net field
    net_field_x = sum(fields_x)
    net_field_y = sum(fields_y)

    return net_field_x, net_field_y
# Example
if __name__ == "__main__":
    charges_positions_list = [(1e-6, (1, 0)), (-2e-6, (-1, 0)), (1e-6, (0, 1))]
    target_point = (0, 0)
    net_field = net_electric_field(charges_positions_list, target_point)
    print(f"Net electric field at point {target_point}: Ex = {net_field[0]:.2e} N/C, Ey = {net_field[1]:.2e} N/C")
