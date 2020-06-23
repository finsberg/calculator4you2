import random
import pytest  # pip install pytest

from calculator4you2 import calculator4you2 as calculator

tol = 1e-14


def test_add():
    assert abs(calculator.add(1, 1) - 2) < tol


def test_subtract():
    assert abs(calculator.subtract(2, 1) - 1) < tol


def test_divide():
    assert abs(calculator.divide(1, 2) - 0.5) < tol


def test_divide_raises_ZeroDivisionError():

    with pytest.raises(ZeroDivisionError):
        calculator.divide(1, 0)


@pytest.mark.parametrize("execution_number", range(3))
def test_add_random_pytest(execution_number):
    x = random.uniform(0, 100)
    y = random.uniform(0, 100)
    assert abs(calculator.add(x, y) - (x + y)) < tol


if __name__ == "__main__":
    pass
