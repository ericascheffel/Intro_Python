import turtle as turtle
from turtle import *

window = turtle.Screen()
flecha = turtle.Turtle()


def constroi_flor(petala,torcao):
    flecha.speed(1)
    color('red', 'yellow')
    begin_fill()  # iniciar a tartaruga no ponto (O,O)
    while True:
        forward(petala)
        left(torcao)
        if abs(pos()) < 1:
            break
    end_fill()
    done()


def triangulo():
    for i in range(3):
        flecha.forward(100)
        flecha.left(120)


def triangule():
    pen = turtle.Pen()
    pen.forward(100)
    pen.left(120)
    pen.forward(100)
    pen.left(120)
    pen.forward(100)


def cuadrado():
    for i in range(4):
        flecha.forward(100)
        flecha.left(90)


def quadrado():
    pen = turtle.Pen()
    pen.forward(100)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
    pen.forward(100)


def pentagono():
   for i in range(5):
      flecha.forward(100)
      flecha.left(72)


def formas(lado, num_lados, angulo):
     """ Desenha sequências de segmentos eventualmente produzindo formas fechadas."""
     for i in range(num_lados):
         flecha.left(angulo)
         flecha.forward(lado)
     done()


def figura():
    flecha.speed(2)
    for i in range(30):
        flecha.circle(5*i)
        flecha.circle(-5*i)
        flecha.left(i)
    #flecha.exitonclick()


def draw_Square_Spiral(flecha, lineLen):
    if lineLen > 0:
        flecha.forward(lineLen)
        flecha.right(90)
        draw_Square_Spiral(flecha,lineLen-2)


def tree(branchLen,flecha):
    #flecha.speed(1)
    if branchLen > 5:
        flecha.forward(branchLen) # desenha tronco
        flecha.color("green")
        flecha.right(20) # vira caneta 20° para direita
        tree(branchLen-10,flecha) # chama a função do início reduzindo o galho
        flecha.left(40) # Desfaz as rotações à direita
        tree(branchLen-10,flecha) #chama a função do início reduzindo o galho
        flecha.right(20) # rotaciona para fazer o ramo da esquerda
        flecha.backward(branchLen) # retorna para o nó anterior

def main():
    flecha.left(90)
    flecha.up()
    flecha.backward(100)
    flecha.down()
    flecha.color("brown")
    flecha.width(5)
    tree(75,flecha)
    done()

#main()

def tree(branchLen,flecha):
    #flecha.speed(1)
    if branchLen > 5:
        flecha.forward(branchLen) # desenha tronco
        #flecha.color("green")
        flecha.right(20) # vira caneta 20° para direita
        tree(branchLen-10,flecha) # chama a função do início reduzindo o galho
        flecha.left(40) # Desfaz as rotações à direita
        tree(branchLen-10,flecha) #chama a função do início reduzindo o galho
        flecha.right(20) # rotaciona para fazer o ramo da esquerda
        flecha.backward(branchLen) # retorna para o nó anterior

def main():
    flecha.left(90)
    flecha.up()
    flecha.backward(100)
    flecha.down()
    flecha.color("brown")
    flecha.width(5)
    tree(75,flecha)
    done()

main()

#draw_Square_Spiral(flecha, 100)
#constroi_flor(100,190)
#formas(100,8,45)
#figura()

#print(bool(1+1 or 2+2))
#print(1+1 or 2+2)

#print(bool(1+1 and 2+2))
#print(1+1 and 2+2)

#x = None or 3
#print(x)