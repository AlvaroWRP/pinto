import turtle

screen = turtle.Screen()
screen.setup(width=1440, height=810)

turtle.speed(15)
turtle.hideturtle()

turtle.pen(pencolor='#462b0a', fillcolor='#462b0a', pensize=5)

turtle.penup()
turtle.goto(-100, -350)
turtle.pendown()

# bola 1
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

turtle.penup()
turtle.goto(100, -350)
turtle.pendown()

# bola 2
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

turtle.penup()
turtle.goto(75, -250)
turtle.pendown()

turtle.setheading(90)

# tronco
turtle.begin_fill()

x = [500, 150, 500, 150]

for i in range(4):
    turtle.forward(x[i])
    turtle.left(90)

turtle.end_fill()

turtle.penup()
turtle.goto(75, 250)
turtle.pendown()

# cabeça
turtle.pencolor('#b31b43')
turtle.fillcolor('#b31b43')

turtle.begin_fill()

turtle.circle(75, 180)

turtle.end_fill()

turtle.penup()
turtle.goto(0, 295)
turtle.pendown()

# risco da cabeça
turtle.pencolor('black')
turtle.fillcolor('black')
turtle.pensize(7)

turtle.begin_fill()

turtle.backward(30)

turtle.end_fill()

turtle.done()
