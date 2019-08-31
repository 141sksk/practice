def show(T):
    if len(T) == 0:
        return ''
    L, data, R = T
    return '(' + show(L) + str(data) + show(R) + ')'

X = (((), 1, ()), 3, ((), 5, ()))
show(X)

def insert(T, n):
    if len(T) == 0:
        return ((), n, ())
    L, data, R = T
    if n == data:
        return T
    if n < data:
        return(insert(L, n), data, R)
    return (L, data, insert(R, n))

def search(T, n):
    if len(T) == 0:
        return False
    L, data, R = T
    if n == data:
        return True
    if n < data:
        return search(L, n)
    return search(R, n)

X = insert((), 6)
show(X)

