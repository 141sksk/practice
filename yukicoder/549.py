def main():

    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    experience = x[n - 1]
    for i in range(n - 1, 0, -1):
        experience += x[i - 1] // 2
    
    print(experience)

if __name__ == "__main__":
    main()