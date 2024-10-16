'''
test_spherical_capacitor.py

Unit tests for the spherical_capacitor.py module.

Tests range from basic logic to verifying expected outcomes.
'''

import unittest
from spherical_capacitor import calculate_spherical_capacitance, EPSILON_0
import numpy as np


class TestSphericalCapacitor(unittest.TestCase):
    '''
    Class with various different unit tests.
    Tests include:
    - Capacitance calculation with no dielectric between shells.
    - Capacitance when inner radius approaches zero.
    - Capacitance when outer radius is much larger than inner radius.
    '''

    def test_no_dielectric(self):
        '''
        Test the capacitance calculation for a spherical capacitor 
        with no dielectric between shells.
        '''
        inner_r = 0.05  # Inner radius in meters
        outer_r = 0.1   # Outer radius in meters

        # No dielectric layers
        dielectrics = []

        capacitance = calculate_spherical_capacitance(inner_r, outer_r, dielectrics)

        # Expected capacitance in vacuum
        expected_capacitance = 4 * np.pi * EPSILON_0 * (inner_r * outer_r) / (outer_r - inner_r)

        self.assertAlmostEqual(capacitance, expected_capacitance, places=12)

    def test_water_between_spheres(self):
        """
        Test capacitance with water as the dielectric between spheres.
        Water has a relative permittivity of 80.1.
        """
        inner_r = 0.05  # Inner sphere radius (meters)
        outer_r = 0.1   # Outer sphere radius (meters)

        dielectrics = [
            {'epsilon_r': 80.1, 'inner_r': inner_r, 'outer_r': outer_r}
        ]

        capacitance = calculate_spherical_capacitance(inner_r, outer_r, dielectrics)

        # Expected capacitance calculation
        expected_cap = 4 * np.pi * EPSILON_0 * 80.1 * (inner_r * outer_r) / (outer_r - inner_r)

        self.assertAlmostEqual(capacitance, expected_cap, places=12)

    def test_half_air_half_diamond(self):
        """
        Test capacitance with half the gap filled with air (er = 1.0)
          and the other half with diamond (er = 5.8).
        """
        inner_r = 0.05  # Inner sphere radius (meters)
        mid_r = 0.075  # Radius between air and diamond
        outer_r = 0.1    # Outer sphere radius (meters)

        dielectrics = [
            {'epsilon_r': 1.0, 'inner_r': inner_r, 'outer_r': mid_r},  # Air
            {'epsilon_r': 5.8, 'inner_r': mid_r, 'outer_r': outer_r}  # Diamond
        ]

        capacitance = calculate_spherical_capacitance(inner_r, outer_r, dielectrics)

        # Calculate expected capacitance for each layer
        capacitance_air = 4 * np.pi * EPSILON_0 * 1.0 * (inner_r * mid_r) / (mid_r - inner_r)
        capacitance_di = 4 * np.pi * EPSILON_0 * 5.8 * (mid_r * outer_r) / (outer_r - mid_r)

        # Total capacitance is the reciprocal of the sum of reciprocals
        expected_capacitance = 1 / ((1 / capacitance_air) + (1 / capacitance_di))

        self.assertAlmostEqual(capacitance, expected_capacitance, places=12)

    def test_silicon_and_salt_layers(self):
        """
        Test capacitance with 1/5 of the gap filled with silicon (er = 11.7) 
        and the other 4/5 filled with salt (er = 5.9).
        """
        inner_r = 0.05  # Inner sphere radius (meters)
        middle_r = 0.06  # Boundary between silicon and salt
        outer_r = 0.1   # Outer sphere radius (meters)

        dielectrics = [
            {'epsilon_r': 11.7, 'inner_r': inner_r, 'outer_r': middle_r},
            {'epsilon_r': 5.9, 'inner_r': middle_r, 'outer_r': outer_r}
        ]

        capacitance = calculate_spherical_capacitance(inner_r, outer_r, dielectrics)

        # Calculate expected capacitance for each layer
        capacitance_si = 4 * np.pi * EPSILON_0 * 11.7 * (inner_r * middle_r) / (middle_r - inner_r)
        capacitance_na = 4 * np.pi * EPSILON_0 * 5.9 * (middle_r * outer_r) / (outer_r - middle_r)

        # Total capacitance is the reciprocal of the sum of reciprocals
        expected_capacitance = 1 / ((1 / capacitance_si) + (1 / capacitance_na))

        self.assertAlmostEqual(capacitance, expected_capacitance, places=12)

    def test_inner_r_approaches_zero(self):
        '''
        Test the capacitance calculation when the inner radius approaches zero.
        '''
        inner_r = 1e-6  # Inner radius approaching zero
        outer_r = 0.5   # Outer radius in meters

        dielectrics = []

        capacitance = calculate_spherical_capacitance(inner_r, outer_r, dielectrics)

        # Expected capacitance approaches 0
        expected_capacitance = 0

        self.assertAlmostEqual(capacitance, expected_capacitance, places=12)

    def test_outer_r_much_larger_than_inner(self):
        '''
        Test the capacitance calculation when the outer radius is much larger than the inner radius.
        '''
        inner_r = 0.05    # Inner radius in meters
        outer_r = 50.0    # Outer radius much larger than inner radius

        dielectrics = []

        capacitance = calculate_spherical_capacitance(inner_r, outer_r, dielectrics)

        # Expected capacitance approaches that of an isolated sphere
        expected_capacitance = 4 * np.pi * EPSILON_0 * inner_r

        self.assertAlmostEqual(capacitance, expected_capacitance, places=12)


if __name__ == '__main__':
    unittest.main()
