import turtle
t=turtle
turtle.pen()
colors=['blue','black','red', 'yellow', 'green']
pen_color=t.pencolor
def draw_rings(my_ring,start_x,start_y,pen_color,pen_size):
    t=my_ring
    t.up()
    t.goto(start_x, start_y)
    t.down()
    t.pensize(pen_size)
    colors=['blue','black','red', 'yellow', 'green']
    pen_color=t.pencolor
    t.circle(30)

one_ring = turtle
draw_rings(one_ring,-100,100,t.pencolor(colors[0]), 3)
draw_rings(one_ring,-35,100, t.pencolor(colors[1]), 3)
draw_rings(one_ring,30,100, t.pencolor(colors[2]), 3)
draw_rings(one_ring,-67,65, t.pencolor(colors[3]), 3)
draw_rings(one_ring,-2,65, t.pencolor(colors[4]), 3)

x=raw_input("Press enter to quit :")
