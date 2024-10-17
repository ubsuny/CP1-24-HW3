"""
This Module is to define the main desired funtion:
    A function to calculate the surface charge density of a conducting spherical shell held at constant potential.

The specifications needed for the shell:
    The radius (R): a float number.
    The constant potential (V): a float number.

Considering the units used, the default system will be the metric system.
However, it will be flexible to convert to other systems by manually choosing the inpus' units.
A constant value of (epsilon_0) is thus set by default to the units of the metric system.
"""

from MathOpsModule import *

def sigma(R, V, epsilon_0 = 8.854*(10**(-12))):
    """
    Returns the surface charge density of a conducting spherical shell of radius (R) held at constant potential (V).
    Parameters:
    R, V, epsilon_0: input numbers (radius, potential, electric permitivity of free space)
    Returns:
    number: the surface charge density
    """
    Sigma = lambda epsilon_00, V0, R0: mult(epsilon_00, div(V0, R0)) 
    return Sigma(epsilon_0, V, R)
