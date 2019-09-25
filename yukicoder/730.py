def main():

    S = list(input())
    if len(S) == len(set(S)):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()