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

