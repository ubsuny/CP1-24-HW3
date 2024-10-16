"""
Coulomb's Law Calculations

This module provides functionality to calculate the electric force between two point charges
based on Coulomb's law.
"""

# Coulomb's constant in N·m²/C² (Coulomb's Law constant)
COULOMBS_CONSTANT = 8.99e9

# Lambda function to calculate the electric force between two charges
calculate_electric_force = lambda q1, q2, r: (
    print("Distance between charges cannot be zero.")
    if r == 0 else 
    COULOMBS_CONSTANT * abs(q1 * q2) / r**2
)

"""
Calculate the electric force between two point charges using Coulomb's law.

Args:
q1 (float): The first charge in coulombs (C).
q2 (float): The second charge in coulombs (C).
r (float): The distance between the charges in meters (m).

Returns:
float: The calculated electric force in newtons (N), or prints a message if the distance is zero.

If the distance between the charges is zero, the function will print an error message 
('Distance between charges cannot be zero.') instead of calculating the force.
"""
