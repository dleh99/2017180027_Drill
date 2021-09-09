import turtle

count=5
Howmany = 0

while(count>=0):
    if(count==0):
        count=5
        turtle.penup()
        if(Howmany==0):
            turtle.goto(0,0)
        elif(Howmany==5):
            turtle.goto(0,100)
        elif(Howmany==10):
            turtle.goto(0,200)
        elif(Howmany==15):
            turtle.goto(0,300)
        elif(Howmany==20):
            turtle.goto(0,400)
        elif(Howmany==25):
            turtle.exitonclick()
        turtle.pendown()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    count-=1
    Howmany+=1

        
