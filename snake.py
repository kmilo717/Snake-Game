#Importación de librería, se define la posición inicial, la distancia de movimiento y los giros (en grados) de la culebra.
from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

#Se crea una clase con nueve funciones para la culebra.
class Snake:
    #La función init da la inicialización al objeto y sus propiedades, donde define los segmentos y crea el cuerpo del objeto.
    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]
    #La función createSnake da la posición inicial de la culebra al iniciar o reiniciar el juego.
    def createSnake(self):
        for position in STARTING_POSITION:
            self.addSegment(position)
    #La función addSegment se encarga de agregar nuevos segmentos (aumentar el largo del cuerpo de la culebra) cuando esta come. Se define su forma, el color, que no quede trazo, dar su respectiva ubicación y adjuntar al cuerpo el segmento nuevo.
    def addSegment(self, position):
        newSegment = Turtle("square")
        newSegment.color("grey")
        newSegment.penup()
        newSegment.goto(position)
        self.segments.append(newSegment)
    #La función extend da el nuevo segmento al cuerpo de la culebra.
    def extend(self):
        self.addSegment(self.segments[-1].position())
    #La función move ejecuta el movimiento del cuerpo de la culebra (segmentos) a través del eje x y el eje y de la pantalla. El movimiento se da cada 20 pixeles.
    def move(self):
        for segNum in range(len(self.segments) -1, 0, -1):
            newX = self.segments[segNum -1].xcor()
            newY = self.segments[segNum -1].ycor()
            self.segments[segNum].goto(newX, newY)
            self.head.forward(MOVE_DISTANCE)
    #La función up determina que en caso de que se accione la tecla de la flecha hacia abajo con la culebra dirigiéndose hacia arriba, esta siga el trayecto que lleva para no colisionar con su propio cuerpo
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    #La función down determina que en caso de que se accione la tecla de la flecha hacia arriba con la culebra dirigiéndose hacia abajo, esta siga el trayecto que lleva para no colisionar con su propio cuerpo
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    #La función left determina que en caso de que se accione la tecla de la flecha hacia la derecha con la culebra dirigiéndose hacia la izquierda, esta siga el trayecto que lleva para no colisionar con su propio cuerpo
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    #La función right determina que en caso de que se accione la tecla de la flecha hacia la izquierda con la culebra dirigiéndose hacia la derecha, esta siga el trayecto que lleva para no colisionar con su propio cuerpo
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)