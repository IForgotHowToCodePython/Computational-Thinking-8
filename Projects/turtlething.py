# ### SETUP ###
import turtle


t = turtle.Turtle()
t.penup()
t.goto (-350,-100)
t.color ("green")
t.pendown()


for i in range(10):
    t.penup()
    t.forward(50)
    t.pendown()
    for i in range (4) :
        t.forward(30)
        t.left(90)




# #############################################
# ### ENDING ###
turtle.exitonclick()
# #############################################