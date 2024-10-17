'''
This module runs the unittest for the functions in PoyntingVector.py module 
'''
import unittest
import sympy as sp

# importing all functions from PoyntingVector module
from poynting_vector import poynting_vector_value, poynting_vector_magnitude

class PoyntingVectorTest(unittest.TestCase):
    # this class implements the unitest functions

    def test_poynting_vector_value(self):
        # testing the poynting vector value function
        e = sp.Matrix([1.0, 0.0, 0.0]).T
        b = sp.Matrix([0.0, 1.0, 0.0]).T
        position = [0.0, 0.0, 0.0]
        time = 0.0

        pv_num = poynting_vector_value(e, b, position, time)
        # obtainng the PoyntingVector for trivial case

        answer_direction = sp.Matrix([0.0, 0.0, 1.0]).T
        # checking if first component is equal to the expected result

        assert pv_num[0] == answer_direction[0]

    def test_poynting_vector_magnitude(self):
        # testing the poynting ector magnitude function
        pv = [3.0, 4.0, 0.0]

        pv_mag = poynting_vector_magnitude(pv)
        # obtaining the trivial case PoyntingVector magnitude

        assert pv_mag == 5 # asserting the value to the expected result

if __name__ == '__main__':
    # running the unit test script
    unittest.main()
