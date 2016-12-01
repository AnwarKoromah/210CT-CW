def PerfectSquare(a):
    num = int(a)
    for i in range(1, num, 1):
        if i * i <= num:
            result = i
        else:
            break
    print("The highest perfect square is: "+str(result)+"\ni.e:"+"("+ str(i-1)+"*"+str(i-1)+"="+str((i-1)*(i-1))+")")


a = input("Enter the number you would like to check: ")
PerfectSquare(a)
