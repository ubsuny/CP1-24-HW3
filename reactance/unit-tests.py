"""
unit-tests.py

This module contains unit tests for validating the functions in the
`reactance.py` module.It uses the `unittest` framework to check calculations
related to inductive and capacitive reactance, parasitic inductance and
capacitance in wires, and the total impedance and phase angle in AC circuits.

The tests cover:
- Basic sanity checks for reactance and impedance.
- Tests for edge cases such as zero frequency and very small values.
"""

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
    """
    TestReactanceCalculations

    This class contains unit tests for various functions in the `reactance.py`
    module.
    It includes tests for:
    - Inductive reactance
    - Capacitive reactance
    - Parasitic reactance in wires (inductance and capacitance)
    - Total impedance and phase calculations
    - Edge cases like zero frequency and small inductance/capacitance

    Each test checks the accuracy of these calculations and ensures that the
    results
    fall within expected ranges.
    """
    def setUp(self):
        # Static configuration values for testing
        self.generator_dict_static = {
            "frequency": lambda i: 1.0,
            "inductance": lambda i: 1.0,
            "capacitance": lambda i: 1.0,
            "resistance": lambda i: 1.0,
            "length": lambda i: 1.0,
            "radius": lambda i: 1.0
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
        iList, pal = compute_segments(generator_dict_simple, self.num_segments)

        # Simple check: with these values, reactance and impedance
        # should be within a reasonable range
        for impedance, phase_angle in zip(iList, pal):
            # Impedance should be positive
            self.assertGreater(impedance, 0)
            # Phase angle should be within [-90, 90] degrees
            self.assertTrue(-90 <= phase_angle <= 90)

            # Print for sanity check
            # {impedance: .2f}  digits after the decimal point.
            print(f"Sanity check: Impedance = {impedance:.2f} Ohms")
            print(f"Phase Angle = {phase_angle:.2f}°")

    def test_inductive_reactance(self):
        """Test calculation of inductive reactance"""
        frequency = 60.0
        inductance = 0.01
        er = 2 * math.pi * frequency * inductance
        self.assertAlmostEqual(inductive_reactance(frequency, inductance), er)

    def test_capacitive_reactance(self):
        """Test calculation of capacitive reactance"""
        frequency = 60.0
        capa = 1e-6
        er = 1 / (2 * math.pi * frequency * capa)
        self.assertAlmostEqual(capacitive_reactance(frequency, capa), er)

    def test_wire_inductance(self):
        """Test calculation of parasitic inductance for a wire"""
        length = 1.0
        radius = 0.001
        ei_f = (4 * math.pi * 1e-7 / (2 * math.pi))
        ei = ei_f * math.log(2 * length / radius)
        self.assertAlmostEqual(calculate_wire_inductance(length, radius), ei)

    def test_wire_capacitance(self):
        """Test calculation of parasitic capacitance for a wire"""
        length = 1.0
        radius = 0.001
        ec = (2 * math.pi * 8.854e-12 * length) / math.log(2 * length / radius)
        self.assertAlmostEqual(calculate_wire_capacitance(length, radius), ec)

    def test_total_impedance_and_phase(self):
        """Test calculation of total impedance and phase angle"""
        tip_dict = {
            'f': 60.0,
            'indc': 0.01,
            'capa': 1e-6,
            'resistance': 10.0,
            'length': 1.0,
            'radius': 0.001
        }

        # Expected impedance and phase angle
        totalZ, phaseAngle = total_impedance_and_phase(tip_dict)

        # Assert impedance is a positive value
        self.assertGreater(totalZ, 0)

        # Assert phase angle is within reasonable bounds (-90 to 90 degrees)
        self.assertTrue(-90 <= phaseAngle <= 90)

    def test_compute_segments_static(self):
        """Test compute_segments function with static values"""
        # Use the static configuration generator dictionary
        il, p = compute_segments(self.generator_dict_static, self.num_segments)

        # Test that the correct number of segments are calculated
        self.assertEqual(len(il), self.num_segments)
        self.assertEqual(len(p), self.num_segments)

        # Test that impedance and phase angle are reasonable numbers
        for impedance, phase_angle in zip(il, p):
            # Impedance should  positive
            self.assertGreater(impedance, 0)
            # Should be within [-90, 90] degrees
            self.assertTrue(-90 <= phase_angle <= 90)

    def test_zero_frequency(self):
        """Test the edge case where frequency is zero"""
        gdzf = {
            "frequency": lambda i: 0.0,
            "inductance": lambda i: 0.01,
            "capacitance": lambda i: 1e-6,
            "resistance": lambda i: 10.0,
            "length": lambda i: 1.0,
            "radius": lambda i: 0.001
        }
        il, pal = compute_segments(gdzf, self.num_segments)

        for impedance, phase_angle in zip(il, pal):
            # Impedance should still be positive
            self.assertGreater(impedance, 0)
            # Phase angle should still be valid
            self.assertTrue(-90 <= phase_angle <= 90)

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
        i, p = compute_segments(generator_dict_small_values, self.num_segments)

        # Test that impedance and phase angle are calculated for small values
        for impedance, phase_angle in zip(i, p):
            self.assertGreater(impedance, 0)
            self.assertTrue(-90 <= phase_angle <= 90)


if __name__ == "__main__":
    unittest.main()
