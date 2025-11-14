# https://github.com/slomar1/lab11-OPM-SRMR
# Partner 1: Omar Porven Miranda
# Partner 2: Santiago Mena


import math
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1,2), 3)
        self.assertEqual(add(4,0), 4)
        self.assertEqual(add(1,-1), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(2,1), 1)
        self.assertEqual(subtract(4,0), 4)
        self.assertEqual(subtract(1,-1), 2)
    # ##########################

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(mul(5, 10), 50)
        self.assertEqual(mul(-5, 10), -50)
        self.assertEqual(mul(5, 0), 0)

    def test_divide(self):
        self.assertAlmostEqual(div(10, 50), 5.0)
        self.assertAlmostEqual(div(5, 10), 2.0)
        self.assertAlmostEqual(div(-2, 10), -5.0)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        #call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)
        with self.assertRaises(ZeroDivisionError):
            div(0, 0)
        with self.assertRaises(ZeroDivisionError):
            div(-5, 0)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(math.log(1,3), 0)
        self.assertEqual(math.log(10,10), 1)
        self.assertEqual(math.log(4,2), 2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            math.log(0, 2)
            math.log(-1, 2)
            math.log(10, 1)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(10, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(4), 2.0)
        with self.assertRaises(ValueError):
           square_root(-1)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()