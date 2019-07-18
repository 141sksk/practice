def sort(A):
    if len(A) < 2:
        return A
    return insert(sort(A[:-1]), A[-1])

def insert(A, temp):
    if len(A) < 1:
        return [temp]
    *B, tail = A
    if tail > temp:
        return insert(B, temp) + [tail]
    else:
        return A + [temp]

print(insert([1, 3, 5, 7, 9], 0))