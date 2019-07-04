def sort(A):
    for i in range(0, len(A) - 1):
        modify_order(A, i)

def modify_order(A, i):
    for j in range(len(A) - 1, i, -1):
        if A[j - 1] > A[j]:
            A[j - 1], A[j] = A[j], A[j - 1]