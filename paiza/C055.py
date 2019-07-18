def main():
    N = int(input())
    G = input()
    S = [input() for i in range(N)]
    count = 0
    for i in S:
        if G in i:
            print(G)
            count += 1
        else:
            continue
    if count == 0:
        print(None)


if __name__ == "__main__":
    main()