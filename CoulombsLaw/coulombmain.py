import coulomb

# Conversion factor: 1 C = 1,000,000 µC
coulomb_to_microcoulomb = 10**-6


def main():
    """
    Main function to calculate and display the electric force between two point charges using Coulomb's law.
    
    This function:
    1. Prompts the user to input the values of two charges (in microcoulombs) and the distance between them (in centimeters).
    2. Converts the charges from microcoulombs to coulombs.
    3. Converts the distance from centimeters to meters.
    4. Calls the Coulomb's law function to compute the electric force between the charges.
    5. Displays the converted charges (in coulombs) and the calculated force (in newtons).
    """
    

    # Get the first charge (q1) from the user, in coulombs.
    q1 = float(input("Enter charge q1 (in microcoulombs): "))
    
    # Get the second charge (q2) from the user, in coulombs.
    q2 = float(input("Enter charge q2 (in microcoulombs): "))

    # Use map and lambda to convert to microcoulombs
    q1, q2 = map(lambda q: q * coulomb_to_microcoulomb, [q1, q2])

    # Get the distance (r) between the charges from the user, in meters.
    r = float(input("Enter distance r (in centimeters): "))
    
    # Calculate the electric force between the two charges using Coulomb's law.
    result = coulomb.calculate_electric_force(q1, q2, r)
    
    # Display the converted charges
    print(f"q1 in microcoulombs: {q1} µC")
    print(f"q2 in microcoulombs: {q2} µC")

    # Display the calculated electric force in newtons (N).
    print("The electric force between q1 and q2 is ", result, "N")


if __name__ == "__main__":
    main()