import turtle
from turtle import Turtle, Screen, colormode
import random

t = Turtle()
s = Screen()

# t.shape("turtle")

# Draw a square
# t.pencolor("red")
# for i in range(4):
#     t.forward(100)
#     t.right(90)

# Draw spaces lines
# for i in range(10):
#     t.forward(10)
#     t.penup()
#     t.forward(10)
#     t.pendown()

# Random shapes from Triangle to shape with 10 sides
# def shape_creator(sides):
#     angle = 360/sides
#     for i in range(sides):
#         t.forward(100)
#         t.right(angle)
#
#
# colormode(255)
# t.pensize(3)
# for shape in range(3, 11):
#     tup = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     print(tup)
#     shape_creator(shape)
#     t.color(tup)
#
# s.exitonclick()

# Random walk
# t.pensize(5)
# colormode(255)
# directions = [0, 90, 180, 270]
# for walk in range(100):
#     t.speed(0)
#     tup = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     t.color(tup)
#     t.setheading(random.choice(directions))
#     t.forward(20)

# Draw a Spirograph
# t.pensize(3)
colormode(255)
t.speed(0)


def draw_spirograph(size_of_gap):
    for r in range(int(360 / size_of_gap)):
        tup = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        t.color(tup)
        t.circle(150)
        current_heading = t.heading()
        t.setheading(current_heading + size_of_gap)


draw_spirograph(5)
