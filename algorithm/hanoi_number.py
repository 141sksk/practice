def move(k):
    A = [None] * k
    A[0] = 1
    for i in range(1, k):
        A[i] = 2 * A[i - 1] + 1
    return A[k - 1]

print(move(4))