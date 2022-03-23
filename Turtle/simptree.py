from turtle import *
TAO = 30
BRC = 8

COLORS = "red maroon green blue cyan purple".split() * 10


def tree(head, deep):
    if deep <= 1:
        return
    colour = COLORS[deep//BRC]
    for tao in [-TAO, TAO]:
        _heading = head+tao
        setheading(_heading)
        color(colour)
        forward(deep)
        tree(_heading, deep-BRC)
        setheading(_heading)
        color(colour)
        back(deep)
    # return


penup()
setpos(0, -200)
pendown()
speed(0)
setheading(90)
forward(100)
tree(90, BRC*8)
done()
