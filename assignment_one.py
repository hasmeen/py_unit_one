
import turtle

pen=turtle.Turtle()
pen.speed(90)


#circles for face
def draw_circle(color, radius):
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()
    pen.penup()

#face and skin tone
pen.fillcolor('beige')
pen.begin_fill()
pen.circle(100)
pen.end_fill()

#go to and fill in the iris and pupils
pen.up()
pen.goto(-40, 110)
draw_circle('white', 15)
pen.goto(-30, 125)
draw_circle('black', 5)
pen.goto(40, 110)
draw_circle('white', 15)
pen.goto(30, 125)
draw_circle('black', 5)

#nose
pen.goto(0, 95)
draw_circle('yellow', 8)

#smile
pen.goto(-40, 85)
pen.pendown()
pen.right(90)
pen.circle(40, 180)
pen.penup()

#tongue
pen.goto(-10, 45)
pen.down()
pen.right(180)
pen.fillcolor('pink')
pen.begin_fill()
pen.circle(10, 180)
pen.end_fill()

#flower petal location
pen.penup()
pen.goto(-65,130)

#flower petal hair loop
for x in range(8):
    pen.fillcolor('pink')
    pen.begin_fill()
    pen.pendown()
    pen.circle(45)
    pen.penup()
    pen.backward(55)
    pen.left(45)
    pen.end_fill()

#exit when clicked
turtle.exitonclick()
