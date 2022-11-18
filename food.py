#Importación de librerias necesarias para el objeto correspondiente a la comida
from turtle import Turtle
import random

#Se crea una clase con dos funciones para la comida, la cuál se define como un objeto Turtle, es decir, un gráfico.
class Food(Turtle):
    #La función init da la inicialización al objeto y sus propiedades, como lo son forma de circulo, que no quede trazo (penup), el tamaño de la forma, el color, la velocidad de aparición y la propiedad refresh.
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()
    #La función refresh (la cuál es una propiedad para el objeto de la comida) se encarga de ubicar la comida en un lugar aleatorio de la pantalla cuando inicia el juego y cada vez que la culebra colisiona con la comida.
    def refresh(self):
        randomX = random.randint(-280, 280)
        randomY = random.randint(-280, 280)
        self.goto(randomX, randomY)