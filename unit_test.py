'''
test_spherical_capacitor.py

Unit tests for the spherical_capacitor.py module.

Tests include:
- Capacitance calculation with no dielectric between shells.
- Capacitance when inner radius approaches zero.
- Capacitance when outer radius is much larger than inner radius.
'''

import unittest
from spherical_capacitor import calculate_spherical_capacitance, EPSILON_0
import numpy as np


class TestSphericalCapacitor(unittest.TestCase):

    def test_no_dielectric(self):
        '''
        Test the capacitance calculation for a spherical capacitor with no dielectric between shells.
        '''
        a = 0.05  # Inner radius in meters
        b = 0.1   # Outer radius in meters

        # No dielectric layers
        dielectrics = []

        C = calculate_spherical_capacitance(a, b, dielectrics)

        # Expected capacitance in vacuum
        expected_C = 4 * np.pi * EPSILON_0 * (a * b) / (b - a)

        self.assertAlmostEqual(C, expected_C, places=12)

    def test_inner_radius_approaches_zero(self):
        '''
        Test the capacitance calculation when the inner radius approaches zero.
        '''
        a = 1e-6  # Inner radius approaching zero
        b = 0.5   # Outer radius in meters

        dielectrics = []

        C = calculate_spherical_capacitance(a, b, dielectrics)

        # Expected capacitance approaches 0
        expected_C = 0

        self.assertAlmostEqual(C, expected_C, places=12)

    def test_outer_radius_much_larger_than_inner(self):
        '''
        Test the capacitance calculation when the outer radius is much larger than the inner radius.
        '''
        a = 0.05    # Inner radius in meters
        b = 50.0    # Outer radius much larger than inner radius

        dielectrics = []

        C = calculate_spherical_capacitance(a, b, dielectrics)

        # Expected capacitance approaches that of an isolated sphere
        expected_C = 4 * np.pi * EPSILON_0 * a

        self.assertAlmostEqual(C, expected_C, places=12)


if __name__ == '__main__':
    unittest.main()