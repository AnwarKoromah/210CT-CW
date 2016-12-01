
lis = [1,2,3,4,1,2,3,1,2,3,4,5]
longestL = []
counter = 1
eList = []


for i in lis:
        num = int(i)
        print(counter)
        if counter == len(lis):
                eList.append(i)
                break
        else:
                if num < lis[counter]:
                    eList.append(i)
                else:
                    eList.append(i)
                    if len(longestL) < len(eList):
                            longestL = eList
                    eList = []
        counter = counter + 1
print(eList)
print(longestL)
