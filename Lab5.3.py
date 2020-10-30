#Julian Casillas
#10/27/2020
#takes information as inputs, draws the polygon, and then fills it in

import turtle

length = int(input("What is the length: "))
sides = int(input("How many number of sides: "))
line = input("What is the color of the line: ")
fill = input("What is the color of the fill: ")


t = turtle.Turtle()
                 
def polygon():
    t.color(line, fill)
    t.begin_fill()
    for num in range (sides):
        t.left(360/sides)
        t.forward(length)
    t.end_fill()
    
    
        
polygon()
