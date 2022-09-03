import turtle

turtle.bgcolor("black")
turtle.pensize(2)
turtle.color("red")
turtle.speed(10)

# Draw a square
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.done()

# creates a nice drawing
for colours in ["red", "green", "orange", "yellow", "blue", "purple"]:
    turtle.color(colours)
    turtle.circle(150)
    turtle.left(60)


# Lets make it cooler
for i in range(12):
    for colours in ["red", "green", "orange", "yellow", "blue", "purple"]:
        turtle.color(colours)
        turtle.circle(150)
        turtle.left(5)
turtle.done()