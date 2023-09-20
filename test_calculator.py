"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 100 == calculator.multiplication(10, 10)

    def test_division(self):
        assert 42 == calculator.division(84, 2)

    def test_remainder(self):
        assert 0 == calculator.remainder(4, 2)
