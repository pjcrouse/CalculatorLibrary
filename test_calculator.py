"""Unit tests for calculator library"""

import calculator
import pytest


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtract(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiply(self):
        assert 100 == calculator.multiply(10, 10)

    def test_divide(self):
        assert 100 == calculator.divide(1000, 10)

    def test_zero_division(self):
        with pytest.raises(ValueError) as e:
            calculator.divide(1, 0)
        assert str(e.value) == "Cannot divide by Zero"
