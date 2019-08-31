def main():

    t = int(input())
    x = [int(input()) for _ in range(t)]
    trueCount = 0
    for i in range(t - 1):
        if x[i + 1] == x[i] + 1 or x[i + 1] == x[i] - 1:
            trueCount += 1
    if x[0] == 1 or x[0] == -1:
        if trueCount == t - 1:
            print("T")
        else:
            print("F")
    else:
        print("F")

if __name__ == "__main__":
    main()