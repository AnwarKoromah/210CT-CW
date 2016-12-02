#Input and split it by spaces
sentence = input("Please enter a sentence")
lis = sentence.split(" ")
eList = []

def reverseString(lis):
    #Iterate the list beackwards
    for a in range(len(lis)-1, 0, -1):
        eList.append(lis[a])
    eList.append(lis[0])
    print(" ".join(eList))

reverseString(lis)
