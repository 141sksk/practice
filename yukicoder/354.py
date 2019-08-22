def main():
    p = int(input())
    n = 2 ** p - 1
    print(bin(n).count("1"))

if __name__ == "__main__":
    main()