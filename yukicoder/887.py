def main():

    n = int(input())
    myList = [n]
    while n != 1:
        if n % 2 == 0:
            n /= 2
            myList.append(int(n))
        else:
            n = 3 * n + 1
            myList.append(int(n))
    print(len(myList) - 1)
    print(max(myList))

if __name__ == "__main__":
    main()