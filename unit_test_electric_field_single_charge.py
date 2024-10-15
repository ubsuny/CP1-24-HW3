"""This unit test script includes a test for a single charge function, for net field from multiple charges, to ensure error handling works correctly for zero distances"""

import unittest
from electric_field_due_to_single_charge import electric_field_single_charge, net_electric_field

class TestElectricField(unittest.TestCase):
    
    def test_single_charge(self):
        """Test the electric field for a single charge at a specific distance."""
        self.assertAlmostEqual(electric_field_single_charge(1e-6, 1), 8.99e3)  # Expected value: 8.99 kN/C
    
    def test_multiple_charges(self):
        """Test the net electric field for multiple charges at a point."""
        charges_positions = [(1e-6, (1, 0)), (-2e-6, (-1, 0)), (1e-6, (0, 1))]
        point_position = (0, 0)
        net_field = net_electric_field(charges_positions, point_position)
        self.assertAlmostEqual(net_field, 2.697e4, delta=1e2)  # Approximation of expected result

    def test_zero_distance(self):
        """Test if the function raises an error when distance is zero."""
        with self.assertRaises(ValueError):
            electric_field_single_charge(1e-6, 0)

if __name__ == '__main__':
    unittest.main()
