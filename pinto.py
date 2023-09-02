import turtle

def set_turtle():
    screen = turtle.Screen()
    screen.setup(width=1440, height=810)

    turtle.speed(15)
    turtle.hideturtle()

    turtle.pen(pencolor='#462b0a', fillcolor='#462b0a', pensize=5)

def draw_ball():
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()

def go_to():
    coordinates_list = [
        [-100, -350],
        [100, -350],
        [75, -250],
        [75, 250],
        [0, 295],
    ]

    for coordinates in coordinates_list:
        turtle.penup()
        turtle.goto(coordinates[0], coordinates[1])
        turtle.pendown()

        yield

set_turtle()

go_to_generator = go_to()

next(go_to_generator)
draw_ball()

next(go_to_generator)
draw_ball()

next(go_to_generator)
turtle.setheading(90)

# tronco
turtle.begin_fill()

x = [500, 150, 500, 150]

for i in range(4):
    turtle.forward(x[i])
    turtle.left(90)

turtle.end_fill()

next(go_to_generator)

# cabeça
turtle.pencolor('#b31b43')
turtle.fillcolor('#b31b43')

turtle.begin_fill()
turtle.circle(75, 180)
turtle.end_fill()

next(go_to_generator)

# risco da cabeça
turtle.pen(pencolor='black', fillcolor='black', pensize=7)

turtle.begin_fill()
turtle.backward(30)
turtle.end_fill()

turtle.done()
