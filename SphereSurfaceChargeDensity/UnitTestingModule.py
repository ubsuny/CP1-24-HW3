"""
This module is to test for the surface charge density of a conducting spherical shell of radius (R) held at constant potential (V).
"""

# Import the function from the module where it's defined
from PhysicsModule import *

# Permittivity of free space
Epsilon_0 = 8.854*(10**(-12))

# Define some test cases
def test_sigma():
    """
    A function that tests for different cases two of which are limiting scenarios (namely, the last two cases [for V = 0, and for large R])
    Parameters: None
    Returns: either returns messages for the first encountered failed test or prints "All tests passed"
    """
    R = [1.0, 2.0, 1.0, 1*(10**6)]
    V = [100.0, 200.0, 0.0, 100.0]
    expected_results = [Epsilon_0 * (V[i] / R[i]) for i in range(len(V))] # List-comprehensions
    for i in range(len(V)):
        assert sigma(R[i], V[i], Epsilon_0) == expected_results[i], f"Test case {i} failed"
    print("All tests passed")
    
# Call the test function
if __name__ == "__main__":
    test_sigma()