def main():

    N, M, P, Q = map(int, input().split())
    count = 0
    while N > 0:
        count += 1
        if count % 12 != 0:
            if P <= count % 12 <= (P + Q - 1):
                N -= 2 * M
            else:
                N -= M
        else:
            if P <= 12 <= (P + Q - 1):
                N -= 2 * M
            else:
                N -= M

    print(count)

if __name__ == "__main__":
    main()