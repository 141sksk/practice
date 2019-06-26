def main():

    N = int(input())
    sushi_plates = list(map(int, input().split()))

    if N == 1:
        # print(sushi_plates.pop())
        print(sushi_plates[0])
        # exit()

    else:
        answers = [0] * (N + 1)
        answers[1] = sushi_plates[0]
        for i in range(2, N + 1):
            answers[i] = max(answers[i - 1], answers[i - 2] + sushi_plates[i - 1])

    print(answers[N])

if __name__ == '__main__':
    main()