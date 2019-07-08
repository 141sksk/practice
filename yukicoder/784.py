def main():
    n = list(reversed(input()))
    m = ""
    x = len(n)
    for i in range(x):
        m += n[i]
        if (i + 3) % 3 == 2 and (i + 1) != x:
            m += ","
    p = reversed(list(m))
    print("".join(p))

if __name__ == "__main__":
    main()