import turtle
t=turtle
turtle.pen()
total_angle=360
side=50
step=total_angle/side
size=20
for i in range(0,total_angle,step):
    t.forward(size)
    t.left(step)

x=raw_input("Press enter to quit :")
