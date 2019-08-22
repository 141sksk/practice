def main():
    d, p = map(int, input().split())
    print(d + d * p // 100)


if __name__ == "__main__":
    main()