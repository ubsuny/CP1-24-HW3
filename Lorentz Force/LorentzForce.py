import math

def lorentz_force(charge, velocity, magnetic_field, angle_radians):
    """
    Calculate the magnetic force on a moving charge.

    Args:
    charge (float): The charge of the particle in Coulombs.
    velocity (float): The velocity of the particle in meters per second.
    magnetic_field (float): The strength of the magnetic field in Teslas.
    angle_radians (float): The angle between the velocity and the magnetic field in radians.

    Returns:
    float: The Lorentz force in Newtons.
    """
    return charge * velocity * magnetic_field * math.sin(angle_radians)
