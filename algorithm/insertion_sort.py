def sort(A):
    for i in range(1, len(A)):
        insert(A, i)


def insert(A, i):
    temp = A[i]
    for j in range(i - 1, -1, -1):
        if temp < A[j]:
            A[j + 1] = A[j]
        else:
            A[j + 1] = temp
            break

    else:
        A[0] = temp