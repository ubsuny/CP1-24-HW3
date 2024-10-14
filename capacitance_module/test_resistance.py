# test_resistance.py

import math
from resistance import resistance, batch_resistances

def test_resistance():
    """
    Unit test for the resistance function.
    """
    # Test case 1
    length = 1.0
    area = 0.01
    resistivity = 1.68e-8  # Ohm meters for copper
    expected = resistivity * (length / area)
    assert math.isclose(resistance(length, area, resistivity), expected), f"Expected {expected}, but got {resistance(length, area, resistivity)}"

    # Test batch resistances
    lengths = [1.0, 2.0, 0.5]
    areas = [0.01, 0.02, 0.005]
    resistivities = [1.68e-8, 2.82e-8, 1.05e-8]  # Example resistivities for copper, aluminum, silver
    expected_batch = [resistivity * (l / A) for l, A, resistivity in zip(lengths, areas, resistivities)]
    assert batch_resistances(lengths, areas, resistivities) == expected_batch, "Batch resistance test failed"

    print("All resistance tests passed.")

# Run the unit test
if __name__ == "__main__":
    test_resistance()