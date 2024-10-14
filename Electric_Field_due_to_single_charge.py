import math

# Coulomb constant in Nm^2/C^2
k = 8.99e9

def electric_field_single_charge(q, r):
    """
    Calculate the electric field due to a single point charge using Coulomb's law.
    """
    if r == 0:
        raise ValueError("Distance r cannot be zero to avoid division by zero.")
    return k * q / r**2
