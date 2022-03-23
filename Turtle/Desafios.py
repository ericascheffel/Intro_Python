"""Bem-vindo à sala de desafios!

   Você pode salvar todo o seu progresso aqui também!
   Organize está página como quiser!

   Desafie-se!
"""
######################################
# TÓPICOS: Sintaxe, padrões e Funções
######################################

"""
DESAFIO 1: Crie algo com o turtle:
"""

"""
DESAFIO 2: Relembre o uso de padrões usando a ITERAÇÃO para criar um desenho/figura/forma:
"""

"""
DESAFIO 3: Crie uma função que possibilite criar desenhos|figuras|formas com base em alguns argumentos 
"""

"""
DESAFIO 4: Crie uma função que ao ser chamada crie uma 'ÁRVORE'.

Dica1: Fractal (do latim fractu: fração, quebrado) é uma figura da geometria não clássica muito encontrada 
       na natureza, isto é, um objeto em que suas partes separadas repetem os traços (a aparência) 
       do todo completo (padrão repetitivo)
Dica2: https://aidobonsai.files.wordpress.com/2011/10/fractaltree.jpg
Dica3: https://3.bp.blogspot.com/-vX49qkQWs20/Tud4BfpN2tI/AAAAAAAAAXA/5r-PkWbqGeU/s1600/%25C3%2581rvore.jpg

color('red', 'maroon')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
"""
from turtle import *
from random import randint, choice
from math import sqrt

COLORS = "red yellow green blue cyan purple".split()


class Volpi:
    def __init__(self):
        penup()
        colour, fill = choice(COLORS), choice(COLORS)
        color(colour, fill)
        side, x, y = randint(20, 90), randint(-200, 200), randint(-200, 200)
        setpos(x, y)
        pendown()
        hipo = sqrt(2*(side**2))/2
        begin_fill()
        left(90)
        forward(side)
        right(90)
        forward(side)
        right(90)
        forward(side)
        right(90+45)
        forward(hipo)
        left(90)
        forward(hipo)
        right(180+45)
        end_fill()


class Volper:
    def __init__(self):
        penup()
        colour, fill = choice(COLORS), choice(COLORS)
        color(colour, fill)
        side, x, y, t = randint(20, 90), 0, 0, randint(1, 90)
        setpos(x, y)
        pendown()
        hipo = sqrt(2*(side**2))/2
        begin_fill()
        left(90)
        forward(side)
        right(90)
        forward(side)
        right(90)
        forward(side)
        right(90+45)
        forward(hipo)
        left(90)
        forward(hipo)
        right(180+45)
        end_fill()


for _ in range(50):
    speed("fast")
    Volpi()
done()
