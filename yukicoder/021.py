def main():

    N = int(input())
    k = int(input())
    mylist = []
    for i in range(N):
        n = int(input())
        mylist.append(n)
    mylist.sort()
    
    print(mylist[-1] - mylist[0])

if __name__ == "__main__":
    main()