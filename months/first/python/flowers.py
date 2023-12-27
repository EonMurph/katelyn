from random import randint
import turtle
import time

s = turtle.getscreen()
s.clear()
turtle.bgcolor("#FF8CD0")

t = turtle.Turtle()
t.speed(10)
t.hideturtle()


def change_color(turt, color):
    turt.pencolor(color)
    turt.fillcolor(color)


def petal(turt, radius, angle):
    # Draw a petal
    turt.begin_fill()
    turt.circle(radius, angle)
    turt.lt(180 - angle)
    turt.circle(radius, angle)
    turt.lt((180 - angle))
    turt.end_fill()


def lily_pad(turt, length, start_angle, start_x, start_y):
    # Set the turtle into position
    turt.up()
    turt.goto(start_x, start_y)
    turt.down()

    # Draw the lily pad
    turt.up()
    turt.goto(start_x + 128, start_y - 72)
    turt.down()
    turt.seth(start_angle + 100)
    change_color(turt, "#58b37b")

    # Set values for sides lily pad ellipse
    major_length = length*2 - 30
    minor_length = major_length // 3
    minor_angle = 80
    major_angle = (360-(minor_angle*2)) / 2

    turt.begin_fill()

    # Draw the right side
    turt.circle(minor_length, minor_angle)

    # Draw the top ellipse
    turt.circle(major_length, major_angle)

    # Draw the left side
    turt.circle(minor_length, minor_angle)

    # Draw the bottom ellipse
    turt.circle(major_length, major_angle*.6)
    first_pt = [turt.xcor(), turt.ycor()]
    turt.circle(major_length, major_angle*.2)
    second_pt = [turt.xcor(), turt.ycor()]
    turt.circle(major_length, major_angle*.2)

    turt.end_fill()

    # Get turtle into position
    turt.up()
    turt.goto(first_pt[0], first_pt[1])
    turt.down()

    # Draw the cut
    change_color(turt, "#FF8CD0")

    turt.begin_fill()
    turt.lt(45)
    turt.fd(60)
    turt.rt(140)
    turt.goto(second_pt[0], second_pt[1])
    turt.circle(major_length, major_angle*.2)
    turt.end_fill()


def lotus(turt, length, start_angle, start_x, start_y):
    # Set values for petals
    short_length = length * .45
    arc_angle = 100
    short_arc_angle = 150

    # Set the turtle back to the initial position
    turt.up()
    turt.goto(start_x, start_y)
    turt.down()
    turt.seth(start_angle)

    # Draw the bottom petal
    turt.seth(start_angle + 140)
    change_color(turt, "#d36165")
    turt.up()
    turt.fd(20)
    turt.seth(start_angle + 245)
    turt.down()
    petal(turt, short_length, short_arc_angle)

    # Set the turtle back to the initial positon
    turt.up()
    turt.goto(start_x, start_y)
    turt.down()
    turt.seth(start_angle)

    # Draw the trio
    change_color(turt, "#e88a8e")
    for _ in range(3):
        petal(turt, length, arc_angle)
        turt.lt(90)

    # Draw the double diagonal petals
    change_color(turt, "#d36165")
    turt.seth(start_angle + 45)
    for _ in range(2):
        petal(turt, length, arc_angle)
        turt.lt(95)

    # Draw the shortest/closest petal
    change_color(turt, "#f1a3a6")
    turt.seth(start_angle + 65)
    petal(turt, short_length, short_arc_angle)


length = [100, 70, 70]
start_angle = [-50, 5, -105]
start_x = [0, 261, -270]
start_y = [0, 80, 80]

lily_pad(t, length[0], start_angle[0], start_x[0], start_y[0])
for i in range(len(length)):
    lotus(t, length[i], start_angle[i], start_x[i], start_y[i])

turtle.exitonclick()