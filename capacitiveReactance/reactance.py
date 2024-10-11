import math

# Define some relevant constants
MU_0 = 4 * math.pi * 1e-7  # Permeability of free space (H/m)
EPSILON_0 = 8.854e-12      # Permittivity of free space (F/m)

def inductive_reactance(frequency: float, inductance: float) -> float:
    """
    Calculate the inductive reactance (X_L) for a given inductor or wire's inductive property.

    X_L = 2 * pi * f * L

    Parameters:
    frequency (float): The frequency of the AC signal in Hertz (Hz).
    inductance (float): The inductance of the inductor in Henrys (H).

    Returns:
    float: The inductive reactance in Ohms (Ω).

    Raises:
    ValueError: If frequency or inductance is non-positive.
    """
    if frequency <= 0 or inductance <= 0:
        raise ValueError("Frequency and inductance must be positive values.")

    # Calculate inductive reactance
    return 2 * math.pi * frequency * inductance

def capacitive_reactance(frequency: float, capacitance: float) -> float:
    """
    Calculate the capacitive reactance (X_C) for a given capacitor or wire's capacitive property.

    X_C = 1 / (2 * pi * f * C)

    Parameters:
    frequency (float): The frequency of the AC signal in Hertz (Hz).
    capacitance (float): The capacitance of the capacitor in Farads (F).

    Returns:
    float: The capacitive reactance in Ohms (Ω).

    Raises:
    ValueError: If frequency or capacitance is non-positive.
    """
    if frequency <= 0 or capacitance <= 0:
        raise ValueError("Frequency and capacitance must be positive values.")

    # Calculate capacitive reactance
    return 1 / (2 * math.pi * frequency * capacitance)

def calculate_wire_inductance(length: float, radius: float) -> float:
    """
    Calculate the parasitic inductance of a straight wire.

    L ≈ (μ0 / (2π)) * ln(2 * length / radius)

    Parameters:
    length (float): The length of the wire in meters.
    radius (float): The radius of the wire in meters.

    Returns:
    float: The parasitic inductance in Henrys (H).
    """
    if length <= 0 or radius <= 0:
        raise ValueError("Length and radius must be positive values.")

    return (MU_0 / (2 * math.pi)) * math.log(2 * length / radius)

def calculate_wire_capacitance(length: float, radius: float) -> float:
    """
    Calculate the parasitic capacitance of a straight wire.

    C ≈ (2π * ε0 * length) / ln(2 * length / radius)

    Parameters:
    length (float): The length of the wire in meters.
    radius (float): The radius of the wire in meters.

    Returns:
    float: The parasitic capacitance in Farads (F).
    """
    if length <= 0 or radius <= 0:
        raise ValueError("Length and radius must be positive values.")

    return (2 * math.pi * EPSILON_0 * length) / math.log(2 * length / radius)

def total_reactance_with_wire(frequency: float, inductance: float, capacitance: float, length: float, radius: float) -> float:
    """
    Calculate the total reactance of a circuit, including both the component and wire properties.

    Total reactance (X) is the difference between inductive reactance (X_L) and capacitive reactance (X_C):
    X = (X_L + wire_inductive_reactance) - (X_C + wire_capacitive_reactance)

    Parameters:
    frequency (float): The frequency of the AC signal in Hertz (Hz).
    inductance (float): The inductance of the inductor in Henrys (H).
    capacitance (float): The capacitance of the capacitor in Farads (F).
    length (float): The length of the wire in meters.
    radius (float): The radius of the wire in meters.

    Returns:
    float: The total reactance in Ohms (Ω).
    """
    # Calculate inductive and capacitive reactance for components
    X_L = inductive_reactance(frequency, inductance)
    X_C = capacitive_reactance(frequency, capacitance)

    # Calculate parasitic inductance and capacitance for the wire
    wire_L = calculate_wire_inductance(length, radius)
    wire_C = calculate_wire_capacitance(length, radius)

    # Calculate reactance due to wire properties
    wire_X_L = inductive_reactance(frequency, wire_L)
    wire_X_C = capacitive_reactance(frequency, wire_C)

    # Calculate total reactance including wire properties
    total_X = (X_L + wire_X_L) - (X_C + wire_X_C)
    return total_X

def main():
    """
    Example usage of the total_reactance_with_wire function.
    """
    # Example parameters for components
    frequency = 60.0  # Hertz (Hz), common AC line frequency
    inductance = 0.01  # 10 millihenrys (H)
    capacitance = 1e-6  # 1 microfarad (F)

    # Example wire properties
    length = 1.0  # Length of the wire in meters
    radius = 0.001  # Radius of the wire in meters (1 mm)

    try:
        # Calculate total reactance with wire properties
        total_X = total_reactance_with_wire(frequency, inductance, capacitance, length, radius)
        print(f"Total reactance of the circuit with wire properties: {total_X:.2f} Ohms")

        # Check whether the reactance is inductive or capacitive
        if total_X > 0:
            print("The circuit is net inductive (inductive reactance is dominant).")
            print("Current lags behind the voltage.")
        elif total_X < 0:
            print("The circuit is net capacitive (capacitive reactance is dominant).")
            print("Current leads the voltage.")
        else:
            print("The circuit is in resonance (inductive and capacitive reactances cancel each other).")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
