def main():
  
    flags = list(map(int, input().split()))
    if flags[3] == 1:
        print("SURVIVED")
    elif flags.count(1) < 2:
        print("SURVIVED")
    else:
        print("DEAD")

if __name__ == "__main__":
    main()