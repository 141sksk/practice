def main():

    S = input()
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
        
if __name__ == "__main__":
    main()