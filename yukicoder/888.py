def main():

    N = int(input())
    total = 0
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            k = N / i
            if k != i:
                total += k
                total += i
            else:
                total += i
    print(int(total))

if __name__ == "__main__":
    main()