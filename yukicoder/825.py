def main():
    A, B, C = map(int, input().split())
    n = A + B - C
    if n < 0:
        if B == 0:
            print("Impossible")
        elif n > -9:
            print(10 + n - 1)
        else:
            print("Impossible")


if __name__ == '__main__':
    main()