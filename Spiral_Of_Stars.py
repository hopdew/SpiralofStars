import turtle
turtle.shape("turtle")
turtle.speed(43)
turtle.color("pink")
turtle.bgcolor("grey")
def star(size):
   for i in range(5):
       turtle.forward(size)
       turtle.right(144)


def starSpiral():
       size = 50
       for i in range(45):
           star(size)
           turtle.right(8)
           size = size + 2

starSpiral()
turtle.penup()
turtle.goto(150,190)
turtle.pendown()
starSpiral()
turtle.penup()
turtle.goto(-150,-190)
turtle.pendown()
starSpiral()


