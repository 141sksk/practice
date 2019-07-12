def main():
    hand = list(map(int, input().split()))
    lst = []
    
    for x in set(hand):
        lst.append(hand.count(x))
    if lst.count(1) == 3:
        print("ONE PAIR")
    elif lst.count(2) == 2 and lst.count(1) == 1:
        print("TWO PAIR")
    elif lst.count(3) == 1 and lst.count(1) == 2:
        print("THREE CARD")
    elif lst.count(3) == 1 and lst.count(2) == 1:
        print("FULL HOUSE")
    else:
        print("NO PAIR")

if __name__ == "__main__":
    main()

