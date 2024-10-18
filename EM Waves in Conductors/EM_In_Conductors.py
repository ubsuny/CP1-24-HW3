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

