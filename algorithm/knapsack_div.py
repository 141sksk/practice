def max(A, n):
    def f(t): return t[1] / t[2]
    A.sort(key = f, reverse = True)
    b = 0; items = []
    for (i, p, w) in A:
        if n >= w:
            b = b + p
            items = items + [(i, w)]
            n = n - w
        else:
            b = b + p * n / w
            items = items + [(i, n)]
            break
    return (b, items)

A = [('A', 400, 5), ('B', 300, 4), ('C', 200, 2), ('D', 300, 1)]
print(max(A, 5))