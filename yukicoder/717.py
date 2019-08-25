def main():
  
    N, M = map(int, input().split())
    S = input()
    T = input()
    SA, SB, TA, TB = S.count("A"), S.count("B"), T.count("A"), T.count("B")
    print(min(SA, TA) + min(SB, TB))

if __name__ == "__main__":
    main()