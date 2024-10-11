import math
import random

# Constants
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
    """
    if frequency <= 0 or inductance <= 0:
        raise ValueError("Frequency and inductance must be positive values.")

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
    """
    if frequency <= 0 or capacitance <= 0:
        raise ValueError("Frequency and capacitance must be positive values.")

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

def total_impedance_and_phase(frequency: float, inductance: float, capacitance: float, resistance: float, length: float, radius: float) -> (float, float):
    """
    Calculate the total impedance (Z) and phase angle (φ) of a circuit, including resistance and wire properties.

    Z = sqrt(R^2 + (X_L + X_{L_wire} - (X_C + X_{C_wire}))^2)
    φ = arctan(total reactance / resistance)

    Parameters:
    frequency (float): The frequency of the AC signal in Hertz (Hz).
    inductance (float): The inductance of the inductor in Henrys (H).
    capacitance (float): The capacitance of the capacitor in Farads (F).
    resistance (float): The resistance of the resistor in Ohms (Ω).
    length (float): The length of the wire in meters.
    radius (float): The radius of the wire in meters.

    Returns:
    float: The total impedance in Ohms (Ω).
    float: The phase angle in degrees (°).
    """
    if resistance < 0:
        raise ValueError("Resistance must be non-negative.")

    # Calculate inductive and capacitive reactance for components
    X_L = inductive_reactance(frequency, inductance)
    X_C = capacitive_reactance(frequency, capacitance)

    # Calculate parasitic inductance and capacitance for the wire
    wire_L = calculate_wire_inductance(length, radius)
    wire_C = calculate_wire_capacitance(length, radius)

    # Calculate reactance due to wire properties
    wire_X_L = inductive_reactance(frequency, wire_L)
    wire_X_C = capacitive_reactance(frequency, wire_C)

    # Calculate total reactance (X = (X_L + X_{L_wire}) - (X_C + X_{C_wire}))
    total_reactance = (X_L + wire_X_L) - (X_C + wire_X_C)

    # Calculate total impedance Z = sqrt(R^2 + total_reactance^2)
    Z = math.sqrt(resistance**2 + total_reactance**2)

    # Calculate phase angle φ = arctan(total_reactance / resistance)
    phase_angle_radians = math.atan(total_reactance / resistance)
    phase_angle_degrees = math.degrees(phase_angle_radians)

    return Z, phase_angle_degrees

def main(randomize: bool = False):
    """
    Example usage of the total_impedance_and_phase function.
    If 'randomize' is set to True, random values for the variables will be generated.

    Parameters:
    randomize (bool): If True, random values will be used for the variables.
    """
    if randomize:
        # Generate random values within reasonable physical ranges
        frequency = random.uniform(50, 50000)         # Hertz (50 Hz to 5 kHz)
        inductance = random.uniform(1e-6, 1e0)      # Henrys (1 microhenry to 1 millihenry)
        capacitance = random.uniform(1e-12, 1e0)    # Farads (1 picofarad to 1 microfarad)
        resistance = random.uniform(1, 1000)          # Ohms (1 to 100 ohms)
        length = random.uniform(0.1, 1000)             # Meters (0.1 to 10 meters)
        radius = random.uniform(0.0001, 1.0)        # Meters (0.1 mm to 10 mm)

    else:
        # Example fixed parameters
        frequency = 60.0       # Hertz (Hz), common AC line frequency
        inductance = 0.01      # Henrys (H)
        capacitance = 1e-6     # Farads (F)
        resistance = 10.0      # Ohms (Ω)
        length = 1.0           # Meters
        radius = 0.001         # Meters (1 mm)

    try:
        # Print out the system values
        print(30*"-")
        print(f"System Values:")
        print(f"Frequency: {frequency:.2f} Hz")
        print(f"Inductance: {inductance:.6f} H")
        print(f"Capacitance: {capacitance:.12f} F")
        print(f"Resistance: {resistance:.2f} Ω")
        print(f"Wire Length: {length:.2f} m")
        print(f"Wire Radius: {radius:.4f} m")

        print(20*"=")
        print("Computed Values")
        print(20*"=")
        # Calculate total impedance and phase angle
        total_Z, phase_angle = total_impedance_and_phase(frequency, inductance, capacitance, resistance, length, radius)
        print(f"Total impedance of the circuit: {total_Z:.2f} Ohms")
        print(f"Phase angle: {phase_angle:.2f}°")

        # Check whether the current lags or leads the voltage
        if phase_angle > 0:
            print("The current lags behind the voltage (inductive circuit).")
        elif phase_angle < 0:
            print("The current leads the voltage (capacitive circuit).")
        else:
            print("The current and voltage are in phase (purely resistive circuit).")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Change 'randomize' to True for random values
    print(30*"-")
    print("Static Configuration:")
    main()
    print("\n")
    print(30*"-")
    print("Randomized Configuration:")
    main(randomize=True)
