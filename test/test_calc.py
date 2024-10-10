import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from calc import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(1e10, 1e10), 2e10)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(1.5, 0.5), 1.0)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(1e10, 1e9), 9e9)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(1.5, 2), 3.0)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(1e5, 1e5), 1e10)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-10, -2), 5)
        self.assertEqual(self.calc.divide(1.5, 0.5), 3.0)
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
        self.assertEqual(self.calc.divide(0, 1), 0)
        self.assertEqual(self.calc.divide(1e10, 1e5), 1e5)

    def test_validate_input(self):
        with self.assertRaises(TypeError):
            self.calc._validate_input("a", 1)
        with self.assertRaises(TypeError):
            self.calc._validate_input(1, "b")
        with self.assertRaises(TypeError):
            self.calc._validate_input("a", "b")
        self.assertEqual(self.calc.subtract(-1, -1), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            self.calc.add("a", 1)
        with self.assertRaises(TypeError):
            self.calc.subtract(1, "b")
        with self.assertRaises(TypeError):
            self.calc.multiply("a", "b")
        with self.assertRaises(TypeError):
            self.calc.divide("a", 1)

if __name__ == '__main__':
    unittest.main()