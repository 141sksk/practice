def main():

    N = int(input())
    positive = (10 ** 6 - 100 * N) * 0.01 + 100 * N * 0.99
    notMember = positive - 100 * N * 0.99
    print((notMember / positive) * 100)

if __name__ == "__main__":
    main()