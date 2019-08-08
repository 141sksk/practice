def main():
    S = input()
    sum = 0
    for i in range(len(S)):
        if S[i].isdecimal():
            sum += int(S[i])
    
    print(sum)

if __name__ == "__main__":
    main()