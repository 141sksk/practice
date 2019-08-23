def main():

    A, B, C, D = map(int, input().split())
    score = 0
    combo = 1
    if D == 10:
        print("Impossible")
    else:
        while B > 100:
            score += 50 * combo * 100
            B -= 100
            combo *= 2
        else:
            score += 50 * combo * B
            if A < 100 - B:
                score += 100 * combo * A
            else:
                score += 100 * combo * (100 - B)
                A -= 100 - B
                combo *= 2
            while A > 100:
                score += 100 * combo * 100
                A -= 100
                combo *= 2
            else:
                score += 100 * combo * A
        print("Possible")
        print(score)  

if __name__ == "__main__":
    main()