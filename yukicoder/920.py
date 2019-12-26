def main():

    x, y, z = map(int, input().split())
    ans = 0

    while x > 0 and y > 0:
        x -= 1
        y -= 1
        ans += 1

    w = max(x, y)

    while w > 0 and z > 0:
        w -= 1
        z -= 1
        ans += 1

    while z > 1:
        z -= 2
        ans += 1

    print(ans)

if __name__ == "__main__":
    main()