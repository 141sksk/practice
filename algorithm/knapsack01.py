def max(A, n):
    B = [(0, [])] * (n + 1)
    for (i, p, w) in A:
        for j in range(n, w - 1, -1):
            if B[j - w][0] + p > B[j][0]:
                B[j] = (B[j - w][0] + p, B[j - w][1] + [i])
        print(i, B)


A = [('A', 400, 5), ('B', 300, 4), ('C', 200, 2), ('D', 300, 1)]
print(max(A, 5))