def main():
    N, D = map(int, input().split())
    Tk = 0
    Kt = -D
    for _ in range(N):
        t, k = map(int, input().split())
        newTk = max(Tk + t, Kt + t - D)
        newKt = max(Kt + k, Tk + k - D)
        Tk = newTk
        Kt = newKt

    print(max(Tk, Kt))

if __name__ == "__main__":
    main()


