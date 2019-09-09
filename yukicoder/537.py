def main():

    N = int(input())
    myList = []
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            j = int(N / i)
            myList.append((str(i) + str(j)))
            myList.append((str(j) + str(i)))
    mySet = set(myList)
    print(len(mySet))

if __name__ == "__main__":
    main()