
a = input("Please enter a list: ")
lis = list(a)

low = int(input("Please enter your low number: "))
high = int(input("Please enter your high number: "))


#Function that fills in the gap between the low and high

eList = []

for i in range(low, high+1, 1):
    eList.append(i)

#Function that checks if any value in 'eList' is in the original list

stop = "Not"

for a in lis:
    if stop == "Stop":
        break
    else:
        for b in eList:
            if str(b) == str(a):
                print("True")
                stop = "Stop"



