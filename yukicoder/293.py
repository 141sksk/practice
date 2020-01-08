def main():

    a, b = map(str, input().split())
    if len(a) < len(b):
        print(b)
    elif len(a) > len(b):
        print(a)
    else:
        for x, y in zip(a, b):
            if x == '4' and y == '7':
                print(a)
                break
            elif x == '7' and y == '4':
                print(b)
                break
            elif int(x) > int(y):
                print(a)
                break
            elif int(x) < int(y):
                print(b)
                break

if __name__ == "__main__":
    main()