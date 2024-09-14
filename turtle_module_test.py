import turtle

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
my_turtle.forward(50)
my_turtle.left(90)
my_turtle.forward(50)

# Close the turtle graphics window when clicked
turtle.exitonclick()