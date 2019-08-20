def main():
    budget = int(input())
    children = int(input())
    if budget / children < 1000:
        print("0")
    else:
        if budget / 1000 % children == 0:
            mount = budget / children
            print(int(mount))
        else:
            mount = round(budget / 1000 // children) * 1000
            print(int(mount))


if __name__ == "__main__":
    main()