def main():

    N = int(input())
    A = list(map(int, input().split()))
    start = N
    for i in range(N - 1, -1, -1):
        if A[i] == start:
            start -= 1

    print(start)

if __name__ == "__main__":
    main()