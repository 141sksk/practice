def main():
  
    n = int(input())
    itemList = []
    count = 0
    for _ in range(n):
        items = list(map(int, input().split()))
        itemList += items
    itemCount = len(itemList)
    for i in range(1, 11):
        amount = itemList.count(i)
        if amount % 2 == 0:
            count += amount / 2
            itemCount -= amount
        elif amount >= 3:
            count += amount // 2
            itemCount -= (amount - 1)
    count += itemCount // 4
    print(int(count))
    
if __name__ == "__main__":
    main()