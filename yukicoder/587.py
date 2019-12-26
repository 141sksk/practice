def main():

    S = input()
    new_str = sorted(S)
    cnt = 0
    ans = ""
    for i in range(12):
        if new_str[i] == new_str[i + 1]:
            cnt += 1
        elif new_str.count(new_str[i]) == 1:
            ans = new_str[i]
    if cnt != 6:
        print("Impossible")
    else:
        print(ans)

if __name__ == "__main__":
    main()