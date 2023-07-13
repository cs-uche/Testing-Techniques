#!usr/bin/env python3

from addition import add_number
from divide import divide_number


def test_add_positive():
    assert add_number(2, 3) == 2 + 3


def test_add_negative():
    assert add_number(2, -3) == 2 + -3


def test_add_zero():
    assert add_number(-5, 0) == (-5) + 0


def test_add_wrong_type():
    assert add_number("one", 2) == "error"


def test_divide_positive():
    assert divide_number(2, 3) == int(2 / 3)


def test_divide_negative():
    assert divide_number(2, -3) == int(2 / -3)


def test_divide_zero():
    assert divide_number(-5, 0) == "error"


def test_divide_wrong_type():
    assert divide_number("one", 2) == "error"
