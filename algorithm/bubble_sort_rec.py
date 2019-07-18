def sort(A):
    if len(A) < 2:
        return A
    head, *B = modify_order(A)
    return [head] + sort(B)

def modify_order(A):
    if len(A) < 2:
        return A
    *B, hip, tail = A

    if(hip > tail):
        return modify_order(B + [tail]) + [hip]
    else:
        return modify_order(B + [hip]) + [tail]


print(modify_order([9, 8, 1, 5, 4]))