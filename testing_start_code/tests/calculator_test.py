import unittest
from src.calculator import add, divide, multiply, subtract

class TestCalculator(unittest.TestCase):
    def test_add__returns_10(self):
        self.assertEqual(10, add(3, 7))

    def test_subtract__returns_negative_4(self):
        self.assertEqual(-4, subtract(3, 7))
        