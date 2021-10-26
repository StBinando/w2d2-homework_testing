import unittest
from src.calculator import add, divide, multiply, subtract

class TestCalculator(unittest.TestCase):
    def test_add__returns_10(self):
        self.assertEqual(10, add(3, 7))