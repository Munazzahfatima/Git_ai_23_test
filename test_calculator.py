import pytest
from calculator import Calculator

@pytest.mark.parametrize("a, b, expected", [
    (3, 5, 8),
    (-1, 1, 0),
    (-1, -1, -2),
    (0, 0, 0)
])
def test_add_parameterized(calculator, a, b, expected):
    assert calculator.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (1, 5, -4),
    (-5, -3, -2)
])
def test_subtract_parameterized(calculator, a, b, expected):
    assert calculator.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (2.0, 3.0, 6.0),
    (-2, 3, -6),
    (0, 5, 0)
])
def test_multiply_parameterized(calculator, a, b, expected):
    assert calculator.multiply(a, b) == pytest.approx(expected)

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (5, 2, 2.5),
    (9, 3, 3)
])
def test_divide_parameterized(calculator, a, b, expected):
    assert calculator.divide(a, b) == pytest.approx(expected)

@pytest.mark.parametrize("a, b", [
    (5, 0),
    (0, 0)
])
def test_divide_by_zero(calculator, a, b):
    with pytest.raises(ValueError):
        calculator.divide(a, b)

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 8),
    (3, 2, 9),
    (2, 0, 1),
    (2, -2, 0.25),  # 1/(2^2)
    (10, -1, 0.1)   # 1/10
])
def test_power_parameterized(calculator, a, b, expected):
    assert calculator.power(a, b) == pytest.approx(expected)

@pytest.mark.parametrize("n, expected", [
    (0, 1),
    (1, 1),
    (5, 120),
    (6, 720)
])
def test_factorial(calculator, n, expected):
    assert calculator.factorial(n) == expected

@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (5, 5),
    (7, 13)
])
def test_fibonacci(calculator, n, expected):
    assert calculator.fibonacci(n) == expected

@pytest.mark.parametrize("n", [-1, -5])
def test_factorial_negative(calculator, n):
    with pytest.raises(ValueError):
        calculator.factorial(n)

@pytest.mark.parametrize("n", [-1, -3])
def test_fibonacci_negative(calculator, n):
    with pytest.raises(ValueError):
        calculator.fibonacci(n)

@pytest.mark.parametrize("a, b, expected", [
    (1.1111, 2.2222, 3.33),
    (1.5555, 2.5555, 4.11),
])
def test_precise_add(precise_calculator, a, b, expected):
    assert precise_calculator.add(a, b) == pytest.approx(expected)

