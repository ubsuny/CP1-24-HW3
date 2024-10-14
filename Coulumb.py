COULOMBS_CONSTANT = 8.99e9

calculate_electric_force = lambda q1, q2, r: (print("Distance between charges cannot be zero.") if r == 0 else COULOMBS_CONSTANT * abs(q1 * q2) / r**2)