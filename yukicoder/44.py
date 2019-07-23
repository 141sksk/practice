def main():
    n = int(input())
    goal = [0] * (n + 1) 
    goal[0] = 1
    goal[1] = 2
    for i in range(2, n + 1):
        goal[i] = goal[i - 1] + goal[i - 2]
    print(goal)
    print(goal[n - 1])

if __name__ == "__main__":
    main()

