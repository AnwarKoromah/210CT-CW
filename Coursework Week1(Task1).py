import random


def RandomList(lis):
    L = []
    b = True
    while b == True:
        a = random.choice(lis)
        c = len(lis)
        d = len(L)
        if a in L:
            if c == d:
                print(L)
                break
        else:
            L.append(a)
    

inp = input("Enter a sequence of numbers")
lis = list(inp)
RandomList(lis)
