import turtle
turtle.Screen().bgcolor("green")
turtle.Screen().setup(400, 500)
polygon = turtle.Turtle()
side_length = int(input("Enter length of sides: "))
sides = int(input("Enter number of sides: "))
side_angle = 360 / sides
for i in range(sides):
    polygon.forward(side_length)
    polygon.right(side_angle)
turtle.done()
