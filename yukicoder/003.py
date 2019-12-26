def bin1(n):
    return bin(n).count("1")

def main():

    goal = int(input())

    Q = [0] * (goal + 1)
    q = [1]
    Q[1] = 1
 
    while q:
        position = q.pop(0)
        print(position)
        stepLength = bin1(position)
        stepCount = Q[position]
        go = position + stepLength
        back = position - stepLength
        if go < goal + 1 and Q[go] == 0:
            Q[go] = stepCount + 1
            q.append(go)
        if back > 0 and Q[back] == 0:
            Q[back] = stepCount + 1
            q.append(back)
        # print(q)

    if Q[goal] != 0:
        print(Q[goal])
    else:
        print(-1)

if __name__ == "__main__":
    main()






