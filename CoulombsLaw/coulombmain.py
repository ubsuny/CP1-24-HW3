"""
This module provides functions for calculating the electric force between two point charges
using Coulomb's law and simulating how this force evolves over time as the distance between
the charges changes.

The module includes:
1. A constant for converting microcoulombs to coulombs.
2. A function `time_evolution` for simulating the electric force over time as the distance
   between the charges changes.
3. A `main` function that interacts with the user to input charges, distance, and other parameters,
   and calculates the electric force, displaying the results over time.
"""

import coulomb

# Conversion factor: 1 C = 1,000,000 µC
COULOMB_TO_MICROCOULOMB = 10**-6

def time_evolution(q1, q2, r_initial, r_change_rate, time_steps):
    """
    Simulates the time evolution of the electric force between two charges over a series of time steps.

    Parameters:
    q1: The charge of the first object (in Coulombs).
    q2: The charge of the second object (in Coulombs).
    r_initial: The initial distance between the two charges (in centimeters).
    r_change_rate: The rate of change of the distance between the charges per time step (in centimeters).
    time_steps: The total number of time steps for the simulation.

    Returns:
    A list containing the time step and the corresponding electric force (in Newtons).

    The function prints the distance and electric force at each time step, and returns a list of the force values 
    over time as the distance between the charges evolves.
    """
    forces_over_time = []
    r = r_initial

    for t in range(time_steps):
        force = coulomb.calculate_electric_force(q1, q2, r)
        forces_over_time.append((t, force))
        print(f"At time {t}: distance = {r} cm, force = {force} N")
        r += r_change_rate  # Update r for the next time step

    return forces_over_time

def main():
    """
    Main function to calculate and display the electric force between two point charges.
    Also simulates the time evolution of the force as the distance changes.

    The user is prompted to input the charges (in microcoulombs), the initial distance (in centimeters),
    the rate of change of distance per time step, and the number of time steps to simulate.
    """
    # Get the first charge (q1) from the user, in microcoulombs.
    q1 = int(input("Enter charge q1 (in microcoulombs): "))
    # Get the second charge (q2) from the user, in microcoulombs.
    q2 = int(input("Enter charge q2 (in microcoulombs): "))

    # Convert charges to coulombs
    q1, q2 = map(lambda q: q * COULOMB_TO_MICROCOULOMB, [q1, q2])

    # Get the initial distance (r) between the charges from the user, in centimeters.
    r_initial = float(input("Enter initial distance r (in centimeters): "))
    # Get the rate at which the distance changes over time
    r_change_rate = float(input("Enter rate of change of distance per time step (in centimeters): "))
    # Get the number of time steps
    time_steps = int(input("Enter number of time steps: "))

    # Simulate the time evolution of the electric force
    time_evolution(q1, q2, r_initial, r_change_rate, time_steps)

if __name__ == "__main__":
    main()
