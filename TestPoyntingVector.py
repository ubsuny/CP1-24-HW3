import numpy as np
import sympy as sp
import math
import unittest
from PoyntingVector import electric_field_expression, magnetic_field_expression, poynting_vector_expression, poynting_vector_value, poynting_vector_magnitude

class PoyntingVectorTest(unittest.TestCase):

    def test_poynting_vector_value(self):
        E = sp.Matrix([1.0, 0.0, 0.0]).T
        B = sp.Matrix([0.0, 1.0, 0.0]).T
        position = [0.0, 0.0, 0.0]
        time = 0.0

        Snum = poynting_vector_value(E, B, position, time)
        AnswerDirection = sp.Matrix([0.0, 0.0, 1.0]).T

        assert Snum[0] == AnswerDirection[0]

    def test_poynting_vector_magnitude(self):
        S = [3.0, 4.0, 0.0] 

        Smag = poynting_vector_magnitude(S)

        assert Smag == 5

if __name__ == '__main__':
    unittest.main()