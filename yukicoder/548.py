def main():

    S = input()
    new_str = sorted(S)
    myList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
    single_cnt = 0
    double_cnt = 0
    ans = ""
    for ltr in new_str:
        if new_str.count(ltr) == 1:
            single_cnt += 1
            myList.remove(ltr)
        elif new_str.count(ltr) == 2:
            double_cnt += 1
            ans = ltr
    if single_cnt == 13:
        for ltr in new_str:
            print(ltr)
    elif single_cnt == 11 and double_cnt == 2:
        myList.remove(ans)
        print(myList[0])
    else:
        print("Impossible")

if __name__ == "__main__":
    main()