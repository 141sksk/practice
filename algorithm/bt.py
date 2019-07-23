from collections import deque

def depth_first_search(T):
    D = deque()
    if len(T) > 0:
        D.append(T)#;show(D)
    while len(D) > 0:
        L, a, R = D.pop()
        print(a, end=',')#;show(D)
        if len(L) > 0:
            D.append(L)#;show(D)
        if len(R) > 0:
            D.append(R)#;show(D)

    print()

def breadth_first_search(T):
    D = deque()
    if len(T) > 0:
        D.append(T)#;show(D)
        while len(D) > 0:
            L, a, R = D.popleft()
            print(a, end=',')#;show(D)
            if len(L) > 0:
                D.append(L)#;show(D)
            if len(R) > 0:
                D.append(R)#;show(D)

    print()

def show(D):
    print('[', end='')
    for(L, a, R) in D:
        print(a, end='<-')
    ptint(']')