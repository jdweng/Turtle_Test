from turtle import *
speed(0)
tracer(0, 0)
ht()
delay(0)
Tim = Turtle()
Tim.pu()
Tim.goto(-175, 100)
Tim.pd()
Goodrick = Turtle()
Goodrick.pu()
Goodrick.goto(175, 100)
Goodrick.pd()
Kenneth=Turtle()
Kenneth.pu()
Kenneth.goto(0, -200)
Kenneth.pd()
Kirkland=Turtle()
for t in [Tim, Goodrick, Kenneth, Kirkland]:
    for i in range(74):
        t.ht()
        t.speed(0)
        t.color('blue')
        t.forward(150)
        t.color('red')
        t.circle(10)
        t.left(505)
        t.color('green')
        t.forward(150)
        t.circle(10)
        t.color('red')
        t.forward(10)
        t.circle (10)
color('purple')
width(10)
for g in range(30):
    forward(50)
    right(60)
    forward(50)
for b in range(30):
    backward(50)
    left(60)
    backward(50)
update()
        
