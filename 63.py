def main():

    L, M = map(int, input().split())
    count = 0
    while L - 2 * M > 0:
        L -= 2 * M
        count += 1
      
    print(M * count)


if __name__ == "__main__":
    main()