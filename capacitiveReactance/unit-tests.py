import unittest
import math
from reactance import inductive_reactance, capacitive_reactance, calculate_wire_inductance, calculate_wire_capacitance, total_impedance_and_phase

class TestImpedanceCalculations(unittest.TestCase):
    """
    Unit tests for impedance, reactance, and phase angle calculations.
    """

    def test_inductive_reactance(self):
        """
        Test the inductive reactance calculation for a known frequency and inductance.
        Formula: X_L = 2 * pi * f * L
        """
        frequency = 60  # Hz
        inductance = 0.01  # H
        expected = 2 * math.pi * frequency * inductance
        self.assertAlmostEqual(inductive_reactance(frequency, inductance), expected, places=6)

    def test_capacitive_reactance(self):
        """
        Test the capacitive reactance calculation for a known frequency and capacitance.
        Formula: X_C = 1 / (2 * pi * f * C)
        """
        frequency = 60  # Hz
        capacitance = 1e-6  # F
        expected = 1 / (2 * math.pi * frequency * capacitance)
        self.assertAlmostEqual(capacitive_reactance(frequency, capacitance), expected, places=6)

    def test_calculate_wire_inductance(self):
        """
        Test the calculation of parasitic inductance for a wire with a known length and radius.
        Uses the formula: L ≈ (μ0 / (2π)) * ln(2 * length / radius)
        """
        length = 1.0  # meters
        radius = 0.001  # meters (1 mm)
        expected = (4 * math.pi * 1e-7 / (2 * math.pi)) * math.log(2 * length / radius)
        self.assertAlmostEqual(calculate_wire_inductance(length, radius), expected, places=12)

    def test_calculate_wire_capacitance(self):
        """
        Test the calculation of parasitic capacitance for a wire with a known length and radius.
        Uses the formula: C ≈ (2π * ε0 * length) / ln(2 * length / radius)
        """
        length = 1.0  # meters
        radius = 0.001  # meters (1 mm)
        expected = (2 * math.pi * 8.854e-12 * length) / math.log(2 * length / radius)
        self.assertAlmostEqual(calculate_wire_capacitance(length, radius), expected, places=12)

    def test_total_impedance_and_phase(self):
        """
        Test the total impedance and phase angle calculation for known component values.
        The expected values are dynamically computed using the same formulas as in the main code.
        """
        # Given values for components
        frequency = 60  # Hz
        inductance = 0.01  # H
        capacitance = 1e-6  # F
        resistance = 10  # Ohms
        length = 1.0  # meters
        radius = 0.001  # meters (1 mm)

        # Perform the calculation using the main function
        total_Z, phase_angle = total_impedance_and_phase(frequency, inductance, capacitance, resistance, length, radius)

        # Now, compute the expected values dynamically using the same formulas as in the main function.
        # This includes the wire's parasitic effects.
        X_L = inductive_reactance(frequency, inductance)
        X_C = capacitive_reactance(frequency, capacitance)

        wire_L = calculate_wire_inductance(length, radius)
        wire_C = calculate_wire_capacitance(length, radius)

        wire_X_L = inductive_reactance(frequency, wire_L)
        wire_X_C = capacitive_reactance(frequency, wire_C)

        # Total reactance considering both components and wire effects
        total_reactance = (X_L + wire_X_L) - (X_C + wire_X_C)

        # Expected total impedance
        expected_Z = math.sqrt(resistance**2 + total_reactance**2)

        # Expected phase angle
        expected_phase_angle = math.degrees(math.atan(total_reactance / resistance))

        # Print values for debugging if necessary
        print(f"Computed Total Impedance: {total_Z}")
        print(f"Expected Total Impedance: {expected_Z}")
        print(f"Computed Phase Angle: {phase_angle}")
        print(f"Expected Phase Angle: {expected_phase_angle}")

        # Assert that computed and expected values match
        self.assertAlmostEqual(total_Z, expected_Z, places=6)
        self.assertAlmostEqual(phase_angle, expected_phase_angle, places=6)



    def test_invalid_resistance(self):
        """
        Test that the system raises a ValueError for negative resistance, as resistance must be non-negative.
        """
        with self.assertRaises(ValueError):
            total_impedance_and_phase(60, 0.01, 1e-6, -10, 1.0, 0.001)

    def test_invalid_inductance(self):
        """
        Test that the system raises a ValueError for non-positive inductance.
        """
        with self.assertRaises(ValueError):
            inductive_reactance(60, -0.01)  # Negative inductance should raise an error

    def test_invalid_capacitance(self):
        """
        Test that the system raises a ValueError for non-positive capacitance.
        """
        with self.assertRaises(ValueError):
            capacitive_reactance(60, -1e-6)  # Negative capacitance should raise an error

    def test_invalid_wire_properties(self):
        """
        Test that the system raises a ValueError for invalid wire length or radius (non-positive values).
        """
        with self.assertRaises(ValueError):
            calculate_wire_inductance(-1, 0.001)  # Negative wire length
        with self.assertRaises(ValueError):
            calculate_wire_inductance(1, -0.001)  # Negative wire radius

# Run the tests
if __name__ == "__main__":
    unittest.main()
