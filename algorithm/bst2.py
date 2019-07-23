def remove(T, n):
    if len(T) == 0:
        return()
    L, data, R = T
    if n == data:
        if len(L) == 0:
            return R
        if len(R) == 0:
            return L
        m, X = remove_min(R)
        return (L, m, X)
    if n < data:
        return(remove(L, n), data, R)
    return (L, data, remove(R, n))

def remove_min(T):
    L, data, R = T
    if len(L) == 0:
        return (data, R)
    m, X = remove_min(L)
    return (m, (X, data, R))

Y = (((), 6, ()), 8, ((), 10, ()))
X = (((), 1, ()), 4, (Y, 11, ()))
print(remove(X, 6))