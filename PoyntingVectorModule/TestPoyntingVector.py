import PoyntingVector
import numpy as np
import sympy as sp
import math
import pytest

def Test_PoyntingVector():
    E_0 = 5
    wave_vector = [1, 0, 1]
    delta = 0
    polarisation = [0, 0, 1]
    f = 100

    position = [0, 0, 0]
    time = 0

    E = electric_field_expression(E_0, wave_vector, delta, f, polarisation)
    B = magnetic_field_expression(E_0, wave_vector, delta, f, polarisation)
    S = poynting_vector_expression(E, B)
    Snum = poynting_vector_value(E, B, position, time)
    Smag = poynting_vector_magnitude(Snum)

    assert Smag - 3978873.5773 < 0.01
