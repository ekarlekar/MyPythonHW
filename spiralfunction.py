import turtle

def draw_spiral(myturtle,start_x,start_y,spiral_size, pen_size):
    t=myturtle
    t.up()
    t.goto(start_x, start_y)
    t.down()
    t.pensize(pen_size)
    angle = 20
    increment = 0.25
    x=0
    loop_size = spiral_size
    colors=['red','green','purple', 'orange']
    while x<loop_size:
        t.pencolor(colors[int(x%len(colors))])
        t.forward(x)
        t.left(angle)
        x=x+increment

timmy_todd = turtle
draw_spiral(timmy_todd, 100,100, 25, 3)
draw_spiral(timmy_todd, -100,-100, 25, 3)
x=raw_input("Press enter to quit :")
