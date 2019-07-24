def main():
    N = int(input())
    W = list(map(int, input().split()))

    if sum(W) % 2 != 0:
        print("impossible")
    else:
        half = sum(W) // 2
        dp = [[0 for i in range(half + 1)] for j in range(N + 1)]
        dp[0][0] = 1
        for i in range(N):
            for j in range(half + 1):
                if W[i] <= j:
                    dp[i + 1][j] = dp[i][j - W[i]] or dp[i][j]
                else: 
                    dp[i + 1][j] = dp[i][j]        

        if dp[N][half]:
            print("possible") 
        else:
            print("impossible")

if __name__ == "__main__":
    main()