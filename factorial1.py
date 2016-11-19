def print_number(x):
    product=1
    while (x>0):
        product=product*x
        x=x-1
    return product


n=int(raw_input("Type in a number:"))
f=print_number(n)
print("Factorial is:", f)
