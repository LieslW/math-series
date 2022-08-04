from math_series.series import fibonacci, lucas, sum_series


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


def test_lucas_if_int():
    assert type(lucas(1)) is int


def test_lucas_zero():
    expected = 2
    actual = lucas(0)
    assert actual == expected


def test_lucas_one():
    expected = 3
    actual = lucas(2)
    assert actual == expected


def test_sum_series_if_int():
    assert type(sum_series(6, 0, 1)) is int


def test_sum_series_one():
    expected = 8
    actual = sum_series(6, 0, 1)
    assert actual == expected

