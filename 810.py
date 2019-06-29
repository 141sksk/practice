def main():

    l, m, r = map(int, input().split())
    myset = set()
    for i in range(l, m + 1):
        amari = i % r
        myset.add(amari)
    print(len(myset))

if __name__ == '__main__':
    main()