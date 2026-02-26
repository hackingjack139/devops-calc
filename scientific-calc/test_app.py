import pytest
from app import squareRoot, factorial, naturalLogarithm, powerFunction
from math import isclose, log

class TestSquareRoot:
    def test_square_root_positive(self):
        assert squareRoot(4) == 2.0
        assert squareRoot(9) == 3.0
        assert squareRoot(10000) == 100.0

    def test_square_root_zero(self):
        assert squareRoot(0) == 0.0
    
    def test_square_root_decimal(self):
        assert squareRoot(0.04) == 0.2
        assert squareRoot(1.44) == 1.2

    def test_square_root_negative(self):
        with pytest.raises(ValueError) as excinfo:
            squareRoot(-4)
        assert str(excinfo.value) == 'Square root for negative numbers is not defined'


class TestFactorial:
    def test_factorial_positive(self):
        assert factorial(1) == 1
        assert factorial(5) == 120
        assert factorial(10) == 3628800
    
    def test_factorial_zero(self):
        assert factorial(0) == 1

    def test_factorial_negative(self):
        with pytest.raises(ValueError) as excinfo:
            factorial(-4)
        assert str(excinfo.value) == 'Factorial for negative numbers is not defined'


class TestNaturalLogarithm:
    def test_natural_logarithm_positive(self):
        assert naturalLogarithm(1) == log(1)
        assert naturalLogarithm(10) == log(10)
        assert naturalLogarithm(10000) == log(10000)

    def test_natural_logarithm_decimal(self):
        assert naturalLogarithm(0.5) == log(0.5)
        assert naturalLogarithm(3.14) == log(3.14)

    def test_natural_logarithm_zero(self):
        with pytest.raises(ValueError) as excinfo:
            naturalLogarithm(0)
        assert str(excinfo.value) == 'Natural logarithm for numbers less than or equal to 0 is not defined'

    def test_natural_logarithm_negative(self):
        with pytest.raises(ValueError) as excinfo:
            naturalLogarithm(-4)
        assert str(excinfo.value) == 'Natural logarithm for numbers less than or equal to 0 is not defined'

    
class TestPowerFunction:
    def test_power_function_positive_base_exponent(self):
        assert isclose(powerFunction(2, 3), 8.0)
        assert isclose(powerFunction(5, 4), 625.0)

    def test_power_function_positive_base_negative_exponent(self):
        assert isclose(powerFunction(2, -2), 0.25)
        assert isclose(powerFunction(10, -1), 0.1)

    def test_power_function_zero_base_positive_exponent(self):
        assert isclose(powerFunction(0, 5), 0.0)

    def test_power_function_zero_base_zero_exponent(self):
        assert isclose(powerFunction(0, 0), 1.0)  # By convention

    def test_power_function_zero_base_negative_exponent(self):
        with pytest.raises(ZeroDivisionError):
            powerFunction(0, -3)