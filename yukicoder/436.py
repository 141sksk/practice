def main():
    S = input()
    c = S.count("c")
    w = S.count("w")
    if c - 1 > w:
        print(w)
    else:
        print(c - 1)

if __name__ == "__main__":
    main() 