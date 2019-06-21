def main():
    A, B = map(int, input().split())
    list = []
    for i in range(A + 1):
        for j in range(B + 1):
            list.append(i + 5 * j)
        
    s = set(list)
   
    for k in sorted(s)[1:]:
        print(k)

if __name__ == '__main__':
    main()