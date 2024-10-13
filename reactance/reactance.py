import math
import random

# Constants
MU_0 = 4 * math.pi * 1e-7  # Permeability of free space (H/m)
EPSILON_0 = 8.854e-12      # Permittivity of free space (F/m)


def inductive_reactance(frequency, inductance):
    """
    Calculate the inductive reactance (X_L) for a given inductor or wire's inductive property.
    If frequency is zero, inductive reactance is zero.
    """
    if frequency == 0:    # If frequency is 0
        return 0          # don't divide by it, just return 0
    reactance = 2 * math.pi * frequency * inductance
    return reactance


def capacitive_reactance(frequency, capacitance):
    """
    Calculate the capacitive reactance (X_C) for a given capacitor or wire's capacitive property.
    If frequency is zero, capacitive reactance is considered infinite.
    """
    if frequency == 0:        # If frequency is 0
        return float('inf')   # don't divide by it, just return 0
    reactance = 1 / (2 * math.pi * frequency * capacitance)  # compute reactance
    return reactance                                         # and return it


def calculate_wire_inductance(length, radius):
    """
    Calculate the parasitic inductance of a straight wire.
    """
    # compute the inductance for this wire segment
    inductance = (MU_0 / (2 * math.pi)) * math.log(2 * length / radius)
    return inductance


def calculate_wire_capacitance(length, radius):
    """
    Calculate the parasitic capacitance of a straight wire.
    """
    capacitance = (2 * math.pi * EPSILON_0 * length) / math.log(2 * length / radius)
    return capacitance


def total_impedance_and_phase(frequency, inductance, capacitance, resistance, length, radius):
    """
    Calculate the total impedance (Z) and phase angle (φ) of a circuit, including resistance and wire properties.
    """
    # Calculate component inductive and capacitive reactance
    X_L = inductive_reactance(frequency, inductance)
    X_C = capacitive_reactance(frequency, capacitance)

    # Calculate wire parasitic inductance and capacitance
    wire_L = calculate_wire_inductance(length, radius)
    wire_C = calculate_wire_capacitance(length, radius)

    # Calculate parasitic reactance for the wire
    wire_X_L = inductive_reactance(frequency, wire_L)
    wire_X_C = capacitive_reactance(frequency, wire_C)

    # Total reactance is the sum of inductive reactance (including wire) minus capacitive reactance (including wire)
    total_reactance = (X_L + wire_X_L) - (X_C + wire_X_C)

    # Total impedance calculation
    total_impedance = math.sqrt(resistance**2 + total_reactance**2)

    # Phase angle calculation
    phase_angle_radians = math.atan(total_reactance / resistance)
    phase_angle_degrees = math.degrees(phase_angle_radians)

    return total_impedance, phase_angle_degrees


def compute_segments(generator_dict, num_segments):
    """
    Compute the impedance and phase angle for a series of segments along a wire.
    Store the computed values in lists for later plotting.
    """
    impedance_list = []
    phase_angle_list = []

    # use an iterate over each segment
    for i in range(num_segments):

        # print lambda functions and their computed values for this segment
        print(f"Segment {i+1}:")                        # print the segment number
        for key, func in generator_dict.items():        # use a dict comprehension
            value = func(i)                             # get a value from the lambda function
            print(f"  {key}: {value}")                  # print the key and value

        # Calculate the current length for this segment using the lambda function for length
        # current_length refers to the length of current segment of wire
        current_length = generator_dict["length"](i)

        # Call total_impedance_and_phase for each segment using the generator functions
        total_Z, phase_angle = total_impedance_and_phase(
            generator_dict["frequency"](i),
            generator_dict["inductance"](i),
            generator_dict["capacitance"](i),
            generator_dict["resistance"](i),
            current_length,
            generator_dict["radius"](i)
        )

        # Append the results to the lists
        impedance_list.append(total_Z)
        phase_angle_list.append(phase_angle)

    # return the two lists
    return impedance_list, phase_angle_list


def main(randomize=False, num_segments=10, dynamic=False):
    """
    Example usage of the total_impedance_and_phase function.

    If 'randomize' is set to True, random values for the variables will be generated.
    Compute values for multiple segments along the wire.

    If 'dynamic' is True, the values will be generated as functions of the segment index (i).
    """
    # Dynamic behavior with lambda functions based on segment index (i)
    if dynamic:
        generator_dict = {
            "frequency": lambda i: 50 + i**2,  # Frequency increases as i^2
            "inductance": lambda i: 0.01 + 0.0001 * i,  # Inductance changes linearly with i
            "capacitance": lambda i: 1e-6 + 1e-12 * i**2,  # Capacitance grows with i^2
            "resistance": lambda i: 10 + 0.1 * i,  # Resistance increases linearly
            "length": lambda i: 1.0 + 0.1 * i,  # Length changes linearly with i
            "radius": lambda i: 0.001 + 1e-5 * i  # Radius increases linearly
        }
    # Random behavior with random values for each segment
    elif randomize:
        generator_dict = {
            "frequency": lambda i: random.uniform(50, 5000),
            "inductance": lambda i: random.uniform(1e-6, 1e0),
            "capacitance": lambda i: random.uniform(1e-12, 1e0),
            "resistance": lambda i: random.uniform(1, 1000),
            "length": lambda i: random.uniform(0.1, 10),  # Now uses 'i' if dynamic
            "radius": lambda i: random.uniform(0.0001, 0.01)
        }
    # Static configuration with fixed values for all segments
    else:
        generator_dict = {
            "frequency": lambda i: 60.0,
            "inductance": lambda i: 0.01,
            "capacitance": lambda i: 1e-6,
            "resistance": lambda i: 10.0,
            "length": lambda i: 1.0,  # Fetch constant length
            "radius": lambda i: 0.001
        }

    # Compute the impedance and phase angle for each segment
    impedance_list, phase_angle_list = compute_segments(generator_dict, num_segments)

    # Print the computed results for each segment
    print("Computed Impedance and Phase Angle for each segment:")
    for i, (impedance, phase_angle) in enumerate(zip(impedance_list, phase_angle_list)):
        print(f"Segment {i+1}: Impedance = {impedance:.2f} Ohms, Phase Angle = {phase_angle:.2f}°")


if __name__ == "__main__":
    # Static configuration
    main(num_segments=10)
    # Randomized configuration
    print("\nRandomized Configuration:")
    main(randomize=True, num_segments=10)
    # Dynamic configuration
    print("\nDynamic Configuration:")
    main(dynamic=True, num_segments=10)
