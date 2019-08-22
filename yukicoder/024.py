def main():
    N = int(input())
    answerSet = {str(i) for i in range(10)}
    for _ in range(N):
        A, B, C, D, R = input().split()
        numberSet = {A, B, C, D}
        if R == "YES":
            answerSet &= numberSet
        else:
            answerSet -= numberSet
    answer = list(answerSet)
    print(answer[0])

if __name__ =="__main__":
    main()
