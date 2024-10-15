"""
This module calculates the Lorentz force on moving charged particles
in a magnetic field using functional programming concepts.

It demonstrates the use of lambda functions and the map function to calculate
the Lorentz force for a list of particles.
"""

import math

# Lambda function to calculate Lorentz force
lorentz_force = lambda charge, velocity, magnetic_field, angle_radians: (
    charge * velocity * magnetic_field * math.sin(angle_radians)
)

def main():
    """
    Demonstrates the calculation of Lorentz forces for a list of particles.

    This function uses the `lorentz_force` lambda function and `map` to compute
    the Lorentz force for a set of particles, each represented by a dictionary
    containing its charge, velocity, magnetic field, and the angle between
    its velocity and the magnetic field.

    Args:
        None

    Returns:
        None
    """

    # Example particle data
    particles = [
        {
            'charge': 1.6e-19,
            'velocity': 2.0e6,
            'magnetic_field': 1.2,
            'angle_radians': math.pi / 4
        },
        {
            'charge': -1.6e-19,
            'velocity': 3.0e6,
            'magnetic_field': 0.8,
            'angle_radians': math.pi / 6
        },
        {
            'charge': 1.6e-19,
            'velocity': 1.5e6,
            'magnetic_field': 1.0,
            'angle_radians': math.pi / 3
        }
    ]

    # Use map to apply lorentz_force to each particle
    forces = list(
        map(
            lambda p: lorentz_force(
                p['charge'], p['velocity'],
                p['magnetic_field'], p['angle_radians']
            ),
            particles
        )
    )

    # Print the Lorentz forces for each particle
    print(forces)

if __name__ == "__main__":
    main()
