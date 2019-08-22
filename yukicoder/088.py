def main():
    s = input()
    mylist = []
    for _ in range(8):
        B = list(input())
        mylist += B
    w = mylist.count("w")
    b = mylist.count("b")
    if (w + b) % 2 == 0:
        print(s)
    else:
        if s == "yukiko":
            print("oda")
        else:
            print("yukiko")
    
if __name__ == "__main__":
    main()