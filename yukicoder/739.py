def main():
    s = input()
    cnt = len(s) // 2
    if s[cnt:] == s[:cnt]:
        print("YES")
    else:
        print("NO")
if __name__ == "__main__":
    main()