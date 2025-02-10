import turtle
def star(t):
    color_list=["red","yellow","blue","green","purple"]
    for i in range(5):
        t.pencolor(color_list[i])
        t.fd(100)
        t.right(145)

turtle.title("별 만들기")
turtle.setup(1000,800)
turtle.bgcolor("beige")
t=turtle.Turtle()
t.shape('turtle')
t.pensize(2)
t.speed(0)
star(t)
turtle.exitonclick()