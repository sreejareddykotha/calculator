import pytest
import calculator


def test_add():
    assert calculator.calculate("+", 2, 3) == 5


def test_subtract():
    assert calculator.calculate("-", 5, 2) == 3


def test_multiply():
    assert calculator.calculate("*", 3, 4) == 12


def test_divide():
    assert calculator.calculate("/", 8, 2) == 4


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.calculate("/", 5, 0)


def test_invalid_operation():
    with pytest.raises(ValueError):
        calculator.calculate("x", 2, 2)