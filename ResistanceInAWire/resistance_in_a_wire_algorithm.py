""" This contains an algorithm module that find the resistance in a wire
 using functional programming. """

# Define a lamba function to calculate the resistance of a wire using resitivity as rho,
# length as l and cross-section area of wire as A.

calculate_resistance = lambda rho, length, area: rho * length / area

# Check during geneerator if user input invalid values.

def resistance_generator(rho, area, lengths):
    """Generator function that creates resistance values of a wire of different lengths"""

    if area <= 0:
        raise ValueError("The area entered must be above zero.")

    if not lengths:
        raise ValueError("You must input some value for the length.")

    for length in lengths:
        yield calculate_resistance(rho, length, area)

# Adding user inputs for values of rho, length, and area.

if __name__ == "__main__":
    try:
        # Asking user above for input values.
        # Asking for resistivity.

        rho = float(input(" Please enter the resistivity of your wire in ohm meters.: "))

        # Asking for area and checking to make sure it is not zero.

        area = float(input("Please enter the cross-sectional area of your wire in meters square.:"))
        if area <= 0:
            raise ValueError("The area entered must be above zero.")

        # Asking for lengths of wire in a list.

        lengths_input = input("Please enter in the lengths of wire in meters separated by spaces.:")

        # Convert lengths input into a list of floats.
        # And ensuring the lengths are separated by a space.

        lengths = list(map(float, lengths_input.split()))

        # Checking to make sure the user provided at least one input for the length

        if not lengths:
            raise ValueError("You must input some value for the length.")

        # Create the generator.

        resistances = resistance_generator(rho, area, lengths)

        # Iterate over the genrator and print the resistance for the lengths given.
        for length, resistance in zip(lengths, resistances):
            print(f" Resistance for length {length} m: {resistance:.6f} ohms ")

    except ValueError as ve:
        print("Invalid input you have been naughty!")
