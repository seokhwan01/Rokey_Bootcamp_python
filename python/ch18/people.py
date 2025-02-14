import turtle

# 🖌️ 기본 설정
turtle.speed(0)
turtle.bgcolor("white")

# 🖼️ 얼굴 원형
def draw_circle(color, x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

# 🏛️ 정장 (사각형 형태)
def draw_rectangle(color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

# 👔 넥타이
def draw_tie(color, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.goto(x - 10, y - 50)
    turtle.goto(x + 10, y - 50)
    turtle.goto(x, y)
    turtle.end_fill()

# 👀 눈
def draw_eye(x, y):
    draw_circle("white", x, y, 15)  # 흰자
    draw_circle("black", x, y + 5, 7)  # 동공

# 🏛️ 얼굴 배경
draw_circle("tan", 0, 50, 100)  # 얼굴

# 🏛️ 머리카락 (크게 윤곽선만 그림)
draw_circle("black", 0, 130, 80)

# 👀 눈
draw_eye(-35, 80)
draw_eye(35, 80)

# 👃 코
turtle.penup()
turtle.goto(-10, 50)
turtle.pendown()
turtle.color("brown")
turtle.setheading(-60)
turtle.circle(10, 120)

# 👄 입
turtle.penup()
turtle.goto(-25, 30)
turtle.pendown()
turtle.color("black")
turtle.setheading(-30)
turtle.circle(25, 60)

# 🏛️ 정장
draw_rectangle("black", -75, -50, 150, 150)

# 👔 넥타이
draw_tie("gold", 0, -50)

# 🖼️ 터틀 숨기기
turtle.hideturtle()
turtle.done()
