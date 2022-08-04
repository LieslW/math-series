def fibonacci(n):
    """
    The Fibonacci sequence starts with integers 0 then 1 and continues with a list of numbers where the two previous integers are added together to create a third value. It occurs infiintely using recursion. This function will return the value at whatever given position (input for n)
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """
    The Lucas Numbers are similar to the Fibonacci sequence, but it starts with integers 2 and 1. This function will return the value at whatever given position (input for n)
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


def sum_series(n, x=0, y=1):
    """
    This function sum_series takes into consideration both functions of lucas and fibonacci. It will determine whether the input is part of which previous function above
    """
    if n == 0:
        return x
    elif n == 1:
        return y
    else:
        return sum_series(n-1, x, y) + sum_series(n-2, x, y)

