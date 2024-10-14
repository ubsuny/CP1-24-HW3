#Python code for Magnetic field of wire
import math

def magnetic_field(I, d):
    """
    #Calculate the magnetic field around a long straight current-carrying wire.

    #Parameters:
    I (float): Current in amperes
    d (float): Distance from the wire in meters

    Returns:
    float: Magnetic field in teslas
    """
    mu_0 = 4 * math.pi * 10**-7  
    # Permeability of free space (T m/A)
    B = (mu_0 * I) / (2 * math.pi * d)  
    # Magnetic field formula
    return B

# Example used:
current = 10.0  
# Current in amperes
distances = (0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 100)   
# Distances in meters

# Calculate and print the magnetic field for each distance
for distance in distances:
    B_field = magnetic_field(current, distance)
    print(f"The magnetic field at {distance} m from a wire carrying {current} A is {B_field:.2e} T.")


#Python code for Magnetic field of wire Using Lambda function
import numpy as np
import matplotlib.pyplot as plt

# Constants
mu_0 = 4 * np.pi * 10**-7  # Permeability of free space (T m/A)

# Parameters
current = 10  # Current in amperes
# Use np.array to create an array of distances
distances = np.array([0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 100])  # Distances from 0.01 m to 100 m

# Lambda function to calculate magnetic field
magnetic_field = lambda I, r: (mu_0 * I) / (2 * np.pi * r)

# Calculate magnetic field values using map with the lambda function
fields = list(map(lambda r: magnetic_field(current, r), distances))

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(distances, fields)
plt.title('Magnetic Field Around a Straight Current-Carrying Wire')
plt.xlabel('Distance from the Wire (m)')
plt.ylabel('Magnetic Field (T)')
plt.grid(True)
plt.ylim(0, max(fields) * 1.1)
plt.xlim(0, 0.5)  # Limit x-axis to 0.5 to focus on the initial part of the curve
plt.show()





#Python code for Magnetic field of wire Using Generator function


import numpy as np
import matplotlib.pyplot as plt

# Constants
mu_0 = 4 * np.pi * 10**-7  # Permeability of free space (T m/A)

def magnetic_field_generator(current, distances):
    """Generator function to yield magnetic field values for given distances."""
    for r in distances:
        yield (mu_0 * current) / (2 * np.pi * r)

# Parameters
current = 10  # Current in amperes
# Corrected np.linspace usage:
# The third argument should be the number of samples (an integer)
# Here, we generate 100 points between 0.01 and 0.5
# Original: distances = np.linspace(0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 100)
distances = np.array([0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 100]) # This line was changed to match the intended behavior

# Create generator
field_generator = magnetic_field_generator(current, distances)

# Calculate magnetic field values
fields = list(field_generator)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(distances, fields)
plt.title('Magnetic Field Around a Straight Current-Carrying Wire')
plt.xlabel('Distance from the Wire (m)')
plt.ylabel('Magnetic Field (T)')
plt.grid(True)
plt.ylim(0, max(fields) * 1.1)
plt.xlim(0, 0.5)
plt.show()
