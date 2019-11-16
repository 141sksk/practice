def main():

    n = int(input())
    A = list(map(int, input().split()))
    ans = A[1] - A[0]
    for i in range(n - 1):
        sub = A[i + 1] - A[i]
        ans = min(sub, ans)
    print(ans)
    print(A[n - 1] - A[0])
    
if __name__ == "__main__":
    main()