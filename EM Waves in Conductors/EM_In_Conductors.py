"""
This is a console program that outputs the electromagnetic properties of various metals based on input wavelengths
in free space. It utilizes the conductivity values for 8 different metals at standard conditions (1 atm, 20 °C).

The following properties are computed for a given pair of wavelength and metal:

- Wave number (k)
- Attenuation constant (kappa)
- Skin depth
- Phase shift
- Characteristic time

Refer to the EM_In_Conductors.md file for a detailed discussion of the aforementioned quantities.

The user is prompted to enter wavelengths and metal names, and the program outputs the calculated
properties for each valid combination.
"""

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

def calculate_properties(wavelength, metal):
    """
    Calculate electromagnetic properties based on wavelength and metal.

    Parameters:
        wavelength (float): The wavelength in meters.
        metal (str): The name of metal (must be a key in the metals dictionary).

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
    sigma = metals[metal]
    
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

    It prompts the user for wavelengths and metal names, validates the input,
    calculates the electromagnetic properties for the valid combinations,
    and displays the results.
    """
    # Input: Wavelengths
    wavelengths_input = input("Enter free space wavelengths (comma-separated, in meters): ").split(",")
    
    # Convert wavelengths input (list of strings) to a list of floats using map
    wavelengths = list(map(float, wavelengths_input))
    
    # Input: Metal Names
    metals = input("Enter metal names (comma-separated from 'Gold', 'Aluminum', 'Mercury', 'Copper', 'Silver', 'Iron', 'Nichrome', 'Manganese'): ").split(",")
    
    # Clean up the input by removing any whitespaces
    metals = [str(m.strip()) for m in metals]
    
    # Filter/Validate metal names
    filter_metals = filter(lambda m: m in metals and m in metals, metals)
    
    # Convert filter output to list
    valid_metals = list(filter_metals)

    # Compute the results for each combination of wavelength and metal using list comprehension
    results = [(wavelength, metal, *calculate_properties(wavelength, metal))
               for wavelength in wavelengths
               for metal in valid_metals]

    # Display the results
    for wavelength, metal, k, kappa, skin_depth, phase_shift, characteristic_time in results:
        print("-----------------------------------------------------------------------------------------------------")
        print("Results for " + metal + " with wavelength " + str(wavelength) + " meters:")
        print("Wave number (k): " + str(k) + " 1/m")
        print("Attenuation constant (kappa): " + str(kappa) + " 1/m")
        print("Skin Depth: " +  str(skin_depth) + " meters")
        print("Phase Shift: " + str(phase_shift) + " degrees")
        print("Characteristic Time: " + str(characteristic_time) + " seconds")
        print("-----------------------------------------------------------------------------------------------------")

if __name__ == "__main__":
    main()
