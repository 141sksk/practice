import itertools

def main():

    n, m = map(int, input().split())
    myList = [[0] * n for _ in range(n)]
    for _ in range(m):
        i1, i2, score = map(int, input().split())
        myList[i1][i2] = score

    mx = 0
    for cmb in itertools.permutations([i for i in range(n)]):
        total = 0
        for j in range(n - 1):
            for k in range(j + 1, n):
                total += myList[cmb[j]][cmb[k]]
        if total > mx:
            mx = total
    print(mx)

if __name__ == "__main__":
    main()