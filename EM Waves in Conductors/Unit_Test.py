"""
The unit tests for functions in EM_In_Conductors.py are included.
"""

import unittest
import math
from EM_In_Conductors import (omega, calculate_properties, k_kappa)

class TestElectromagneticProperties(unittest.TestCase):
    """
    TestElectromagneticProperties is a unit test class for verifying that the calculations
    related to electromagnetic properties of metals from the code are indeed correct.

    This class contains tests for the following functions:
    - omega.
    - k_kappa.
    - calculate_properties.

    In addition, it also tests for the validation of error handling for invalid metals and negative wavelength values.
    
    Each test case ensures that the methods behave as expected under normal and 
    edge-case conditions.
    """

    def test_omega(self):
        """Test omega calculation with a known value."""
        wavelength = 1e-6 
        expected_omega = 2 * math.pi * c / wavelength
        self.assertAlmostEqual(omega(wavelength), expected_omega)

    def test_calculate_properties_gold(self):
        """Test properties calculation for Gold."""
        wavelength = 1e-6 
        metal = "Gold"
        
        k, kappa, skin_depth, phase_shift, characteristic_time = calculate_properties(wavelength, metal)
        
        self.assertGreater(k, 0)
        self.assertGreater(kappa, 0)
        self.assertGreater(skin_depth, 0)
        self.assertGreater(phase_shift, 0)
        self.assertGreater(characteristic_time, 0)
    
    def test_calculate_properties_silver(self):
        """Test properties calculation for Silver."""
        wavelength = 5e-7
        metal_type = "Silver"
        
        k, kappa, skin_depth, phase_shift, characteristic_time = calculate_properties(wavelength, metal)
        
        self.assertGreater(k, 0)
        self.assertGreater(kappa, 0)
        self.assertGreater(skin_depth, 0)
        self.assertGreater(phase_shift, 0)
        self.assertGreater(characteristic_time, 0)

    def test_k_kappa(self):
        """Test k_kappa calculation with known values."""
        omega_value = 2 * math.pi * c / 1e-6 
        sigma = 5.95e7  # Conductivity for Copper
        epsilon = epsilon_0
        mu = mu_0
        
        expected_k, expected_kappa = self.calculate_expected_k_kappa(omega_value, sigma, epsilon, mu)
        
        k, kappa = k_kappa(omega_value, sigma, epsilon, mu)
        
        self.assertAlmostEqual(k, expected_k, places=5)
        self.assertAlmostEqual(kappa, expected_kappa, places=5)

    def calculate_expected_k_kappa(self, omega, sigma, epsilon, mu):
        """Helper function to calculate expected k and kappa."""
        term = (sigma / (epsilon * omega)) ** 2
        factor = omega * math.sqrt(epsilon * mu / 2)
        
        k = factor * math.sqrt(math.sqrt(1 + term) + 1)   
        kappa = factor * math.sqrt(math.sqrt(1 + term) - 1)
        
        return k, kappa

    def test_invalid_metal(self):
        """Test with an invalid metal type."""
        wavelength = 1e-6
        with self.assertRaises(KeyError):
            calculate_properties(wavelength, "InvalidMetal")

    def test_negative_wavelength(self):
        """Test with a negative wavelength."""
        wavelength = -1e-6
        with self.assertRaises(ValueError):
            calculate_properties(wavelength, "Gold")
          
if __name__ == "__main__":
    unittest.main()
