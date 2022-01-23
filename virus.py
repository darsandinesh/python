import turtle
a=0
b=0
turtle.bgcolor("black")
turtle.speed(10)
turtle.pencolor("red")
turtle.penup()
turtle.goto(0,200)
turtle.pendown()
turtle.setheading(33)

while True:
    turtle.forward(a)
    turtle.right(b)
    a+=4
    b+=1
