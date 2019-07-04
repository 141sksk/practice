def main():
    s1, s2 = map(str, input().split())
    if s1 == "Sun" or s1 == "Sat":
        if s2 == "Sun" or s2 == "Sat":
            print("8/33")
        else:
            print("8/32")
    else:
        print("8/31")


if __name__ == "__main__":
    main()