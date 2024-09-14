import turtle

def square_v1():
    for i in range(4):
        my_turtle.forward(50)
        my_turtle.left(90)

def square_v2(length):
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.left(90)

def polygon(n, length):
    angle = 360 / n
    for i in range(n):
        my_turtle.forward(length)
        my_turtle.left(angle)

def square_v3(length):
    polygon(4, length)

# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("black")
# Set the width and height of the screen
screen.setup(width=500, height=500)

# Create a new turtle object, equivalent to Jupyter's make_turtle
my_turtle = turtle.Turtle()

# Set the turtle's shape and color
my_turtle.shape( "circle" )  # Other options: arrow, classic, square, triangle, and turtle
my_turtle.color( "green" )

# Draw with a turtle.
square_v1()  # Basic fixed sized square.
my_turtle.color( "red" )
square_v2(100)  # More generalized square with side length passed as an argument.
my_turtle.color( "yellow" )
polygon(n=7, length=30)  # Even more generalized, draw any regular polygon, note passing arguments by name
my_turtle.color( "purple" )
square_v3(200)  # More generalized square with side length passed as an argument.


# Close the turtle graphics window when clicked
turtle.exitonclick()