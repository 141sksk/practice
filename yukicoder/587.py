def main():

    S = input()
<<<<<<< HEAD
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

=======
    cnt = 0
    ans = ""
    for i in range(13):
        if S.count(S[i]) == 2:
            cnt += 1  
        else:
            ans = S[i]
    if cnt == 12:
        print(ans)
    else:
        print("Impossible")
        
>>>>>>> f42c56548300fc5b8680c29225b5e5c9d986b00b
if __name__ == "__main__":
    main()