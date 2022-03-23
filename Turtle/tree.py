from turtle import *
from math import log
TAO = 40
BRC = 2

COLORS = "red maroon green blue cyan purple".split() * 10


def tree(head, deep):
    if deep <= 1:
        return
    deepl = deep**4/4000
    colour = COLORS[deep//BRC]
    for tao in [-TAO, TAO]:
        _heading = head+tao
        setheading(_heading)
        color(colour)
        forward(deepl)
        _ = [_ for _ in tree(_heading, deep-BRC)]
        setheading(_heading)
        color(colour)
        back(deepl)
        yield
    return


penup()
setpos(0, -100)
pendown()
speed(0)
_ = [_ for _ in tree(270-180, BRC*13)]
done()
