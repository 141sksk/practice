def sort(A):
    if len(A) < 2:
        return A
    p = A[0]
    print(p)
    X, Y = devide(p, A[1:])
    # print(X, Y)
    return sort(X) + [p] + sort(Y)

def devide(p, A):
    if len(A) < 1:
        return([], [])
    X, Y = devide(p, A[1:])
    # print(X, Y)
    a = A[0]
    # print(a)
    if a < p:
        return ([a] + X, Y)
    else:
        return(X, [a] + Y)

