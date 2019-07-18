def sort(A):
    if len(A) < 2:
        return A
    head, *B = select_min(A)
    return [head] + sort(B)

def select_min(A):
    if len(A) < 2:
        return A
    *B, tail = A
    print(A)
    head, *C = select_min(B)
    if (tail < head):
        return [tail] + C + [head]
    else:
        return [head] + C + [tail]

print(select_min([30, 40, 1, 20, 10]))