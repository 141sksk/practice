def main():
    Sa, Pa, Xa = map(str, input().split())
    Sb, Pb, Xb = map(str, input().split())
    if int(Pa) > int(Pb):
        print(Sa)
    elif int(Pb) > int(Pa):
        print(Sb)
    else:
        print("-1")
if __name__ == "__main__":
    main()