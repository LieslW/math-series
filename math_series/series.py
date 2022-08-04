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
    if n <= 1:
        if n == 0:
            return 2
        else:
            return 1
        return lucas(n-1) + lucas(n-2)


# def sum_series