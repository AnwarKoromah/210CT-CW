
def longestSubsequence(lis):
    eList = []
    longestL = []
    counter = 1

    for i in lis:
            num = int(i)
            if counter == len(lis):
                    eList.append(i)
                    if len(longestL) < len(eList):
                                longestL = eList
            else:
                    if num < lis[counter]:
                        eList.append(i)
                    else:
                        eList.append(i)
                        if len(longestL) < len(eList):
                                longestL = eList
                        eList = []
            counter = counter + 1
    print("Longest sub-sequence: " + str(longestL))


eList = []
a = input("Enter a sequence of numbers sepearted by commas: ")
b = a.split(",")
for i in b:
        z = int(i)
        eList.append(z)

longestSubsequence(eList)
