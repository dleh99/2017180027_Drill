import turtle

def Move_left():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def Move_down():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def Move_right():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def Move_up():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()
    turtle.stamp()

turtle.shape('turtle')

turtle.onkey(Move_left, 'a')
turtle.onkey(Move_up, 'w')
turtle.onkey(Move_down, 's')
turtle.onkey(Move_right, 'd')
turtle.onkey(restart, 'Escape')
turtle.listen()
