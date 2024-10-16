'''
This module calculates the PoyntingVector for a given electromagnetic wave
'''
import numpy as np
import sympy as sp
import math

def electric_field_expression(E_0, wave_vector, delta, f, polarisation):
    # function to generate the Electric Field expression
    t, x, y, z = sp.symbols('t x y z')    # defining the positon and time variables
    omega = 2 * sp.pi * f    # defining the angular frequenc variable

    r = sp.Matrix([x, y, z])    # generating the position vector
    k = sp.Matrix(wave_vector)    # generating the wave vector

    norm_polarisation = np.linalg.norm(polarisation)    # norm of the polarisation vector
    polarisation_normalised = list(map(lambda a: a / norm_polarisation, polarisation)) # normalising the polarisaion vector using map and lamda function

    n_hat = sp.Matrix(polarisation_normalised)    # generating the normalised polarisation vector

    k_dot_r = r.dot(k) 

    return E_0 * sp.cos(k_dot_r - omega * t + delta) * n_hat.T    # returning the Electric Field in algebraic form

def magnetic_field_expression(E_0, wave_vector, delta, f, polarisation):
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

    k_cross_n = k_hat.cross(n_hat)    # the polarisation direction for magnetic field
    k_dot_r = r.dot(k)

    return (1/c) * E_0 * sp.cos(k_dot_r - omega * t + delta) * k_cross_n.T    # returning the magnetic field in algebraic form

def poynting_vector_expression(E, B):
    mu = sp.symbols('mu')
    S = (1/mu) * E.cross(B)    # obtaining the algebraic expression for Poynting Vector
    return S

def poynting_vector_value(E, B, position, time):
    S = poynting_vector_expression(E, B)
    return S.subs({'x': position[0], 'y': position[1], 'z': position[2], 't': time, 'c' : 299792458, 'mu' : 0.00000125663}).evalf()
    # returning the numeric value for Poynting Vector

def poynting_vector_magnitude(S):
    return math.sqrt(S[0] ** 2 + S[1] ** 2 + S[2] ** 2)    # returning the magnitude of Poynting Vector

def main():
    # taking all parameters through function call
    E_0 = float(input("Please enter the value of Electric Field amplitude (in V/m): "))
    kx = float(input("Please enter x-component of wave-vector kx (in radians/m): "))
    ky = float(input("Please enter y-component of wave-vector ky (in radians/m): "))
    kz = float(input("Please enter z-component of wave-vector kz (in radians/m): "))
    delta = float(input("Please enter the phase factor (in radians): "))
    f = float(input("Please enter frequency of the electromagnetic wave (in Hz): "))
    nx = float(input("Please enter x-component of polarisation: "))
    ny = float(input("Please enter y-component of polarisation: "))
    nz = float(input("Please enter z-component of polarisation: "))
    x = float(input("enter the x-coordinate of position (in m): "))
    y = float(input("enter the y-coordinate of position (in m): "))
    z = float(input("enter the z-coordinate of position (in m): "))
    time = float(input("Please enter time (in sec): "))

    # calculating the Electric, Magnetic Field and Poynting vector
    E = electric_field_expression(E_0, [kx, ky, kz], delta, f, [nx, ny, nz]) 
    B = magnetic_field_expression(E_0, [kx, ky, kz], delta, f, [nx, ny, nz])
    S = poynting_vector_expression(E, B)
    Snum = poynting_vector_value(E, B, [x, y, z], time)
    Smag = poynting_vector_magnitude(Snum)

    # Outputs all results
    print("Electric Field (in V/m): ", E)
    print("Magnetic Field (in T): ", B)
    print("Poynting Vector (in W/m^2): ", S, " = ", Snum)
    print("The magnitude of Poynting Vector (in W/m^2): ", Smag)

if __name__ == "__main__":
    main()    # function call condition