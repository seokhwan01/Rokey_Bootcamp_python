import turtle
turtle.title("무지개")
turtle.setup(800,700)
turtle.bgcolor("black")

t=turtle.Turtle()
t.pensize(10)
t.shape("turtle")
t.speed(10)
color_list=["red","orange","yellow","green","blue","navy","purple"]

def rainbow(t):
    radius,x,y=map(int,input("radius x y : ").split())
    diffence = int(radius/10)
    for i in color_list:
        t.setheading(90)
        t.pencolor(i)
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.circle(radius,180)
        radius+=diffence
        x+=diffence
    t.hideturtle()
rainbow(t)
turtle.exitonclick()