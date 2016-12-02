
"""
myList = []
vowels = ["a","e","i","o","u"]


a = input("Enter a string")
lis = list(a)


for letter in a:
    if letter not in vowels:
        myList.append(letter)

print("".join(myList))

if str(lis[counter]) not in vowels:
        myList.append(lis[counter])

    
    counter = counter + 1
    print("".join(myList))
"""
counter = 0
eList = []

def removeVowels(lis, counter, eList):
    vowels = ["a","e","i","o","u"]
    if counter == len(lis):
        print("".join(eList))
    else:
        if lis[counter] in vowels:
            counter = counter + 1
            removeVowels(lis, counter, eList)
        else:
            eList.append(lis[counter])
            counter = counter + 1
            removeVowels(lis, counter, eList)
    

a = input("Enter a string")
b = str(a)
lis = list(b)

removeVowels(lis, counter, eList)
