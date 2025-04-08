from turtle import *
import math

t1 = Turtle ()
t1.goto(0,-250) #-130
t1.pensize(4)
t1.speed(11)
t1.fillcolor("black")
t1.begin_fill() # Comenzar a dibujar
t1.circle(250) # El numero es el radio
t1.end_fill() # Para terminar de dibujar

# TENEDOR
# mango de tenedor
t1.goto(0,80)
t1.pendown()
t1.pensize(2)
t1.speed(7)
t1.fillcolor("grey")
t1.begin_fill()
t1.left(150)
t1.forward(100)
t1.right(40)
t1.left(125)
t1.forward(10)
t1.left(95)
t1.forward(100)
t1.left(95)
t1.forward(10)
t1.left(80)
t1.forward(100)
t1.right(90)
t1.end_fill()


# Base ovalo
t1.goto(-88,120)
t1.pendown()
t1.pensize(2)
t1.speed(7)
t1.fillcolor("grey")
t1.begin_fill()
t1.forward(10)
t1.left(37)
t1.forward(15)
t1.right(40)
t1.backward(35)
t1.end_fill()


#ovalo de tenedor
def dibujar_ovalo(a, b, x_centro, y_centro):
    t1.speed(0)
    t1.penup()
    t1.goto(x_centro, y_centro)  
    t1.pendown()
    t1.begin_fill()
    t1.color("grey")
    
    for i in range(361):
        
        angulo = math.radians(i)
        x = a * math.cos(angulo) + x_centro
        y = b * math.sin(angulo) + y_centro
        
        
        x += (y - y_centro) / 1.7
        
        t1.goto(x, y)
    
    t1.end_fill()
   

# El primer par define el tamaño, el segundo par define la ubicación

dibujar_ovalo(10, 20, -98, 133)

# Dientes del tenedor

t1.goto(-89,151)
t1.pendown()
t1.pensize(2)
t1.speed(7)
t1.fillcolor("grey")
t1.begin_fill()
t1.forward(5)#
t1.left(90)
t1.forward(60)
t1.left(90)
t1.forward(5)
t1.left(90)
t1.forward(60)
t1.end_fill()

t1.fillcolor("grey")
t1.begin_fill()
t1.right(90)
t1.forward(10)
t1.right(90)
t1.forward(10)
t1.right(90)
t1.forward(10)
t1.right(90)
t1.forward(10)
t1.right(90)
t1.forward(10)
t1.right(90)
t1.forward(60)
t1.left(90)
t1.forward(5)
t1.left(90)
t1.forward(60)
t1.right(90)
t1.forward(10)
t1.right(90)
t1.forward(10)
t1.right(90)
t1.forward(10)
t1.right(90)
t1.forward(10)
t1.right(90)
t1.forward(10)
t1.right(90)
t1.end_fill()

t1.fillcolor("grey")
t1.begin_fill()
t1.forward(60)
t1.left(90)
t1.forward(5)
t1.left(90)
t1.forward(60)

t1.right(90)
t1.forward(10)
t1.right(90)
t1.forward(10)
t1.right(90)
t1.forward(10)
t1.right(90)
t1.forward(10)
t1.right(90)
t1.forward(10)
t1.right(90)
t1.end_fill()

t1.fillcolor("grey")
t1.begin_fill()
t1.forward(60)
t1.left(90)
t1.forward(5)
t1.left(90)
t1.forward(66)
t1.left(180)
t1.end_fill()

t1.fillcolor("grey")
t1.begin_fill()
t1.forward(70)
t1.right(90)
t1.end_fill()

t1.fillcolor("grey")
t1.begin_fill()
t1.forward(50)
t1.right(90)
t1.forward(5)
t1.right(90)
t1.forward(50)
t1.end_fill()

# Hamburguesa


# Carne 1
t4 = Turtle()
def dibujar_carne(a,b,x_centro,y_centro):
    t4.speed(0)
    t4.penup()
    t4.goto(a + x_centro,y_centro)
    t4.pendown()
    t4.begin_fill()
    t4.color("brown")
    for i in range(361):
      angulo = math.radians(i)
      x= a * math.cos(angulo) + x_centro
      y= b * math.sin(angulo) + y_centro
      t4.goto(x,y)
    t4.end_fill()
dibujar_carne(70,8,5,10)

def dibujar_carne2(a,b,x_centro,y_centro):
    t4.speed(0)
    t4.penup()
    t4.goto(a + x_centro,y_centro)
    t4.pendown()
    t4.begin_fill()
    t4.color("brown")
    for i in range(361):
      angulo = math.radians(i)
      x= a * math.cos(angulo) + x_centro
      y= b * math.sin(angulo) + y_centro
      t4.goto(x,y)
    t4.end_fill()

# El primer par define el tamaño, # El segundo par define la ubicación
dibujar_carne2(70,8,5,2)
t4.fillcolor("brown")
t4.begin_fill()
t4.left(90)
t4.forward(9)
t4.left(90)
t4.forward(141)
t4.left(90)
t4.forward(9)
t4.left(90)
t4.forward(150)
t4.end_fill()

# Carne 2
t4 = Turtle()
def dibujar_carne(a,b,x_centro,y_centro):
    t4.speed(0)
    t4.penup()
    t4.goto(a + x_centro,y_centro)
    t4.pendown()
    t4.begin_fill()
    t4.color("brown")
    for i in range(361):
      angulo = math.radians(i)
      x= a * math.cos(angulo) + x_centro
      y= b * math.sin(angulo) + y_centro
      t4.goto(x,y)
    t4.end_fill()
dibujar_carne(70,8,5,1)

