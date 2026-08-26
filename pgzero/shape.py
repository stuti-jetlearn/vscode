import turtle

pen = turtle.Turtle()

shape = turtle.textinput(
    "Shape",
    "Enter square, triangle or pentagon:"
)

if shape == "square":
    for i in range(4):
        pen.forward(100)
        pen.right(90)

elif shape == "triangle":
    for i in range(3):
        pen.forward(100)
        pen.right(120)

elif shape == "pentagon":
    for i in range(5):
        pen.forward(100)
        pen.right(72)

else:
    pen.write("I don't know that shape!")

turtle.done()