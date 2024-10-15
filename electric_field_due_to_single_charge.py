import math

# Coulomb constant in Nm^2/C^2
k = 8.99e9

def electric_field_single_charge(q, r):
    """
    Calculate the electric field due to a single point charge using Coulomb's law.
    
    Parameters:
    q (float): Charge in Coulombs
    r (float): Distance in meters from the charge to the point where the field is calculated
    
    Returns:
    float: Electric field magnitude in N/C
    """
    if r == 0:
        raise ValueError("Distance r cannot be zero to avoid division by zero.")
    return k * q / r**2

def net_electric_field(charges_positions, point_position):
    """
    Calculate the net electric field at a given point due to multiple point charges.
    
    Parameters:
    charges_positions_list (list of tuples): A list of tuples, where each tuple contains:
        - charge (q) in Coulombs,
        - position (x, y) in meters of the charge.
    target_point (tuple): The (x, y) position in meters where the net electric field is calculated.
    
    Returns:
    float: The net electric field magnitude in N/C at the target_point.
    """
    distances = list(
        map(
            lambda pos: math.sqrt(
                (pos[1][0] - point_position[0])**2 + (pos[1][1] - point_position[1])**2
            ), 
            charges_positions
        )
    )
    electric_fields = [
        electric_field_single_charge(charge[0], dist) 
        for charge, dist in zip(charges_positions, distances)
    ]

    # Sum up the magnitudes of all electric fields
    total_net_field = sum(electric_fields)
    
    return total_net_field

# Example
if __name__ == "__main__":
    charges_positions_list = [(1e-6, (1, 0)), (-2e-6, (-1, 0)), (1e-6, (0, 1))]
    target_point = (0, 0)
    
    net_field = net_electric_field(charges_positions_list, target_point)
    print(f"Net electric field at point {target_point}: {net_field:.2e} N/C")
    
