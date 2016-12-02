#Function to check if a number is a prime number

"""
for a in range(num-1, 1, -1):
    if num % a == 0:
        b = False
        break
    else:
        b = True


if b is True:
    print("This number is PRIME")
else:
    print("This number is NOT PRIME")
"""


def IsPrimeOrNah(num, nextN):
    if num == 1:
        print("Nah")
    else:
        if num % nextN == 0:
            print("Nah")
        else:
            if nextN == 2:
                print("Prime")
            else:
                nextN = nextN-1
                IsPrimeOrNah(num, nextN)
        

num = int(input("Please enter a number: "))
nextN = num-1
IsPrimeOrNah(num, nextN)
