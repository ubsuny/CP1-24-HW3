"""This unit test script includes a test for a single charge function, for net field from multiple charges, to ensure error handling works correctly for zero distances"""

import unittest
from electric_field_due_to_single_charge import electric_field_single_charge, net_electric_field

class TestElectricField(unittest.TestCase):
    """
    Unit tests for electric_field_single_charge and net_electric_field functions.
    """

    def test_electric_field_single_charge(self):
        """
        Test electric field due to a single charge at a specific distance.
        """
        # Test with a charge at (1, 0) and calculate the field at (0, 0)
        charge = 1e-6  # 1 microcoulomb
        r_vector = (-1, 0)  # point at (0, 0) and charge at (1, 0)
        result = electric_field_single_charge(charge, r_vector)

        # Expected result for Ex and Ey
        expected_ex = -8.99e3  # N/C in the x-direction
        expected_ey = 0.0      # N/C in the y-direction

        # Check that the results match expected values
        self.assertAlmostEqual(result[0], expected_ex, places=2)
        self.assertAlmostEqual(result[1], expected_ey, places=2)

    def test_net_electric_field(self):
        """
        Test net electric field due to multiple charges.
        """
        # Three charges: +1e-6 C at (1, 0), -2e-6 C at (-1, 0), +1e-6 C at (0, 1)
        charges_positions = [(1e-6, (1, 0)), (-2e-6, (-1, 0)), (1e-6, (0, 1))]
        point_position = (0, 0)
        
        # Call net_electric_field function
        result = net_electric_field(charges_positions, point_position)

        # Expected result: Net electric field vector at the origin (calculated previously)
        expected_ex = 2.70e4  # N/C in the x-direction
        expected_ey = 8.99e3  # N/C in the y-direction

        # Check that the results match expected values
        self.assertAlmostEqual(result[0], expected_ex, places=2)
        self.assertAlmostEqual(result[1], expected_ey, places=2)

if __name__ == '__main__':
    unittest.main()

