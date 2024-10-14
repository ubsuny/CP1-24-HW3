import unittest
from Electric_potential import electric_potential

class TestElectricPotential(unittest.TestCase):

    def test_electric_potential(self):
        charge = 1e-6  
        distances = [0.01, 0.02, 0.03]
        expected_potentials = [899000.0, 449500.0, 299666.6666666667]
        assert(electric_potential(charge, distances) == expected_potentials)
        print(electric_potential(charge, distances))
        
    
    def test_electric_potential_zero_distance(self):
        charge = 1e-6  
        distances = [0.01, 0.02, 0.0, 0.05]  # Include a distance of 0
        expected_potentials = [899000.0, 449500.0, float('inf'), 179800.0]  # Expect infinity for distance 0
    
        potentials = electric_potential(charge, distances)
        assert potentials == expected_potentials
        print(f"Expected {expected_potentials}, but got {potentials}")
        
            
if __name__ == '__main__':
    unittest.main()