#Function to check if a number is a prime number

"""

#If num % number below, returns a float then do again for the next number
#If you get an int returned then stop the loop and say it isn't prime.

#2 is th eonly even prime, so if even then return not prime
#0 and 1 are not considered prime numbers

#range works like this = range(start, stop, step), step is how to count

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







