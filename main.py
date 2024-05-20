from turtle import Turtle, Screen

tim = Turtle()
tim.shape("classic")
tim.color("red")

# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)

for x in range(4):
    tim.forward(100)
    tim.right(90)


screen = Screen()
screen.exitonclick()
