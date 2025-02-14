import turtle

# 🐶 강아지 얼굴 그리기
def draw_circle(color, x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)  # 원의 중심을 기준으로 이동
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

# 🐶 강아지 귀 그리기
def draw_ear(color, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.goto(x - 40, y - 50)
    turtle.goto(x, y - 90)
    turtle.goto(x + 40, y - 50)
    turtle.goto(x, y)
    turtle.end_fill()

# 🐶 강아지 얼굴
turtle.speed(3)
turtle.bgcolor("white")

# 얼굴
draw_circle("tan", 0, -50, 100)

# 귀 (왼쪽, 오른쪽)
draw_ear("saddlebrown", -80, 80)
draw_ear("saddlebrown", 80, 80)

# 눈 (왼쪽, 오른쪽)
draw_circle("white", -35, 30, 20)
draw_circle("white", 35, 30, 20)
draw_circle("black", -35, 35, 8)
draw_circle("black", 35, 35, 8)

# 코
draw_circle("black", 0, -10, 12)

# 입 (간단한 곡선)
turtle.penup()
turtle.goto(-20, -40)
turtle.pendown()
turtle.color("black")
turtle.setheading(-60)
turtle.circle(20, 120)

turtle.hideturtle()
turtle.done()
