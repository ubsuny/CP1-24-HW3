"""
This module is to test for the surface charge density
of a conducting spherical shell of radius (R) held at constant potential (V).
"""

# Import the function from the module where it's defined
from physics_module import sigma

# Permittivity of free space
EPSILON_0 = 8.854*(10**(-12))

# Define some test cases
def test_sigma():
    """
    A function that tests for different cases
    two of which are limiting scenarios
    (namely, the last two cases [for V = 0, and for large R])
    
    Parameters: None
    
    Returns:
    either returns messages for the first encountered failed test
    or prints "All tests passed"
    """
    radii = [1.0, 2.0, 1.0, 1*(10**6)]
    potentials = [100.0, 200.0, 0.0, 100.0]
    # The map function
    calculated_results = map(sigma, radii, potentials)
    # List comprehensions
    expected_results = [EPSILON_0 * (potentials[i] / radii[i]) for i in range(len(radii))]
    for i in range(len(radii)):
        assert next(calculated_results) == expected_results[i], f"Test case {i} failed"
    print("All tests passed")

# Call the test function
test_sigma()
