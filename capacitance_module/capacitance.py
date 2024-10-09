# capacitance.py

# Constant for permittivity of free space
epsilon_0 = 8.854e-12  # F/m

def capacitance(area, distance):
    """
    Calculate the capacitance of a parallel plate capacitor.

    Parameters:
    area (float): Area of the plate in square meters.
    distance (float): Distance between the plates in meters.

    Returns:
    float: Capacitance in farads.
    """
    return epsilon_0 * (area / distance)

# Test the function with example values
if __name__ == "__main__":
    A = 1.0  # Area in square meters
    d = 0.01  # Distance in meters
    print(f"Capacitance: {capacitance(A, d)} F")
