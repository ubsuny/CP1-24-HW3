"""
This script calculates the total resistance of resistors connected in parallel.
It follows these steps:
1. Defines a function to calculate the total parallel resistance using the reciprocals of the resistances.
2. Allows the user to input resistance values dynamically.
3. Computes and displays the total parallel resistance.
"""
from functools import reduce
# Step 1: Define the function to calculate total parallel resistance
def calculate_parallel_resistance(resistances):
    """
    Calculate total resistance in a parallel circuit.
    resistances: an iterable of resistance values.
    Returns: the total resistance as a float.
    """
    # Use map with lambda to calculate the reciprocals of the resistances
    reciprocals = map(lambda r: 1/r, resistances)
    # Use reduce with lambda to sum the reciprocals
    total_reciprocal = reduce(lambda x, y: x + y, reciprocals)
    # Return the inverse of the total reciprocal
    return 1 / total_reciprocal
# Step 2: Define a function to input resistances and calculate total parallel resistance
def input_resistances_and_calculate(num_resistances, calc_func):
    """
    Take the number of resistances and calculate the total resistance using a passed function.
    num_resistances: Number of resistances in parallel.
    calc_func: Function that calculates total resistance.
    """
    # Use a generator to dynamically input resistance values
    resistances = (float(input(f"Enter resistance in ohms {i+1}: ")) for i in range(num_resistances))
    # Call the resistance calculation function (calc_func) to compute the total resistance
    total_resistance = calc_func(resistances)
    return total_resistance
# Step 3: Main function to interact with the user and demonstrate the usage
"""
Main function to prompt the user for the number of resistances,
input resistance values, and calculate total parallel resistance.
"""
def main():
    # Ask user for the number of resistances
    num_resistances = int(input("Enter the number of resistances in parallel: "))
    # Call the function to input resistances and calculate the total parallel resistance
    total_resistance = input_resistances_and_calculate(num_resistances, calculate_parallel_resistance)
    # Print the calculated total resistance
    print(f"Total parallel resistance: {total_resistance:.2f} ohms")
# Run the main function
if __name__ == "__main__":
    main()
