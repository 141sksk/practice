def main():
    n = int(input())
    for i in range(n):
        x, y = map(int, input().split())
        if i == 0:
            z = y - x
            if z <= 0:
                print("-1")
                break
        else:
            w = y - x
            if z != w:
                print("-1")
                break
    else:
        print(z)

if __name__ == "__main__":
    main()