import turtle
import random
turtle.setup(650,350,200,200)
turtle.penup()
turtle.fd(-300)
turtle.pendown()
turtle.width(25)


#turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
    turtle.pencolor(random.choice(["yellow","purple","blue","black"]))
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40 * 2/3)




