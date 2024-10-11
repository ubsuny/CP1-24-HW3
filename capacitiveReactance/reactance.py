import math

# Note: Type hinting syntax does not affect execution
def inductive_reactance(frequency: float, inductance: float) -> float:
    """
    Calculate the inductive reactance (X_L) for a given inductor.

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
    reactance = 2 * math.pi * frequency * inductance
    return reactance

# Note: Type hinting syntax does not affect execution
def capacitive_reactance(frequency: float, capacitance: float) -> float:
    """
    Calculate the capacitive reactance (X_C) for a given capacitor.

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
    reactance = 1 / (2 * math.pi * frequency * capacitance)
    return reactance

# NOTE: Type hinting syntax does not affect execution
def total_reactance(frequency: float, inductance: float, capacitance: float) -> float:
    """
    Calculate the total reactance of a simple AC circuit consisting of an inductor and a capacitor.

    Total reactance (X) is the difference between inductive reactance (X_L) and capacitive reactance (X_C):
    X = X_L - X_C

    Parameters:
    frequency (float): The frequency of the AC signal in Hertz (Hz).
    inductance (float): The inductance of the inductor in Henrys (H).
    capacitance (float): The capacitance of the capacitor in Farads (F).

    Returns:
    float: The total reactance in Ohms (Ω), which can be positive (net inductive) or negative (net capacitive).

    Raises:
    ValueError: If frequency, inductance, or capacitance is non-positive.
    """
    # Calculate inductive reactance
    X_L = inductive_reactance(frequency, inductance)

    # Calculate capacitive reactance
    X_C = capacitive_reactance(frequency, capacitance)

    # Calculate total reactance (X = X_L - X_C)
    total_X = X_L - X_C
    return total_X

def main():
    """
    Example usage of the total_reactance function.
    """
    # Example parameters
    frequency = 60.0  # Hertz (Hz), common AC line frequency
    inductance = 0.01  # 10 millihenrys (H)
    capacitance = 1e-6  # 1 microfarad (F)

    try:
        # Calculate total reactance
        total_X = total_reactance(frequency, inductance, capacitance)
        print(f"Total reactance of the circuit: {total_X:.2f} Ohms")

        # Check whether the reactance is inductive or capacitive
        if total_X > 0:
            print("The circuit is net inductive (inductive reactance is dominant).")
        elif total_X < 0:
            print("The circuit is net capacitive (capacitive reactance is dominant).")
        else:
            print("The circuit is in resonance (inductive and capacitive reactances cancel each other).")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
