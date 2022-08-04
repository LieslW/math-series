from math_series.series import fibonacci


def test_fibonacci_if_int():
    assert type(fibonacci(3)) is int


def test_fibonacci_zero():
    expected = 0
    actual = fibonacci(0)
    assert actual == expected


def test_fibonacci_one():
    expected = 1
    actual = fibonacci(1)
    assert actual == expected

