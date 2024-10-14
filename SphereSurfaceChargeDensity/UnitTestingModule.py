import unittest
from PhysicsModule import *

class TestSurfaceCharge(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(sigma(5, 0), 0.0)


if __name__ == '__main__':
    unittest.main()