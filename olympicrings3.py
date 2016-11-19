import turtle

def draw_ring(tu,o_x,o_y,start_x,start_y,pen_color,pen_size):
    tu.up()
    tu.goto(o_x+start_x, o_y+start_y)
    tu.down()
    tu.pensize(pen_size)
    tu.circle(30)


def draw_olympics(tu,o_x,o_y):
    tu.up()
    tu.goto(o_x,o_y)
    colors=['blue','black','red', 'yellow', 'green']
    draw_ring(tu,o_x,o_y,-100,100,tu.pencolor(colors[0]), 3)
    draw_ring(tu,o_x,o_y,-35,100, tu.pencolor(colors[1]), 3)
    draw_ring(tu,o_x,o_y,30,100, tu.pencolor(colors[2]), 3)
    draw_ring(tu,o_x,o_y,-67,65, tu.pencolor(colors[3]), 3)
    draw_ring(tu,o_x,o_y,-2,65, tu.pencolor(colors[4]), 3)



tu=turtle
draw_olympics(tu,0,0)
draw_olympics(tu,-150,150)
draw_olympics(tu,150,150)
draw_olympics(tu,-150,-150)
draw_olympics(tu,150,-150)
tu.hideturtle()

x=raw_input("Press enter to quit :")
