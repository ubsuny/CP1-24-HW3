'''
This module runs the unittest for the functions in PoyntingVector.py module 
'''
import math
import unittest
import sympy as sp

# importing all functions from PoyntingVector module
from PoyntingVector import poynting_vector_value, poynting_vector_magnitude

class PoyntingVectorTest(unittest.TestCase):

    def test_poynting_vector_value(self): 
        E = sp.Matrix([1.0, 0.0, 0.0]).T
        B = sp.Matrix([0.0, 1.0, 0.0]).T
        position = [0.0, 0.0, 0.0]
        time = 0.0

        Snum = poynting_vector_value(E, B, position, time) # obtainng the PoyntingVector for trivial case
        AnswerDirection = sp.Matrix([0.0, 0.0, 1.0]).T # checking if first component is equal to the expected result

        assert Snum[0] == AnswerDirection[0]

    def test_poynting_vector_magnitude(self):
        S = [3.0, 4.0, 0.0] 

        Smag = poynting_vector_magnitude(S) # obtaining the trivial case PoyntingVector magnitude

        assert Smag == 5 # asserting the value to the expected result

if __name__ == '__main__':
    unittest.main()
