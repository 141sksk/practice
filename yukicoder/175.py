def main():

    L = int(input())
    N = int(input())
    S = map(str, input().split())
    print(2 ** (L - 3) * N)

if __name__ == "__main__":
    main()