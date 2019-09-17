def main():

    n = int(input())
    A = []
    B = []
    for _ in range(n):
        a, b = list(map(int, input().split()))
        A.append(a)
        B.append(b)
    m = int(input())
    X = []
    Y = []
    M = [0] * m
    for _ in range(m):
        x, y = list(map(int, input().split()))
        X.append(x)
        Y.append(y)
    for i in range(n):
        for j in range(m):
            if X[j] <= A[i] and Y[j] >= B[i]:
                M[j] += 1
    mx = max(M)
    
    if max(M) == 0:
        print("0")
    else:
        for x in range(m):
            if M[x] == mx:
                print(x + 1)

if __name__ == "__main__":
    main()