# test_capacitance.py

import math
from capacitance import capacitance

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
    
    print("All tests passed.")

# Run the unit test
if __name__ == "__main__":
    test_capacitance()