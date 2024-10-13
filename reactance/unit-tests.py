import unittest
import math
from reactance import (
    inductive_reactance,
    capacitive_reactance,
    calculate_wire_inductance,
    calculate_wire_capacitance,
    total_impedance_and_phase,
    compute_segments
)

class TestReactanceCalculations(unittest.TestCase):

    def setUp(self):
        # Static configuration values for testing
        self.generator_dict_static = {
            "frequency": lambda i: 60.0,
            "inductance": lambda i: 0.01,
            "capacitance": lambda i: 1e-6,
            "resistance": lambda i: 10.0,
            "length": lambda i: 1.0,
            "radius": lambda i: 0.001
        }
        self.num_segments = 5

    def test_sanity_check(self):
        """Test a simple, ideal case for sanity check."""
        # Use simple values for the test
        generator_dict_simple = {
            "frequency": lambda i: 1.0,  # 1 Hz frequency
            "inductance": lambda i: 1.0,  # 1 H inductance
            "capacitance": lambda i: 1.0,  # 1 F capacitance
            "resistance": lambda i: 1.0,  # 1 Ohm resistance
            "length": lambda i: 1.0,  # 1 m length
            "radius": lambda i: 1.0  # 1 m radius (arbitrary, but simple)
        }

        # Compute impedance and phase for this simple setup
        impedance_list, phase_angle_list = compute_segments(generator_dict_simple, self.num_segments)

        # Simple check: with these values, reactance and impedance should be within a reasonable range
        for impedance, phase_angle in zip(impedance_list, phase_angle_list):
            self.assertGreater(impedance, 0)  # Impedance should be positive
            self.assertTrue(-90 <= phase_angle <= 90)  # Phase angle should be within [-90, 90] degrees

            # Print for sanity check (optional, but you can enable this during debug)
            # {impedance: .2f}  digits after the decimal point.
            print(f"Sanity check: Impedance = {impedance:.2f} Ohms, Phase Angle = {phase_angle:.2f}°")

    def test_inductive_reactance(self):
        """Test calculation of inductive reactance"""
        frequency = 60.0
        inductance = 0.01
        expected_reactance = 2 * math.pi * frequency * inductance
        self.assertAlmostEqual(inductive_reactance(frequency, inductance), expected_reactance)

    def test_capacitive_reactance(self):
        """Test calculation of capacitive reactance"""
        frequency = 60.0
        capacitance = 1e-6
        expected_reactance = 1 / (2 * math.pi * frequency * capacitance)
        self.assertAlmostEqual(capacitive_reactance(frequency, capacitance), expected_reactance)

    def test_wire_inductance(self):
        """Test calculation of parasitic inductance for a wire"""
        length = 1.0
        radius = 0.001
        expected_inductance = (4 * math.pi * 1e-7 / (2 * math.pi)) * math.log(2 * length / radius)
        self.assertAlmostEqual(calculate_wire_inductance(length, radius), expected_inductance)

    def test_wire_capacitance(self):
        """Test calculation of parasitic capacitance for a wire"""
        length = 1.0
        radius = 0.001
        expected_capacitance = (2 * math.pi * 8.854e-12 * length) / math.log(2 * length / radius)
        self.assertAlmostEqual(calculate_wire_capacitance(length, radius), expected_capacitance)

    def test_total_impedance_and_phase(self):
        """Test calculation of total impedance and phase angle"""
        frequency = 60.0
        inductance = 0.01
        capacitance = 1e-6
        resistance = 10.0
        length = 1.0
        radius = 0.001

        # Expected impedance and phase angle
        total_Z, phase_angle = total_impedance_and_phase(frequency, inductance, capacitance, resistance, length, radius)

        # Assert impedance is a positive value
        self.assertGreater(total_Z, 0)

        # Assert phase angle is within reasonable bounds (-90 to 90 degrees)
        self.assertTrue(-90 <= phase_angle <= 90)

    def test_compute_segments_static(self):
        """Test compute_segments function with static values"""
        # Use the static configuration generator dictionary
        impedance_list, phase_angle_list = compute_segments(self.generator_dict_static, self.num_segments)

        # Test that the correct number of segments are calculated
        self.assertEqual(len(impedance_list), self.num_segments)
        self.assertEqual(len(phase_angle_list), self.num_segments)

        # Test that impedance and phase angle are reasonable numbers
        for impedance, phase_angle in zip(impedance_list, phase_angle_list):
            self.assertGreater(impedance, 0)  # Impedance should always be positive
            self.assertTrue(-90 <= phase_angle <= 90)  # Phase angle should be within [-90, 90] degrees

    def test_zero_frequency(self):
        """Test the edge case where frequency is zero"""
        generator_dict_zero_freq = {
            "frequency": lambda i: 0.0,
            "inductance": lambda i: 0.01,
            "capacitance": lambda i: 1e-6,
            "resistance": lambda i: 10.0,
            "length": lambda i: 1.0,
            "radius": lambda i: 0.001
        }
        impedance_list, phase_angle_list = compute_segments(generator_dict_zero_freq, self.num_segments)

        for impedance, phase_angle in zip(impedance_list, phase_angle_list):
            self.assertGreater(impedance, 0)  # Impedance should still be positive
            self.assertTrue(-90 <= phase_angle <= 90)  # Phase angle should still be valid

    def test_very_small_inductance_capacitance(self):
        """Test with very small inductance and capacitance"""
        generator_dict_small_values = {
            "frequency": lambda i: 60.0,
            "inductance": lambda i: 1e-12,
            "capacitance": lambda i: 1e-12,
            "resistance": lambda i: 10.0,
            "length": lambda i: 1.0,
            "radius": lambda i: 0.001
        }
        impedance_list, phase_angle_list = compute_segments(generator_dict_small_values, self.num_segments)

        # Test that impedance and phase angle are calculated for small values
        for impedance, phase_angle in zip(impedance_list, phase_angle_list):
            self.assertGreater(impedance, 0)
            self.assertTrue(-90 <= phase_angle <= 90)

if __name__ == "__main__":
    unittest.main()
