def fibonacci(n):
    """
    The Fibonacci sequence starts with integers 0 then 1 and continues with a list of numbers where the two previous integers are added together to create a third value. It occurs infiintely using recursion. This function will return the value at whatever given position (input for n)
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# def lucas


# def sum_series