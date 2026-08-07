import pytest

def add(a, b):
    return a + b

def is_even(num):
    return num % 2 == 0

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -2) == -3

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (0, 0, 0),
    (10, -5, 5),
    (-3, -7, -10)
])
def test_add_multiple(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("num, result", [
    (2, True),
    (3, False),
    (0, True),
    (-1, False)
])
def test_is_even(num, result):
    assert is_even(num) == result