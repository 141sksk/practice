def main():
    n = int(input())
    step = [0] * n
    step[0] = 1
    step[1] = 2
    for i in range(2, n):
        step[i] = step[i - 1] + step[i - 2]
    print(step[n - 1])

if __name__ == "__main__":
    main()

    