# Electric_potential.py

"""
Module to calculate the electric potential due to a point charge.

Physics background:
The electric potential V at a distance r from a point charge q is given by the formula:

    V = k * q / r
    
where k is Coulomb's constant (8.99 × 10^9 N·m²/C²).

"""

# Constants
k = 8.99e9  # Coulomb's constant in Nm^2/C^2

def electric_potential(charge, distances):
    """
    Calculate the electric potential due to a point charge at multiple distances.

    Parameters:
    charge (float): The charge in Coulombs.
    distances (list of float): List of distances in meters from the charge.

    Returns:
    list of float: List of electric potentials at the given distances.
    """
    # Lambda function to calculate electric potential for a single distance
    potential_func = lambda r: k * charge / r if r != 0 else float('inf')  # To avoid division by zero

    # We use a map to apply the lambda function to each distance
    potentials = list(map(potential_func, distances))
    
    return potentials