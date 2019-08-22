def main():
    n = int(input())
    m = int(input())
    for _ in range(m):
        exchange = list(map(int, input().split()))
        if exchange[0] == n:
            n = exchange[1]
        elif exchange[1] == n:
            n = exchange[0]
    print(n)
if __name__ == "__main__":
    main()