from turtle import *
import coordenadas

pen = Turtle()

bgcolor("black")

pen.pensize(2)
pen.penup()
pen.speed(0)

def cuadrado():
	pen.pendown()
	pen.forward(15)
	pen.left(90)
	pen.forward(15)
	pen.left(90)
	pen.forward(15)
	pen.left(90)
	pen.forward(15)
	pen.left(90)
	pen.penup()

for x in range(len(coordenadas.logo1)):
	pen.color("#4584b6")
	pen.goto(coordenadas.logo1[x])
	cuadrado()

for x in range(len(coordenadas.logo2)):
	pen.color("#ffde57")
	pen.goto(coordenadas.logo2[x])
	cuadrado()

pen.begin_fill()
pen.goto(-60, 135)
pen.color("#4584b6")
cuadrado()
pen.end_fill()

pen.begin_fill()
pen.goto(60, -135)
pen.color("#ffde57") #color
cuadrado()
pen.end_fill()

done()