from turtle import *
from random import choice

TAO = 360-60
TAO = 120
THE = 60
BRC = 2
ANG = [-THE, TAO]*2

COLORS = "red yellow green blue cyan purple".split()
class Koch:
    def __init__(self):
        self.frac= [self.fixflake, self.fixflake, self.fixflake, self.fixflake]
        self.end = [self.line]*4
    def line(self, side, deep):
        forward(side)
        
    def flake(self, side, deep):
        going = heading()
        side = side/3
        deep -= 1
        do = self.frac if deep else self.end
        #do = self.end
        for go, a in zip (do, ANG):
            go(side, deep)
            right(a)
        
    def fixflake(self, side, deep):
        self.flake(side, deep)
        left(TAO)

    def flakes(self, side, deep):
        [self.flake(side, deep) for _ in "abc"]


penup()
setpos(-300, 200)
pendown()
color(COLORS[0])
speed(0)
#side(200, 5)
Koch().flakes(600,5)
done()
