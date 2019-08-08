def main():

    n = list(input())
    mx = int("".join(n))
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            n[i], n[j] = n[j], n[i]
            mx = max(mx, int("".join(n)))
            n[j], n[i] = n[i], n[j]
            
    print(mx)

if __name__ == '__main__':
    main()