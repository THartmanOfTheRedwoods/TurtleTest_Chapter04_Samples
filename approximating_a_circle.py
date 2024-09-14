import turtle
import math

def polygon(n, length):
    angle = 360 / n
    for i in range(n):
        my_turtle.forward(length)
        my_turtle.left(angle)

def circle_v1(radius):
    circumference = 2 * math.pi * radius
    n = 30
    length = circumference / n
    polygon(n, length)  # Simulates a circle by drawing a 30 sided polygon.

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
my_turtle.speed(10)  # Somewhat equivalent to Jupyter turtle's delay parameter (1 slow to 10 fast).
circle_v1(30)


# Close the turtle graphics window when clicked
turtle.exitonclick()