def getFactorial(n):
    if n<=1:
        return 1
    else:
        return n*getFactorial(n-1)
x=int(raw_input("Type in a number:"))
f=getFactorial(x)
print("Factorial of {0} is {1}").format(x,f)
