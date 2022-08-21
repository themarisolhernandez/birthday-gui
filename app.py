import turtle
import random
import pygame

# set the background color for the page
win = turtle.Screen()
win.bgcolor("light blue")

pygame.mixer.init()
pygame.mixer.music.load("las_mananitas.mp3")
pygame.mixer.music.play()

tommy = turtle.Turtle()
tommy.shape("circle")
tommy.speed(1.5)


# draw lines
tommy.penup()
tommy.goto(-190, -180)
tommy.color("yellow")
tommy.pensize(8)
tommy.pendown()
tommy.goto(190,-180)
tommy.penup()

tommy.penup()
tommy.goto(-160, -150)
tommy.color("purple")
tommy.pensize(8)
tommy.pendown()
tommy.goto(160,-150)
tommy.penup()

tommy.penup()
tommy.goto(-130, -120)
tommy.color("teal")
tommy.pensize(8)
tommy.pendown()
tommy.goto(130,-120)
tommy.penup()

# draw cake
tommy.goto(-74,-110)
tommy.pendown()
tommy.color("white")
tommy.goto(50,-110)
tommy.left(90)
tommy.forward(60)
tommy.left(90)
tommy.forward(125)
tommy.left(90)
tommy.forward(60)
tommy.penup()

#draw candles
tommy.goto(-60, -40)
tommy.color("aquamarine")
tommy.pendown()
tommy.pensize(3)
tommy.goto(-60, -20)
tommy.penup()

tommy.goto(-40, -40)
tommy.color("yellow")
tommy.pendown()
tommy.pensize(3)
tommy.goto(-40, -20)
tommy.penup()

tommy.goto(-20, -40)
tommy.color("green")
tommy.pendown()
tommy.pensize(3)
tommy.goto(-20, -20)
tommy.penup()

tommy.goto(0, -40)
tommy.color("pink")
tommy.pendown()
tommy.pensize(3)
tommy.goto(0, -20)
tommy.penup()

tommy.goto(20, -40)
tommy.color("blue")
tommy.pendown()
tommy.pensize(3)
tommy.goto(20, -20)
tommy.penup()

# draw stars
tommy.goto(-270, 200)
tommy.color("yellow")
tommy.pendown()
tommy.pensize(5)
tommy.speed(3)
for i in range(5):
    tommy.forward(50)
    tommy.right(144)
tommy.penup()

tommy.goto(-270, -20)
tommy.color("yellow")
tommy.pendown()
for i in range(5):
    tommy.forward(50)
    tommy.right(144)
tommy.penup()

tommy.goto(270, -20)
tommy.color("yellow")
tommy.pendown()
for i in range(5):
    tommy.forward(50)
    tommy.right(144)
tommy.penup()

tommy.goto(270, 200)
tommy.color("yellow")
tommy.pendown()
for i in range(5):
    tommy.forward(50)
    tommy.right(144)
tommy.penup()

# draw astronaut head
tommy.penup()
tommy.goto(-70,195)
tommy.color("#C19A6B")
tommy.pendown()
tommy.circle(70)
tommy.penup()

# draw astronaut helmet
tommy.penup()
tommy.goto(-90,195)
tommy.color("black")
tommy.pendown()
tommy.circle(90)
tommy.penup()

# draw astronaut nose
tommy.penup()
tommy.goto(8,185)
tommy.color("#967969")
tommy.pensize(3)
tommy.pendown()
tommy.left(180)
tommy.circle(8, 180)
tommy.penup()

# draw astronaut eyes
tommy.penup()
tommy.goto(25,215)
tommy.color("black")
tommy.pensize(15)
tommy.pendown()
tommy.circle(1)
tommy.penup()

tommy.penup()
tommy.goto(-28,215)
tommy.color("black")
tommy.pensize(15)
tommy.pendown()
tommy.circle(1)
tommy.penup()

# draw astronaut smile
tommy.penup()
tommy.goto(-35,175)
tommy.pensize(3)
tommy.pendown()
tommy.circle(35, 180)
tommy.penup()

# draw astronaut mustache
tommy.goto(20,167)
tommy.penup()
tommy.pendown()
tommy.left(30)
tommy.forward(10)
tommy.left(120)
tommy.forward(10)
tommy.right(120)
tommy.forward(10)
tommy.left(120)
tommy.forward(10)
tommy.right(120)
tommy.forward(10)
tommy.left(120)
tommy.forward(10)
tommy.right(120)
tommy.forward(10)
tommy.left(120)
tommy.forward(10)
tommy.penup()

# add helmet details
tommy.penup()
tommy.pensize(5)
tommy.goto(-90,215)
tommy.pendown()
tommy.left(305)
tommy.circle(20, 180)
tommy.penup()

tommy.penup()
tommy.goto(90,180)
tommy.pendown()
tommy.left(360)
tommy.circle(20, 180)
tommy.penup()

tommy.penup()
tommy.goto(8,268)
tommy.pendown()
tommy.right(90)
tommy.forward(13)
tommy.penup()

tommy.penup()
tommy.goto(-7,268)
tommy.pendown()
tommy.forward(13)
tommy.penup()

# print message
tommy.goto(-150, 35)
tommy.color("grey")
tommy.pendown()
tommy.write("HAPPY BIRTHDAY PAPI!",  font=("Arial", 25, "normal"))
tommy.penup()
tommy.goto(-350, 350)


# send the turtle to the corner
win.exitonclick()