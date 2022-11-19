#Importación de librería, se le define la alineación y la fuente.
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Times New Roman", 24, "normal")

#Se crea una clase con cuatro funciones para la barra de puntaje, la cuál se define como un objeto Turtle, es decir, un gráfico.
class Scoreboard(Turtle):
    #La función init da la inicialización al objeto y sus propiedades, como lo son puntaje inicial, color, que no quede trazo (penup), ubicación, esconder el gráfico (Turtle) y la propiedad updateScoreboard.
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("aquamarine")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.updateScoreboard()
    #La función updateScoreboard actualiza la barra de puntaje la cuál incrementará a medida que la culebra coma. A esta se le define la alineación y la fuente asignadas en la importación.
    def updateScoreboard(self):
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)
    #la función gameOver muestra el mensaje "GAME OVER >:D" cuando la culabra colisione contra el límite del juego (pared) o contra su propio cuerpo.
    def gameOver(self):
        self.goto(0, 0)
        self.write("GAME OVER, DUDE >:D", align = ALIGNMENT, font = FONT)
    #La función increaseScore incrementa el puntaje cada vez que la culebra coma y lo actualiza en la barra de puntaje.
    def increaseScore(self):
        self.score += 1
        self.clear()
        self.updateScoreboard()