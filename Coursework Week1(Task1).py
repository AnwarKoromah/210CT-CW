import random

#Uses random.choice to add random items from original list to new list

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
                #Break will stop the loop when all values are in new list
                break
        else:
            L.append(a)
    

inp = input("Enter a sequence of numbers: ")
#Allows the user to enter double digits to the list
lis = []
x = inp.split(",")
for i in x:
        z = int(i)
        lis.append(z)

RandomList(lis)
