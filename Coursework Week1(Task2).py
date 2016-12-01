def Factorial(factNo):
    factorial = 1
    for i in range(1, factNo + 1):
        factorial = factorial * i 
    return(factorial)


#Count number of 0s in the result
def CountZeros(exampleNum)
    exampleNum = factorial
    lis = list(str(exampleNum))
    final = 0 
    for a in lis:
        aa = int(a)
        if aa == 0:
            final += 1
    print(final)




factNo = int(input("Please enter a number."))
Factorial(factNo)
CountZeros(factorial)












"""
factNo = int(input("Please enter a number."))

factorial = 1

for i in range(1, factNo + 1):
    factorial = factorial * i 
print(factorial)


#Count number of 0s in the result

exampleNum = factorial

lis = list(str(exampleNum))


final = 0 

for a in lis:
    aa = int(a)
    if aa == 0:
        final += 1

print(final)



"""
