def least_common_multiple(x, y):
    for k in range(1, y + 1):
        if x * k % y == 0:
            return x * k
        else:
            continue

def main():

    n = int(input())
    a, b, c = map(int, input().split())
    AB = least_common_multiple(a, b)
    BC = least_common_multiple(b, c)
    CA = least_common_multiple(c, a)
    ABC = least_common_multiple(AB, c)
    A = n // a
    B = n // b
    C = n // c
    A_B = n // AB
    B_C = n // BC
    C_A = n // CA
    A_B_C = n // ABC
    ans = A + B + C - A_B - B_C - C_A + A_B_C
    print(ans)

if __name__ == "__main__":
    main()