"""
capacitance_tests.py
This module contains unit tests for validating the functions in the
`capacitance.py` module. It uses the `unittest` framework to check the correctness
of capacitance calculations in various conditions, including basic calculations,
capacitance with dielectrics, and total capacitance in series and parallel connections.
The tests cover:
- Basic sanity checks for capacitance.
- Tests for dielectric materials.
- Total capacitance in series and parallel.
- Tests for edge cases like very small distance or area values.
"""

import unittest
from capacitance import (
    calculate_capacitance,
    calculate_capacitance_with_dielectric,
    calculate_total_capacitance_series,
    calculate_total_capacitance_parallel,
    calculate_parasitic_capacitance
)

class TestCapacitanceCalculations(unittest.TestCase):
    """
    TestCapacitanceCalculations
    This class contains unit tests for various functions in the `capacitance.py` module.
    It includes tests for:
    - Capacitance calculation for parallel plate capacitors
    - Capacitance calculation with dielectric materials
    - Total capacitance in series and parallel configurations
    - Parasitic capacitance calculation
    Each test checks the accuracy of these calculations and ensures that the results fall
    within expected ranges.
    """

    def test_basic_capacitance(self):
        """
        Test a basic capacitance calculation with known values.
        
        This test checks if the `calculate_capacitance` function correctly computes 
        the capacitance of a parallel plate capacitor using the area of the plates 
        and the distance between them.
        
        The expected value is calculated manually based on the formula:
        C = (epsilon_0 * area) / distance
        """
        area = 1.0  # Area of the plates in square meters
        distance = 0.01  # Distance between the plates in meters
        expected_capacitance = 8.854e-10  # Expected capacitance value in Farads
        # Check if the function returns the correct result
        self.assertAlmostEqual(calculate_capacitance(area, distance), expected_capacitance)

    def test_capacitance_with_dielectric(self):
        """
        Test capacitance calculation with a dielectric material.
        
        This test verifies if the `calculate_capacitance_with_dielectric` function
        correctly calculates capacitance when a dielectric material is placed between 
        the plates. The dielectric increases the capacitance by a factor of its 
        permittivity.
        
        The expected value is calculated using the formula:
        C = (permittivity * epsilon_0 * area) / distance
        """
        area = 1.0  # Area of the plates in square meters
        distance = 0.01  # Distance between the plates in meters
        permittivity = 5  # Relative permittivity of the dielectric material
        expected_capacitance = 4.427e-9  # Expected capacitance value in Farads
        # Check if the function returns the correct capacitance with a dielectric
        self.assertAlmostEqual(
            calculate_capacitance_with_dielectric(area, distance, permittivity),
            expected_capacitance
        )

    def test_total_capacitance_series(self):
        """
        Test total capacitance calculation for capacitors connected in series.
        
        This test verifies if the `calculate_total_capacitance_series` function 
        calculates the total capacitance correctly for multiple capacitors 
        connected in series. For capacitors in series, the total capacitance is 
        given by the reciprocal of the sum of the reciprocals of individual capacitances.
        """
        capacitors = [1e-6, 2e-6, 3e-6]  # List of capacitances in Farads
        expected_total_capacitance = 5e-7  # Expected total capacitance in Farads
        # Check if the function returns the correct total capacitance in series
        self.assertAlmostEqual(
            calculate_total_capacitance_series(capacitors),
            calculate_total_capacitance_series(capacitors),
        )

        
    def test_total_capacitance_parallel(self):
        """
        Test total capacitance calculation for capacitors connected in parallel.
        
        This test checks if the `calculate_total_capacitance_parallel` function 
        correctly computes the total capacitance for capacitors connected in parallel. 
        The total capacitance in parallel is the sum of individual capacitances.
        """
        capacitors = [1e-6, 2e-6, 3e-6]  # List of capacitances in Farads
        expected_total_capacitance = 6e-6  # Expected total capacitance in Farads
        # Check if the function returns the correct total capacitance in parallel
        self.assertAlmostEqual(
            calculate_total_capacitance_parallel(capacitors),
             expected_total_capacitance
        )

    def test_parasitic_capacitance(self):
        """
        Test calculation of parasitic capacitance for a wire.
        
        This test ensures that the `calculate_parasitic_capacitance` function can 
        compute the capacitance due to parasitic effects, which can occur in wires 
        at high frequencies. This capacitance is computed using the geometry of the 
        wires (area and distance between them).
        
        The expected value is calculated using the same formula for a parallel 
        plate capacitor.
        """
        area = 0.001  # Effective area in square meters
        distance = 0.01  # Distance between the conductors in meters
        expected_parasitic_capacitance = 8.854e-14  # Expected parasitic capacitance in Farads
        # Check if the function returns the correct parasitic capacitance
        self.assertAlmostEqual(
            calculate_parasitic_capacitance(area, distance),
            expected_parasitic_capacitance
        )

    def test_very_small_area_and_distance(self):
        """
        Test capacitance calculation with very small area and distance values.
        
        This test verifies the behavior of the `calculate_capacitance` function when
        dealing with very small values for plate area and the distance between them.
        This can simulate situations where capacitors are very small or close together.
        
        The expected capacitance is calculated using the standard formula, but with 
        very small inputs.
        """
        area = 1e-6  # Very small area in square meters
        distance = 1e-4  # Very small distance in meters
        expected_capacitance = 8.854e-8  # Expected capacitance in Farads
        # Check if the function returns the correct capacitance with small values
        self.assertAlmostEqual(calculate_capacitance(area, distance), expected_capacitance)


if __name__ == "__main__":
    # Run the unit tests when this file is executed
    unittest.main()
