def main():
    N = int(input())
    a = input()
    if " " in a:
        print('"assert"')
    else:
        b, c = int(input()), int(input())
        a = int(a)
        myList = {a + b, b + c, c + a}
        myList.remove(max(myList))
        print(max(myList))

if __name__ == "__main__":
    main()

# N = int(input())
# a = input()
# if " " in a:
    print('"assert"')
# else:
#     b,c = int(input()),int(input())
#     a = int(a)
#     l = {a+b,a+c,b+c}
#     l.remove(max(l))
#     print(max(l))