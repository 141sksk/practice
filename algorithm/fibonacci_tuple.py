def fib(n):
    if n < 1:
        return (0, 0)
    if n == 1:
        return (0, 1)
    else:
        (a, b) = fib(n - 1)
        return (b, a + b)