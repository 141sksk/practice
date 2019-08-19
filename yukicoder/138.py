def main():
    a = list(map(int, input().split('.')))
    b = list(map(int, input().split('.')))
    for i in range(3):
        if a[i] > b[i]:
            print("YES")
            break
        elif a[i] < b[i]:
            print("NO")
            break
    else:
        print("YES")

if __name__ == "__main__":
    main()