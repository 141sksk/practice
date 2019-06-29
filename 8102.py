def main():
    l, r, m = map(int, input().split())
    c = r - l + 1
    print(min(c, m))

if __name__ == "__main__":
    main()