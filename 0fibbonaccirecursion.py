def fib(n):
    if (n==1):
        return (1)
    elif (n==0):
        return (0)
    else:
        return (fib (n-1)+ fib(n-2))

n=int(raw_input("Type in a number:"))
y=0
x=0
while x<=n:
    x= fib(y)
    if (x<=n):
        print(x)
    y=y+1
