import math

# Coulomb constant in Nm^2/C^2
k = 8.99e9

def electric_field_single_charge(q, r):
    """
    Calculate the electric field due to a single point charge using Coulomb's law.
    """
    if r == 0:
        raise ValueError("Distance r cannot be zero to avoid division by zero.")
    return k * q / r**2

def net_electric_field(charges_positions, point_position):
    """
    Calculate the net electric field at a given point due to multiple point charges.
    """
    distances = list(map(lambda pos: math.sqrt((pos[1][0] - point_position[0])**2 + (pos[1][1] - point_position[1])**2), charges_positions))
    electric_fields = [electric_field_single_charge(charge[0], dist) for charge, dist in zip(charges_positions, distances)]
    net_field = sum(electric_fields)
    return net_field

# Example usage
charges_positions = [(1e-6, (1, 0)), (-2e-6, (-1, 0)), (1e-6, (0, 1))]
point_position = (0, 0)

net_field = net_electric_field(charges_positions, point_position)
print(f"Net electric field at point {point_position}: {net_field:.2e} N/C")
