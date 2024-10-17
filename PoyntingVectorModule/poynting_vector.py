'''
This module calculates the PoyntingVector for a given electromagnetic wave
'''
import math
import numpy as np
import sympy as sp

def electric_field_expression(e_0, wave_vector, delta, f, polarisation):    # generates Electric Field
    t, x, y, z = sp.symbols('t x y z')  # defining the positon and time variables
    omega = 2 * sp.pi * f   # defining the angular frequenc variable

    r = sp.Matrix([x, y, z])    # generating the position vector
    k = sp.Matrix(wave_vector)  # generating the wave vector

    norm_polarisation = np.linalg.norm(polarisation)    # norm of the polarisation vector

    polarisation_normalised = list(map(lambda a: a / norm_polarisation, polarisation))
    # normalising the polarisaion vector using map and lamda function
    n_hat = sp.Matrix(polarisation_normalised)
    # generating the normalised polarisation vector
    k_dot_r = r.dot(k)
    return e_0 * sp.cos(k_dot_r - omega * t + delta) * n_hat.T
    # returning the Electric Field in algebraic form

def magnetic_field_expression(e_0, wave_vector, delta, f, polarisation):    # generates Magnetic Field
    c, t, x, y, z = sp.symbols('c t x y z')
    omega = 2 * sp.pi * f
    r = sp.Matrix([x, y, z])
    k = sp.Matrix(wave_vector)
    norm_polarisation = np.linalg.norm(polarisation)
    polarisation_normalised = list(map(lambda a: a / norm_polarisation, polarisation))
    norm_k = np.linalg.norm(wave_vector)
    k_normalised = list(map(lambda a: a / norm_k, wave_vector))

    n_hat = sp.Matrix(polarisation_normalised)
    k_hat = sp.Matrix(k_normalised)

    k_cross_n = k_hat.cross(n_hat)  # the polarisation direction for magnetic field
    k_dot_r = r.dot(k)

    return (1/c) * e_0 * sp.cos(k_dot_r - omega * t + delta) * k_cross_n.T
    # returning the magnetic field in algebraic form

def poynting_vector_expression(e, b):   # calculates poynting vector
    mu = sp.symbols('mu')
    pv = (1/mu) * e.cross(b)
    # obtaining the algebraic expression for Poynting Vector
    return pv

def poynting_vector_value(e, b, position, time):    # enumerates poynting vector
    pv = poynting_vector_expression(e, b)
    return pv.subs({'x': position[0], 'y': position[1], 'z': position[2],
                    't': time, 'c' : 299792458, 'mu' : 0.00000125663}).evalf()
    # returning the numeric value for Poynting Vector

def poynting_vector_magnitude(pv):  # calculate poynting vector magitude
    return math.sqrt(pv[0] ** 2 + pv[1] ** 2 + pv[2] ** 2)
    # returning the magnitude of Poynting Vector
