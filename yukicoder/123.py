def main():

    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    cards = [x + 1 for x in range(n)]
    for a_i in A:
        P = [cards[a_i - 1]]
        cards.pop(a_i - 1)
        cards = P + cards
    print(cards[0])


if __name__ == "__main__":
    main()