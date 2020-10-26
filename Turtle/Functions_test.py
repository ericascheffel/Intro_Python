""" Bem-vindo ao script-tutorial do módulo turtle!

    Este documento guarda exemplos do uso dos recursos no módulo Turtle!

    Descomente as linhas abaixo para testar as funcionalidades.
"""
import turtle as turtle # Importa o módulo turtle dando nome a ele
from turtle import * # o "*" diz que é para importar tudo o que está dentro do módulo turtle

#window = turtle.Screen() # Cria a tela permanente onde a tartaruga pode andar
#flecha = turtle.Turtle() # criar uma instância da classe Turtle: Uma tartaruguinha com nome 'flecha'

begin_fill() # Este MÉTODO Deve ser chamado SE QUISER preencher a forma que será desenhada
print(flecha.position()) # Este ATRIBUTO do método 'pos' diz a localização atual da 'flecha'.
                          # É necessário a função python print pois o canvas não imprime esta informação.
flecha.color("black", "red")
flecha.circle(80)

end_fill() # Se usar o being_fill() é necessário utilizar o end_fill() ao terminar

#for feitos in range(6):
    #flecha.undo() # apaga o que foi feito

#flecha.speed(10) # Determina velocidade da tartarura: Mais rápido =0, rápido=10, Normal = 6
#flecha.forward(80) # Andar para frente
#flecha.backward(80) # anda para trás
#flecha.right(90) # muda a direção à direita por z°
#flecha.left(90) # muda a direção à esquerda por z°
#flecha.setx(100) # tartaruga vai para a posição x°
#flecha.sety(100) # tartaruga vai para a posição y°
#flecha.setheading(180) # define a orientação da tartaruga em norte(90), leste(0), oeste(180), sul(270)
#flecha.home() # retorna para a posição inicial
#flecha.circle(30,180,3) # cria um círculo. argumentos: raio, tamanho do círcurlo grau°, números de ações
#flecha.dot(50,"blue") # Cria um ponto
#flecha.stamp() #carimba uma cópia da tartaruga na posição dela

#for feitos in range(20):
    #flecha.undo()

#flecha_dois = turtle.Turtle() #Cria uma segunda instância da classe Turtle
#flecha_dois.speed(1)
#flecha_dois.color("blue")
#flecha_dois.fd(10) # alias para o método forward da classe Tnavigator
#flecha_dois.dot(50, "blue") # cria um ponto (diametro,"cor") na origem
#flecha_dois.penup() # "Retira" a caneta do canvas
#flecha_dois.setposition(50,50) # anda até a posição (x,y)
#flecha_dois.pendown() # "Retorna" a caneta para o canvas
#flecha_dois.pensize(20)
#flecha_dois.forward(200)

#flecha_dois.clear()

#tartaruga = turtle.Turtle()

#tartaruga.shape("triangle")
#window.bgcolor("green")
#tartaruga.setx(100)
#tartaruga.sety(300)
#tartaruga.home()
#tartaruga.clear()


#final = turtle.Turtle()
#final.right(90)
#final.color("purple")
#final.shape("turtle") # muda a forma da tartaruga. Aceita as strings : “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
#final.write("Final da Apresentação!", False, "center",('verdana', 20, 'normal')) # escreve um texto segundo os parâmetros:
                                                                                  # arg, move=False/True, align=’left’,'center' or right, font=(fontname, fontsize, fonttype)
#final.hideturtle() #esconde a tartaruga
#mainloop()
#done() #Também é possível usar done(), mas o console reclamou :)


