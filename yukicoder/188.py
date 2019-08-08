def main():

    ans = 0
    for month in range(1, 13):
        for day in range(1, 31):
            if day // 10 + day % 10 == month:
                ans += 1

    print(ans)

if __name__ == "__main__":
    main()