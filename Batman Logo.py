import turtle

bat = turtle.Turtle()

bat.turtlesize(1, 1, 1)
bat.pensize(8)

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("BATMAN")

bat.color("white", "black")
bat.begin_fill()
bat.left(90) 
bat.circle(50, 85) 
bat.circle(15, 110)
bat.right(180)

bat.circle(30, 150)
bat.right(5)
bat.forward(10) 

bat.right(90)
bat.circle(-70, 140)
bat.forward(40)
bat.right(110)

bat.circle(100, 30)
bat.circle(30, 100)
bat.left(50)
bat.forward(50)
bat.right(145)

bat.forward(30)
bat.left(55)
bat.forward(10)

bat.forward(10)
bat.left(55)
bat.forward(30)
bat.right(145)
bat.forward(50)
bat.left(50)
bat.circle(30, 100)
bat.circle(100, 30)
bat.right(90)
bat.right(20)
bat.forward(40)
bat.circle(-70, 140)

bat.right(90)
bat.forward(10)
bat.right(5)
bat.circle(30, 150)

bat.left(180)
bat.circle(15, 110)
bat.circle(50, 85)

bat.end_fill()
turtle.done()
