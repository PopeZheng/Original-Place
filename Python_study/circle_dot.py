import turtle

x1,y1 = eval(input("Enter the the center of circle cooridnate(x,y):"))
radius = eval(input("Enter the circle's radius:"))
x2,y2 = eval(input("Enter a point cooridnate(x,y):"))

turtle.showturtle()
turtle.penup()
turtle.goto(x1,y1-radius)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(x2,y2)
turtle.pendown()
turtle.begin_fill()
turtle.color("red")
turtle.circle(1)
turtle.end_fill()

turtle.penup()
turtle.goto(x1,y1-radius-20)

d = (x1-x2)**2 + (y1-y2)**2

if d<radius**2:
    turtle.write("This dot is in the circle")
elif d == radius**2:
    turtle.write("This dot is on the circle")
else:
    turtle.write("This dot is off the circle")
    
turtle.done()


