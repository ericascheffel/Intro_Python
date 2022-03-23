from turtle import *
from random import choice
# from math import log
TAO = 360-120
BRC = 2

COLORS = "red yellow green blue cyan purple".split()


def tree(side, deep):
    if deep <= 1:
        return
    colour, fill = choice(COLORS), choice(COLORS)
    color(colour, fill)
    inside = side/2
    deepl = deep**4/3000
    begin_fill()
    right(TAO)
    forward(side)
    sier(inside, deep-1)
    right(TAO)
    forward(side)
    sier(inside, deep-1)


    # tree(head-TAO, deep-BRC)
    right(TAO)
    forward(side)
    sier(inside, deep - 1)
    # tree(head-TAO, deep-BRC)
    right(TAO)
    forward(side)
    # tree(head-TAO, deep-BRC)
    end_fill()

    return


def sier(side, deep):
    if deep <= 1:
        return
    inside = side/2
    tree(inside, deep)
    forward(inside)
    tree(inside, deep)
    forward(inside)
    tree(inside, deep)
    forward(inside)


penup()
setpos(400, -300)
pendown()
speed(0)
sier(800, 5)
done()
