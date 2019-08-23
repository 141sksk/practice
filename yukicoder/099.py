def main():

    N = int(input())
    myList = list(map(int, input().split()))
    oddCount = 0
    evenCount = 0
    for i in range(N):
        if myList[i] % 2 == 0:
            evenCount += 1
        else:
            oddCount += 1
    print(abs(oddCount - evenCount))

if __name__ == "__main__":
    main()