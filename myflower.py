import turtle
import time

charu=turtle.Turtle()
time.sleep(10)
charu.color("red","yellow")
charu.begin_fill()
x=range(1,19)
for i in x :
    charu.forward(300)
    charu.left(170)
    charu.forward(300)
    charu.left(170)
    i+=1
charu.end_fill()
turtle.done()
