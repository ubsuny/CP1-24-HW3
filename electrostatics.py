import numpy as np

#Constants
epsilon0 = 8.854187817e-12  #Farads per meter

#Lambda function to calculate the distance between an observation point x and all charges p
r_xp = lambda x, p: np.linalg.norm(x - p, axis=1)

#Standard function to calculate the scalar electrostatic potential at multiple observation points
def scalarpot(x, p, q):
    """
    Computes the scalar electrostatic potential at multiple observation points(x) due to N charges (q) at positions (p).
    
    Inputs:
    - x: List of observations points. Each point should be given as a list of length 3 signifying the position, in meters, in the x, y and z directions
    - p: List of positions of the charges. Each item in the list should be a list of length 3 signifying the position, in meters, in the x, y and z directions
    - q: Charge (in Coulombs) of the charges at position p. Each charge is assumed to be the same. This could be generalized to include different charges at each point.
    
    Returns:
    - V: Array of potential values at each observation point
    """
    V = np.zeros(len(x))  #Initialize potential array for observation points. 
    
    #Loop over all observation points using enumerate, an iterator
    for i, obs_point in enumerate(x): #enumerate(x) returns the index of x as i and the value of x at that index as obs_point
        #Compute distances from the observation point to all charges
        distances = r_xp(obs_point, p)
        #Avoid division by zero in case an observation point coincides with a charge
        distances[distances == 0] = np.inf
        #Compute potential contributions from each charge and sum them up
        V[i] = np.sum(q / (4 * np.pi * epsilon0 * distances))
    
    return V #Returns a list of vector potentials at the given points, x