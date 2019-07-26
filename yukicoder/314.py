def main():

    n = int(input())
    k1, k2, p = [0 for i in range(n + 1)], [0 for i in range(n + 1)], [0 for i in range(n + 1)]
    k1[1], k2[1], p[1] = 1, 0, 0
    for i in range(1, n):
        k1[i + 1] = p[i] % (10 ** 9 + 7)
        k2[i + 1] = k1[i] % (10 ** 9 + 7)
        p[i + 1] = (k1[i] + k2[i]) % (10 ** 9 + 7)

    print((k1[n] + k2[n] + p[n]) % (10 ** 9 + 7))

if __name__ == "__main__":
    main()