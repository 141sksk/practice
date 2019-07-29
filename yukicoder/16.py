def main():

    x, n = map(int, input().split())
    s = list(map(int, input().split()))
    sum = 0
    for j in range(n):
        sum += pow(x, s[j], 1000003)
    ans = sum % 1000003
    print(ans)

if __name__ == "__main__":
    main()

