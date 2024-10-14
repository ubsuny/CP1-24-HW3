import unittest
import numpy as np
from electrostatics import scalarpot

class TestElectrostaticPotential(unittest.TestCase):

    def test_zero_q(self):
        '''Tests that the electrostatic potential at all locations is zero if the input charge is zero'''
        N = 300 #300 Charges
        x = [[0,0,0], [1,1,1], [10,10,10],[1000,1000,1000]] #Four locations to find potential, both close to and far from charges
        p = np.random.rand(N, 3) #Randomly scatters charges around origin
        q = 0 #Sets all charges to zero

        assert np.sum(scalarpot(x,p,q)) == 0


    def test_single_charge_origin(self):
        '''Tests the potential due to a single charge at the origin'''
        q = 1.60217663e-19  # Charge of one electron
        epsilon0 = 8.854187817e-12  # Farads per meter
    
        x = np.array([[1, 0, 0], [0, 1, 1], [10, 10, 10]])  #Observation points
        p = np.array([[0, 0, 0]])  #Single charge at origin
    
        expected_potentials = q / (4 * np.pi * epsilon0 * np.linalg.norm(x, axis=1))  #Exact values
    
        potentials = scalarpot(x, p, q)
    
        #Check if calculated potentials match expected values
        np.testing.assert_allclose(potentials, expected_potentials, rtol=1e-6)


    def test_observation_point_at_charge(self):
        '''Tests that the potential returns inf when the observation point is at the same location as a charge'''
        q = 1.60217663e-19
    
        x = np.array([[0, 0, 0]])  #Observation point is at the charge's position
        p = np.array([[0, 0, 0]])  #Single charge at origin
    
        potentials = scalarpot(x, p, q)
    
        #The potential should be inf since distance is zero
        self.assertTrue(np.isinf(potentials[0]))

    