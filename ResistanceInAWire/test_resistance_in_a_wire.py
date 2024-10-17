""" This contains the unit testing functions for Resistance_In_A_Wire_Algorithm.py """

# Importing pytest and the resistance in a wire algorithm

import pytest
from resistance_in_a_wire_algorithm import calculate_resistance, resistance_generator

# Testing the calculate resistance function with known values.

def test_calculate_resistance():
    """Calclate an expected resistance of known values to test against algorithm"""
    rho = 1.68e-8 # Resistivity of a copper wire in ohm meters.
    area = 1e-6   # Standard Cross sectional area of a wire in meters.
    length = 1    # Some length of a wire in meters.

    # Calculate the expected resistance given the above values.

    expected_resistance = rho * length / area

    # Check the algorithm calculation against the expected value.

    assert abs(calculate_resistance(rho, length, area) - expected_resistance) < 1e-10

# Testing the generator function with known values.

def test_resistance_generator():
    """Calculate expected resistances to test against algorithms generator"""
    rho = 1.68e-8 # Resistivity of a copper wire in ohm meters.
    area = 1e-6   # Standard Cross sectional area of a wire in meters.
    lengths = [1, 5, 10]    # Some lengths of a wire in a list in meters.

    # Create the generator function for the listed lengths

    resistances = resistance_generator(rho, area, lengths)

    # Calculate the expected values of resistance given the above values.

    expected_resistances = [calculate_resistance(rho, length, area) for length in lengths]

    # Check the algorithm calculation against the expected values

    for expected, actual in zip(expected_resistances, resistances):
        assert abs(expected - actual) < 1e-10

# Testing that the ValueError is raised if a zero or negative area are given.

def test_zero_area():
    """Tests to make sure expected error happens when zero input is given"""
    with pytest.raises(ValueError, match="The area entered must be above zero."):
        list(resistance_generator(1.68e-8, 0, [1, 2]))
# Testing that the ValueError is raised if the user input no length values.

def test_empty_length():
    """Tests to make sure expected error is given when no inputs are given"""
    with pytest.raises(ValueError, match="You must input some value for the length."):
        list(resistance_generator(1.68e-8, 1e-6, []))
