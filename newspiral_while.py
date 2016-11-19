import turtle
t=turtle
t.up()
t.goto(100,0)
t.down()
t.pensize(3)
angle = 20
increment = 0.25
x=0
loop_size = 25
colors=['red','green','purple', 'orange']
while x<loop_size:
    t.pencolor()
    t.forward(x)
    t.left(angle)
    x=x+increment

x=raw_input("Press enter to quit :")
