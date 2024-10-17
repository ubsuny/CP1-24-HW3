import math
from lorentz_force import lorentz_force

def test_lorentz_force_at_90_degrees():
    """Test when angle between velocity and magnetic field is 90 degrees."""
    charge = 1.6e-19  # Coulombs
    velocity = 2e6  # m/s
    magnetic_field = 0.01  # Tesla
    angle_radians = math.pi / 2  # 90 degrees

    expected_force = charge * velocity * magnetic_field
    assert math.isclose(lorentz_force(charge, velocity, magnetic_field, angle_radians), expected_force)


def test_lorentz_force_at_0_degrees():
    """Test when angle between velocity and magnetic field is 0 degrees."""
    charge = 1.6e-19  # Coulombs
    velocity = 2e6  # m/s
    magnetic_field = 0.01  # Tesla
    angle_radians = 0  # 0 degrees

    expected_force = 0  # sin(0) is 0
    assert math.isclose(lorentz_force(charge, velocity, magnetic_field, angle_radians), expected_force)


def test_lorentz_force_with_zero_charge():
    """Test when charge is zero."""
    charge = 0  # Coulombs
    velocity = 2e6  # m/s
    magnetic_field = 0.01  # Tesla
    angle_radians = math.pi / 2  # 90 degrees

    expected_force = 0
    assert math.isclose(lorentz_force(charge, velocity, magnetic_field, angle_radians), expected_force)


def test_lorentz_force_with_zero_velocity():
    """Test when velocity is zero."""
    charge = 1.6e-19  # Coulombs
    velocity = 0  # m/s
    magnetic_field = 0.01  # Tesla
    angle_radians = math.pi / 2  # 90 degrees

    expected_force = 0
    assert math.isclose(lorentz_force(charge, velocity, magnetic_field, angle_radians), expected_force)


def test_lorentz_force_with_zero_magnetic_field():
    """Test when magnetic field is zero."""
    charge = 1.6e-19  # Coulombs
    velocity = 2e6  # m/s
    magnetic_field = 0  # Tesla
    angle_radians = math.pi / 2  # 90 degrees

    expected_force = 0
    aassert math.isclose(lorentz_force(charge, velocity, magnetic_field, angle_radians), expected_force)


def test_lorentz_force_with_negative_charge():
    """Test with a negative charge."""
    charge = -1.6e-19  # Coulombs (electron)
    velocity = 2e6  # m/s
    magnetic_field = 0.01  # Tesla
    angle_radians = math.pi / 2  # 90 degrees

    expected_force = charge * velocity * magnetic_field  # Should be negative
    assert math.isclose(lorentz_force(charge, velocity, magnetic_field, angle_radians), expected_force)


def test_lorentz_force_with_negative_magnetic_field():
    """Test with a negative magnetic field."""
    charge = 1.6e-19  # Coulombs
    velocity = 2e6  # m/s
    magnetic_field = -0.01  # Tesla
    angle_radians = math.pi / 2  # 90 degrees

    expected_force = charge * velocity * magnetic_field  # Should be negative
    assert math.isclose(lorentz_force(charge, velocity, magnetic_field, angle_radians), expected_force)
