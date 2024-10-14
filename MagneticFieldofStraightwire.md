# Documentation

## Magnetic Field of Straight wire

It is understood that a moving charge or current generates a magnetic field. A long straight wire carrying a current I is 
shown in diagram below. The presence of current in the wire creates a magnetic field around it which consist of concentric
circles. 
![Screenshot 2024-10-13 164423](https://github.com/user-attachments/assets/25840c22-e22b-402f-86fb-426b548127b3)

The strength of magnetic field, B, can be found at a distance r away from the wire by the equation below:
$\displaystyle{B}=\frac{{\mu_{{0}}{I}}}{{{2}\pi{r}}}$
where, $\displaystyle\mu_{{0}}$ is a constant known as permeability of free space and has the 
value $\displaystyle\mu_{{0}}={4}\pi\cdot{10}^{ -{{7}}}{T}\cdot\frac{m}{{A}}$
It should be noted that the distance r must be measured perpendicular to the wire.
So, The magnetic field produced by a long, straight wire consists of concentric circles centered around the wire, 
with the direction of the field determined by the right-hand rule: point your thumb in the direction of the current, 
and your fingers will curl in the direction of the magnetic field at any point around the wire; the field strength is
inversely proportional to the distance from the wire.
Key Points: 
1. Shape of field lines: Concentric circles around the wire.
2. Direction determination: Right-hand rule - point your thumb in the direction of the current, your fingers curl in 
the direction of the magnetic field.
3. Strength dependence: The magnetic field strength decreases as the distance from the wire increases


#Documentation for Code:

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



import unittest
class Test_calculate_magnetic_field(unittest.TestCase):
    def test_calculate_magnetic_field(self):
        # Define a list of lengths of distances
        d = [0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 100]
        # Define the current
        I = 10.0

        # Calculate the expected magnetic field
        expected_magnetic_field = [2.00e-04, 2.00e-05, 1.00e-05, 6.67e-06, 5.00e-06, 4.00e-06, 2.00e-08]

        # Use the magnetic_field() function to calculate the magnetic field
        # Correctly apply magnetic_field to each distance in d using a list comprehension:
        actual_magnetic_field = [magnetic_field(I, distance) for distance in d]  

        # Assert that the actual magnetic fields are equal to the expected magnetic fields
        # Using assertAlmostEqual for floating-point comparisons to avoid precision issues
        for i in range(len(d)):
            self.assertAlmostEqual(actual_magnetic_field[i], expected_magnetic_field[i], places=7) 

# Run the tests without exiting the kernel in a Jupyter environment
# if __name__ == '__main__':
#   unittest.main(argv=['first-arg-is-ignored'], exit=False) # if in jupyter notebook

# If running as a standalone script, use:
if __name__ == '__main__':
    unittest.main()

    ##Result of Code:
# Python code 
The magnetic field at 0.01 m from a wire carrying 10.0 A is 2.00e-04 T.

The magnetic field at 0.1 m from a wire carrying 10.0 A is 2.00e-05 T.

The magnetic field at 0.2 m from a wire carrying 10.0 A is 1.00e-05 T.

The magnetic field at 0.3 m from a wire carrying 10.0 A is 6.67e-06 T.

The magnetic field at 0.4 m from a wire carrying 10.0 A is 5.00e-06 T.

The magnetic field at 0.5 m from a wire carrying 10.0 A is 4.00e-06 T.

The magnetic field at 100 m from a wire carrying 10.0 A is 2.00e-08 T.

#Using Lambda Function
![<img width="666" alt="Screenshot 2024-10-14 171115 1" src="](https://github.com/user-attachments/assets/8407ba66-6217-4f84-b34d-319db9356f1f">)


#Using Generator Function
<img width="673" alt="Screenshot 2024-10-14 170110 2" src="https://github.com/user-attachments/assets/1496423e-7e7f-4ead-ac26-eec963ae9dd9">

