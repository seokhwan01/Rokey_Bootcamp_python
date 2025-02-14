import turtle
turtle.title("미애니")
turtle.setup(700,500)
turtle.bgcolor("beige")

t=turtle.Turtle()
t.shape('turtle')
t.pensize(2)
t.speed(10)
n=300
for i in range(n):
   t.forward(i)
   t.right(91)
# t.color("black","olive")
# t.begin_fill()
# t.circle(20)
# t.end_fill()
# t.pencolor("skyblue")
# t.pensize(7)

# n,l=map(int,input().split())
# t.begin_fill()
# for i in range(n):
#     t.right(360/n)
#     t.forward(l)
# t.end_fill()

turtle.done()