def dibujar_carne2(a,b,x_centro,y_centro):
    t4.speed(0)
    t4.penup()
    t4.goto(a + x_centro,y_centro)
    t4.pendown()
    t4.begin_fill()
    t4.color("brown")
    for i in range(361):
      angulo = math.radians(i)
      x= a * math.cos(angulo) + x_centro
      y= b * math.sin(angulo) + y_centro
      t4.goto(x,y)
    t4.end_fill()

# El primer par define el tamaño, # El segundo par define la ubicación
dibujar_carne2(70,8,5,-9)
t4.fillcolor("brown")
t4.begin_fill()
t4.left(90)
t4.forward(9)
t4.left(90)
t4.forward(141)
t4.left(90)
t4.forward(9)
t4.left(90)
t4.forward(150)
t4.end_fill()

t2 = Turtle ()
# Pan 2
def dibujar_pan2(a,b,x_centro,y_centro):
    t2.speed(0)
    t2.penup()
    t2.goto(a + x_centro,y_centro)
    t2.pendown()
    t2.begin_fill()
    t2.color("orange")
    for i in range(361):
      angulo = math.radians(i)
      x= a * math.cos(angulo) + x_centro
      y= b * math.sin(angulo) + y_centro
      t2.goto(x,y)
    t2.end_fill()

# El primer par define el tamaño, # El segundo par define la ubicación
dibujar_pan2(60,8,3,-36)

t2.fillcolor("orange")
t2.begin_fill()
t2.left(90)
t2.forward(20)
t2.left(90)
t2.forward(120)
t2.left(90)
t2.forward(20)
t2.left(90)
t2.forward(120)
t2.left(90)
t2.end_fill()

t5 = Turtle ()
# Queso en forma de triángulos discretos que sobresalen
def dibujar_queso(a,b,x_centro,y_centro):
    t5.speed(0)
    t5.penup()
    t5.goto(a + x_centro,y_centro)
    t5.pendown()
    t5.begin_fill()
    t5.color("yellow")
    for i in range(361):
      angulo = math.radians(i)
      x= a * math.cos(angulo) + x_centro
      y= b * math.sin(angulo) + y_centro
      t5.goto(x,y)
    t5.end_fill()

# El primer par define el tamaño, # El segundo par define la ubicación
dibujar_queso(60,10,5,10)

t5.fillcolor("yellow")
t5.begin_fill()
t5.right(150)
t5.forward(70)
t5.right(60)
t5.forward(55)
t5.left(60)
t5.forward(20)
t5.right(90)
t5.forward(20)
t5.right(120)
t5.forward(140)
t5.end_fill()

# tomate
t4 = Turtle()
def dibujar_carne(a,b,x_centro,y_centro):
    t4.speed(0)
    t4.penup()
    t4.goto(a + x_centro,y_centro)
    t4.pendown()
    t4.begin_fill()
    t4.color("red")
    for i in range(361):
      angulo = math.radians(i)
      x= a * math.cos(angulo) + x_centro
      y= b * math.sin(angulo) + y_centro
      t4.goto(x,y)
    t4.end_fill()
dibujar_carne(70,8,5,24)

def dibujar_carne2(a,b,x_centro,y_centro):
    t4.speed(0)
    t4.penup()
    t4.goto(a + x_centro,y_centro)
    t4.pendown()
    t4.begin_fill()
    t4.color("red")
    for i in range(361):
      angulo = math.radians(i)
      x= a * math.cos(angulo) + x_centro
      y= b * math.sin(angulo) + y_centro
      t4.goto(x,y)
    t4.end_fill()

# El primer par define el tamaño, # El segundo par define la ubicación
dibujar_carne2(70,8,5,16)
t4.fillcolor("red")
t4.begin_fill()
t4.left(90)
t4.forward(9)
t4.left(90)
t4.forward(141)
t4.left(90)
t4.forward(9)
t4.left(90)
t4.forward(150)
t4.end_fill()


def dibujar_lechuga_mejorada(a, b, x_centro, y_centro):
    t3 = Turtle()
    t3.speed(0)
    t3.penup()
    t3.goto(x_centro, y_centro)
    t3.pendown()
    t3.begin_fill()
    t3.color("green")
    
    # Hacemos la forma menos regular cambiando ligeramente las coordenadas
    for i in range(361):
        angulo = math.radians(i)
        x = a * math.cos(angulo) + x_centro
        y = b * math.sin(angulo) + y_centro

        # Cambiar ligeramente la posición para crear una forma más irregular
        # Hacemos que la "lechuga" tenga más variabilidad en las coordenadas
        x += math.sin(math.radians(i * 10)) * 5  # Variación en el eje X
        y += math.cos(math.radians(i * 5)) * 5   # Variación en el eje Y

        t3.goto(x, y)

    t3.end_fill()

# Dibujamos una lechuga con un tamaño de elipse más grande y un desplazamiento irregular
dibujar_lechuga_mejorada(70, 10, 5, 33)

t2 = Turtle ()
# Pan 1
def dibujar_pan1(a,b,x_centro,y_centro):
    t2.speed(0)
    t2.penup()
    t2.goto(a + x_centro,y_centro)
    t2.pendown()
    t2.begin_fill()
    t2.color("orange")
    for i in range(361):
      angulo = math.radians(i)
      x= a * math.cos(angulo) + x_centro
      y= b * math.sin(angulo) + y_centro
      t2.goto(x,y)
    t2.end_fill()

# El primer par define el tamaño, # El segundo par define la ubicación
dibujar_pan1(60,20,3,60)

t2.fillcolor("orange")
t2.begin_fill()
t2.right(90)
t2.forward(20)
t2.right(90)
t2.forward(120)
t2.right(90)
t2.forward(20)
t2.right(90)
t2.forward(120)
t2.right(90)
t2.end_fill()
done()