# Import the function from the module where it's defined
from PhysicsModule import *

epsilon_0 = 8.854*(10**(-12))  # Permittivity of free space

# Define some test cases
def test_sigma1():
    # Test case 1
    R = 1.0  
    V = 100.0  
    # Expected surface charge density: sigma = epsilon_0 * (V / R)
    expected_result = epsilon_0 * (V / R)
    assert sigma(R, V, epsilon_0) == expected_result, "Test case 1 failed"
    print("Test1 passed")

def test_sigma2():    
    # Test case 2:
    R = 2.0
    V = 200.0
    expected_result = epsilon_0 * (V / R)
    assert sigma(R, V) == expected_result, "Test case 2 failed"
    print("Test1 passed")
    
def test_sigma3():
    # Test case 3: Zero potential (V = 0 should give sigma = 0)
    R = 1.0
    V = 0.0
    expected_result = 0.0
    assert sigma(R, V) == expected_result, "Test case 3 failed (V = 0)"
    print("Test3 passed")

def test_sigma4():
    # Test case 4: Large radius (R)
    R = 1*(10**6)  # Large radius
    V = 100.0
    expected_result = epsilon_0 * (V / R)
    assert sigma(R, V, epsilon_0) == expected_result, "Test case 4 failed (large R)"
    print("Test4 passed")
    
# Call the test function
if __name__ == "__main__":
    test_sigma1()
    test_sigma2()
    test_sigma3()
    test_sigma4()