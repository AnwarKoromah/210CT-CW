#Program that removes all the vowels from a string

#word = input("Please enter a string")

#strings are immutable so need to create a new string

#lenOfStr = len(word)

#Create new str(maybe add charcters to list then turn list into string)
#If first charcter =a,e,i,o,u then remove it
#If not then add the charcter to the new str
#For as many times as the string length

myList = []
vowels = ["a","e","i","o","u"]


a = input("Enter a string")


for letter in a:
    if letter not in vowels:
        myList.append(letter)

print("".join(myList))
