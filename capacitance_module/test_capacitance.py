# test_capacitance.py

import math
from capacitance import capacitance, batch_capacitances

def test_capacitance():
    """
    Unit test for the capacitance function.
    """
    epsilon_0 = 8.854e-12

    # Test case 1
    A = 1.0
    d = 0.01
    expected = epsilon_0 * (A / d)
    assert math.isclose(capacitance(A, d), expected), f"Expected {expected}, but got {capacitance(A, d)}"

    # Test batch capacitances
    areas = [1.0, 2.0, 0.5]
    distances = [0.01, 0.02, 0.005]
    expected_batch = [epsilon_0 * (A / d) for A, d in zip(areas, distances)]
    assert batch_capacitances(areas, distances) == expected_batch, "Batch capacitance test failed"

    print("All capacitance tests passed.")

# Run the unit test
if __name__ == "__main__":
    test_capacitance()
