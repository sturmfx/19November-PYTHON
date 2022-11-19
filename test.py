import turtle
import random

rnd = random
t = turtle.Turtle()
s = turtle.Screen()
s.setup(800, 800)
t.pencolor("red")

colors = ["red", "blue", "green", "yellow"]


def figure(edges, length_min, length_max):
    g = rnd.randint(length_min,length_max)
    a = round(g / edges)
    b = 5
    c = round(a / (2 * b))
    degree = round(360 / edges)
    d = rnd.randint(0, 100)
    for i in range(edges):
        if d >= 50:
            for j in range(c):
                t.forward(b)
                t.penup()
                t.forward(b)
                t.pendown()
        else:
            t.forward(a)
        t.right(degree)


def randomfig(n, min, max, length_min, length_max):
    for i in range(n):
        x = rnd.randint(-200, 200)
        y = rnd.randint(-200, 200)
        color = rnd.randint(0, len(colors) - 1)
        t.pencolor(colors[color])
        t.penup()
        t.goto(x, y)
        t.pendown()
        figure(rnd.randint(min, max), length_min, length_max)


randomfig(10, 3, 7, 200, 600)
