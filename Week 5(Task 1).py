

a = input("Enter a sequence of integers:")
lis = list(a)

def longestSubsequence(lis):
    eList = []
    longestL = []
    counter = 1
"""

    for listL in range(0, len(lis), 1):
        No = int(listL)
        for num in lis:
            if num < lis[No]:
                print(lis[No])
                if num in eList:
                    nothing = True
                else:
                    eList.append(num)
            else:
                print(lis[No])
"""

    for i in lis:
        num = int(i)
        if num < lis[counter]:
            eList.append(i)
        else:
            eList.append(i)
            longestL = eList
            eList = []
    counter = counter + 1

    print(eList)
    print(longestL)
    

longestSubsequence(lis)



#created the first list
#append the first ascending sequnce to a new list
#then have the remaining in another list
#compare two lists, first is kept under namespace and is the highest.
#use that to compare to the second sequnce.
#keep going through sequnces until the end.
#the second list should be chnaging to the first list if its bigger.




"""


#This code below works

eList = []

for listL in range(0, len(lis), 1):
    No = int(listL)
    for num in lis:
        if num < lis[No]:
            print(num)
            print(lis[No])
            print("Success")
            if num in eList:
                nothing = True
            else:
                eList.append(num)
        else:
            print(num)
            print(lis[No])
            print("Fail")
"""

