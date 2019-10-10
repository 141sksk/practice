def main():

    a, b, c, d, e, f = map(int, input().split())
    if (a + c + e) % 2 == 0:
        print(":-)")
    else:
        print(":-(")
        
if __name__ == "__main__":
    main()