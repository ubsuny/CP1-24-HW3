import math

# Constants
mu_0 = 4 * math.pi * 1e-7  # Permeability of free space (H/m)
epsilon_0 = 8.854187817e-12  # Permittivity of free space (F/m)
c = 3e8  # Speed of light in vacuum (m/s)

# Metal dictionary with conductivity in S/m for each metal at 1 atm, 20 °C.
# Conductivity data from Handbook of Chemistry and Physics, 91st ed. (Boca Raton, Fla.: CRC Press, 2010)
metals = {"Gold": 4.52e7,
    "Aluminum": 3.77e7,
    "Mercury": 1.04e6,
    "Copper": 5.95e7, 
    "Silver": 6.3e7,  
    "Iron": 1.04e7,   
    "Nichrome": 9.26e5, 
    "Manganese": 6.94e5}

def omega(wavelength):
    """
    Calculate angular frequency from wavelength.

    Parameters:
        wavelength (float): The wavelength in meters.

    Returns:
        float: The angular frequency in radians per second.
    """
    return 2 * math.pi * c / wavelength

def calculate_properties(wavelength, metal_type):
    """
    Calculate electromagnetic properties based on wavelength and metal type.

    Parameters:
        wavelength (float): The wavelength in meters.
        metal_type (str): The type of metal (must be a key in the metals dictionary).

    Returns:
        tuple: A tuple containing:
            - k (float): Wave number (1/m).
            - kappa (float): Attenuation constant (1/m).
            - skin_depth (float): Skin depth in meters.
            - phase_shift (float): Phase shift in degrees.
            - characteristic_time (float): Characteristic time in seconds.
    """

    # Validate the wavelength
    if wavelength <= 0:
        raise ValueError("Wavelength must be a positive number.")

    # Get conductivity for the selected metal
    sigma = metals[metal_type]
    
    # Calculate angular frequency
    omega_value = omega(wavelength)
    
    def k_kappa(omega, sigma, epsilon, mu):  # This can be used to work out k and kappa in different media
        """
        Calculate wave number (k) and attenuation constant (kappa).

        Parameters:
            omega (float): Angular frequency.
            sigma (float): Conductivity of the metal.
            epsilon (float): Permittivity of medium.
            mu (float): Permeability of medium.

        Returns:
            tuple: A tuple containing:
                - k (float): Wave number (1/m).
                - kappa (float): Attenuation constant (1/m).
        """
        term = (sigma / (epsilon * omega)) ** 2
        factor = omega * math.sqrt(epsilon * mu / 2)
        
        # Griffiths D.J, Introduction to Electrodynamics (4th Ed) - Equation 9.126
        k = factor * math.sqrt(math.sqrt(1 + term) + 1)   
        kappa = factor * math.sqrt(math.sqrt(1 + term) - 1)
        
        
        return k, kappa

    # Compute k and kappa for FREE SPACE. Note that we can change our code here to include dielectrics
    k, kappa = k_kappa(omega_value, sigma, epsilon_0, mu_0)

    # Skin Depth (1/kappa)
    skin_depth = 1 / kappa

    # Phase shift (arctan(kappa/k) in degrees)
    phase_shift = math.degrees(math.atan(kappa / k))
    
    # Characteristic time calculation
    characteristic_time = epsilon_0 / sigma

    return k, kappa, skin_depth, phase_shift, characteristic_time

def main():
    """
    Main function to execute the program.

    It prompts the user for wavelengths and metal types, validates the input,
    calculates the electromagnetic properties for the valid combinations,
    and displays the results.
    """
    # Input: Wavelengths
    wavelengths_input = input("Enter free space wavelengths (comma-separated, in meters): ").split(",")
    
    # Convert wavelengths input (list of strings) to a list of floats using map
    wavelengths = list(map(float, wavelengths_input))
    
    # Input: Metal types
    metal_types = input("Enter metal types (comma-separated from 'Gold', 'Aluminum', 'Mercury', 'Copper', 'Silver', 'Iron', 'Nichrome', 'Manganese'): ").split(",")
    
    # Clean up the input by removing any whitespaces
    metal_types = [str(m.strip()) for m in metal_types]
    
    # Filter/Validate metal types
    filter_metal_types = filter(lambda m: m in metal_types and m in metals, metal_types)
    
    # Convert filter output to list
    valid_metal_types = list(filter_metal_types)

    # Compute the results for each combination of wavelength and metal type using list comprehension
    results = [(wavelength, metal_type, *calculate_properties(wavelength, metal_type))
               for wavelength in wavelengths
               for metal_type in valid_metal_types]

    # Display the results
    for wavelength, metal_type, k, kappa, skin_depth, phase_shift, characteristic_time in results:
        print("-----------------------------------------------------------------------------------------------------")
        print("Results for " + metal_type + " with wavelength " + str(wavelength) + " meters:")
        print("Wave number (k): " + str(k) + " 1/m")
        print("Attenuation constant (kappa): " + str(kappa) + " 1/m")
        print("Skin Depth: " +  str(skin_depth) + " meters")
        print("Phase Shift: " + str(phase_shift) + " degrees")
        print("Characteristic Time: " + str(characteristic_time) + " seconds")
        print("-----------------------------------------------------------------------------------------------------")
