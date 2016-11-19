import turtle
def draw_ring(tu,start_x,start_y,pen_color,pen_size):
    tu.up()
    tu.goto(start_x, start_y)
    tu.down()
    tu.pensize(pen_size)
    tu.circle(30)

t=turtle
colors=['blue','black','red', 'yellow', 'green']
pen_color=t.pencolor
draw_ring(t,-100,100,t.pencolor(colors[0]), 3)
draw_ring(t,-35,100, t.pencolor(colors[1]), 3)
draw_ring(t,30,100, t.pencolor(colors[2]), 3)
draw_ring(t,-67,65, t.pencolor(colors[3]), 3)
draw_ring(t,-2,65, t.pencolor(colors[4]), 3)
t.hideturtle()
x=raw_input("Press enter to quit :")
