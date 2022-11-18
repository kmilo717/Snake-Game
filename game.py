#Importación de librerias (funciones) que ayudarán a crear el juego.
#las funciones "snake", "food" y "scoreboard" provienen de otros archivos python en los cuáles se les asignan las debidas propiedades a cada objeto (función).
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#Screen properties:
#Se define una variable que será la pantalla del juego, a esta misma se le define propiedades como las dimensiones (alto y ancho), el color de fondo, el título y el método tracer para que los cuadros que conforman el cuerpo de la culebra se vean unidos constantemente.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

#Definición de variables asignándo las funciones importadas.
snake = Snake()
food = Food()
scoreboard = Scoreboard()

#Movement commands:
#Se dan las instrucciones de movimiento del cuerpo de la serpiente con las teclas del teclado
screen.listen
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#Movement cicle:
#Mientras se esté jugando, la pantalla irá actualizándose y se generará movimiento a la culebra.
playingGame = True
while playingGame:
    screen.update()
    time.sleep(0.2)
    snake.move()
    #Collision with food:
    #Cuando se da la colisión de la culebra con la comida, ejecuta las funciones de generar más comida (refresh), de incrementar el tamaño de la culebra (extend) y de aumentar el puntaje en pantalla (increaseScore).
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increaseScore()
    #Collision with wall:
    #Cuando se da la colisión de la culebra con alguna de las paredes, ejecuta la función de parar el juego (False) y de mostrar el mensaje "GAME OVER >:D".
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        playingGame = False
        scoreboard.gameOver()
    #Collision with body:
    #Cuando se da la colisión de la culebra con alguna de las paredes, ejecuta la función de parar el juego (False) y de mostrar el mensaje "GAME OVER >:D".
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            playingGame = False
            scoreboard.gameOver()

#Método con la funcionalidad de que al ejecutar el juego, se salga únicamente dando click en el botón de salida (exit).
screen.exitonclick()




'''
----------PART OF THE INITIAL CODE----------

#Snake properties
segments = []
for position in startingPosition:
    newSegment =Turtle("square")
    newSegment.color("white")
    newSegment.penup()
    newSegment.goto(position)
    segments.append(newSegment)

#Snake properties
firstSegment = Turtle("square")
firstSegment.color("white")

secondSegment = Turtle("square")
secondSegment.color("white")
secondSegment.goto(-20, 0)

thirdSegment = Turtle("square")
thirdSegment.color("white")
thirdSegment.goto(-40, 0)

'''