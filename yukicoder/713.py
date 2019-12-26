def is_primary(m):
    cnt = 0
    for i in range(2, m):
        if m % i == 0:
            cnt += 1
    if cnt == 0:
        return m
    else:
        return 0

def main():
    n = int(input())
    ans = 0
    for i in range(2, n + 1):
        ans += is_primary(i)
    print(ans)

if __name__ == "__main__":
<<<<<<< HEAD
    main()

=======
    main()
>>>>>>> f42c56548300fc5b8680c29225b5e5c9d986b00b
