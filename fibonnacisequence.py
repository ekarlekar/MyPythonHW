x = 0
y = 1
z = x + y
f = int(raw_input("Type in a number:"))
while (z <= f):
    print (z)
    z = x + y
    x = y
    y = z
