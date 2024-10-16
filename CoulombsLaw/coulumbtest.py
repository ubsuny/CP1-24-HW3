import unittest
import coulomb

# Test class for Coulomb's law function
class TestElectricForce(unittest.TestCase):
    """
    Test class for the Coulomb's law function in the 'coulomb' module.
    
    This class contains unit tests to validate the calculation of the electric force
    between two point charges using various test cases:
    - Positive charges
    - Negative charges
    - Zero distance
    - Zero charge
    """


    def test_positive_charge(self):
        """
        Test the electric force between two positive charges.
        
        This test checks if the calculated force is correct when both charges are positive.
        The charges are given in coulombs and the distance in meters.
        """

        result = coulomb.calculate_electric_force(1e-6, 1e-6, 0.1)  # Example charges and distance
        expected = coulomb.COULOMBS_CONSTANT * abs(1e-6 * 1e-6) / (0.1**2)
        self.assertAlmostEqual(result, expected)

    def test_negative_charge(self):
        """
        Test the electric force between two negative charges.
        
        This test checks if the calculated force is correct when both charges are negative.
        The charges are given in coulombs and the distance in meters.
        """

        result = coulomb.calculate_electric_force(-1e-6, -1e-6, 0.1)  # Both charges negative
        expected = coulomb.COULOMBS_CONSTANT * abs(-1e-6 * -1e-6) / (0.1**2)
        self.assertAlmostEqual(result, expected)

    def test_zero_distance(self):
        """
        Test the behavior of the function when the distance between charges is zero.
        
        This test checks if the function properly handles the case where the distance is zero,
        which would lead to an undefined result in Coulomb's law. It should return an error message.
        """

        result = coulomb.calculate_electric_force(-1e-6, -1e-6, 0)
        expected = print("Distance between charges cannot be zero.")  # Expected behavior for zero distance
        self.assertEqual(result, expected)

    def test_zero_charge(self):
        """
        Test the electric force when one of the charges is zero.
        
        This test checks if the calculated force is zero when one of the charges is zero,
        as the force should be zero when any charge is zero.
        """

        result = coulomb.calculate_electric_force(0, 1e-6, 0.1)  # One charge is zero
        expected = 0  # Electric force should be zero
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
