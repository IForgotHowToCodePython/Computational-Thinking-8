
import turtle
t = turtle.Turtle()

# setup
t.speed(10)
turtle.Screen().bgcolor("light blue")


# stripes

# move to stripe 1
t.goto(-250, -100)

h=50
# stripe 1
t.color("yellow")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.end_fill()


# move to stripe 2
t.goto(-250, -50)

# stripe 2
t.color("yellow")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.end_fill()

# move to stripe 3
t.goto(-250, 0)

# stripe 3
t.color("blue")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.end_fill()

# move to stripe 4
t.goto(-250, 50)

# stripe 4
t.color("blue")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.forward(500)
t.left(90)
t.forward(h)
t.left(90)
t.end_fill()

# move to stripe 5
t.goto(-250, 100)


turtle.exitonclick()