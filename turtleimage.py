import turtle

ANIMATION_SPEED = 10
NUM = 3
turtle.speed(ANIMATION_SPEED)
triangle = turtle.Turtle()
triangle.pencolor("pink")
triangle.fillcolor("light blue")

triangle.begin_fill()
for x in range (NUM):
    triangle.forward(100)
    triangle.left(120)
    triangle.forward(100)
    triangle.left(120)
    triangle.forward(100)
triangle.end_fill()

turtle.done()
