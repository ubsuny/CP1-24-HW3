import unittest
import Coulumb

class TestElectricForce(unittest.TestCase):


    def test_positive_charge(self):

        result = Coulumb.calculate_electric_force(1e-6, 1e-6, 0.1)  # Example charges and distance
        expected = Coulumb.COULOMBS_CONSTANT * abs(1e-6 * 1e-6) / (0.1**2)
        self.assertAlmostEqual(result, expected)

    def test_negative_charge(self):

        result = Coulumb.calculate_electric_force(-1e-6, -1e-6, 0.1)  # Both charges negative
        expected = Coulumb.COULOMBS_CONSTANT * abs(-1e-6 * -1e-6) / (0.1**2)
        self.assertAlmostEqual(result, expected)

    def test_zero_distance(self):

        result = Coulumb.calculate_electric_force(-1e-6, -1e-6, 0)
        expected = print("Distance between charges cannot be zero.")  # Expected behavior for zero distance
        self.assertEqual(result, expected)

    def test_zero_charge(self):

        result = Coulumb.calculate_electric_force(0, 1e-6, 0.1)  # One charge is zero
        expected = 0  # Electric force should be zero
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
