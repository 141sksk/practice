def main():

    a, b, c, d, e, f, g, h, i = list(map(int, input().split()))
    lst = [a, b, c, d, e, f, g, h, i]
    for i in range(1, 11):
        if i not in lst:
            print(i)

if __name__ == "__main__":
    main()