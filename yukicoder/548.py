def main():

    S = input()
    new_str = sorted(S)
    myList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
<<<<<<< HEAD
    atama = ""
    single_cnt = 0
    double_cnt = 0
=======
    single_cnt = 0
    double_cnt = 0
    ans = ""
>>>>>>> f42c56548300fc5b8680c29225b5e5c9d986b00b
    for ltr in new_str:
        if new_str.count(ltr) == 1:
            single_cnt += 1
            myList.remove(ltr)
        elif new_str.count(ltr) == 2:
            double_cnt += 1
<<<<<<< HEAD
            atama = ltr
    print(single_cnt)
    print(double_cnt)
    if single_cnt == 13:
        for ltr in new_str:
            print(ltr)
    elif single_cnt == 11 and double_cnt == 1:
        myList.remove(atama)
=======
            ans = ltr
    if single_cnt == 13:
        for ltr in new_str:
            print(ltr)
    elif single_cnt == 11 and double_cnt == 2:
        myList.remove(ans)
>>>>>>> f42c56548300fc5b8680c29225b5e5c9d986b00b
        print(myList[0])
    else:
        print("Impossible")

if __name__ == "__main__":
    main()