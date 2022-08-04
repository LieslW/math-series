from math_series.series import fibonacci


def test_fibonacci_if_int():
    assert type(fibonacci(3)) is int
