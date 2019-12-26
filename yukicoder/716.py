def main():

    n = int(input())
    A = list(map(int, input().split()))
    ans = A[1] - A[0]
    for i in range(n - 1):
        sub = A[i + 1] - A[i]
        ans = min(sub, ans)
    print(ans)
    print(A[n - 1] - A[0])
<<<<<<< HEAD

=======
    
>>>>>>> f42c56548300fc5b8680c29225b5e5c9d986b00b
if __name__ == "__main__":
    main()