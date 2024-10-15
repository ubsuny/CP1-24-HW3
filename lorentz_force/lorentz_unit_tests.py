"""
Module to test lorentz_force.py
"""

import math
from lorentz_force import lorentz_force

def test_lorentz_force_at_90_degrees():
    """
    Test case where the angle between velocity and magnetic field is 90 degrees (π/2 radians).
    The sin(90 degrees) is 1, so the force should be maximized.
    """
    charge = 1.6e-19  # Charge in Coulombs
    velocity = 2e6    # Velocity in m/s
    magnetic_field = 0.01  # Magnetic field in Tesla
    angle_radians = math.pi / 2  # 90 degrees

    expected_force = charge * velocity * magnetic_field  # sin(90 degrees) is 1
    assert math.isclose(lorentz_force(
        charge, velocity, magnetic_field, angle_radians), expected_force)


def test_lorentz_force_at_0_degrees():
    """
    Test case where the angle between velocity and magnetic field is 0 degrees.
    The sin(0 degrees) is 0, so the force should be zero.
    """
    charge = 1.6e-19  # Charge in Coulombs
    velocity = 2e6    # Velocity in m/s
    magnetic_field = 0.01  # Magnetic field in Tesla
    angle_radians = 0  # 0 degrees

    expected_force = 0  # sin(0 degrees) is 0
    assert lorentz_force(charge, velocity, magnetic_field, angle_radians) == expected_force


def test_lorentz_force_at_45_degrees():
    """
    Test case where the angle between velocity and magnetic field is 45 degrees (π/4 radians).
    The sin(45 degrees) is sqrt(2)/2.
    """
    charge = 1.6e-19  # Charge in Coulombs
    velocity = 2e6    # Velocity in m/s
    magnetic_field = 0.01  # Magnetic field in Tesla
    angle_radians = math.pi / 4  # 45 degrees

    expected_force = charge * velocity * magnetic_field * math.sin(angle_radians)
    assert math.isclose(lorentz_force(
        charge, velocity, magnetic_field, angle_radians), expected_force)
