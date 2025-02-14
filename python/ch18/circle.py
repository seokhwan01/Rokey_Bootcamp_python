import turtle
def circle_color(t):
    color_list=["red","orange","yellow","green","blue","navy","purple"]
    radius=50
    for i in color_list:
        t.pencolor(i)
        t.circle(radius)
        radius+=5
        
turtle.title("원 그리기")
turtle.setup(800,500)
turtle.bgcolor("black")
t=turtle.Turtle()
t.shape("turtle")
t.pensize(2)
t.speed(0)
circle_color(t)

turtle.exitonclick()