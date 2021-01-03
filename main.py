from turtle import Turtle, Screen
from colors import COLORS
import random

# possibilities forward backward right left



timmy_the_turtle = Turtle()
timmy_the_turtle.shape('turtle')
timmy_the_turtle.color('cyan2')

movements = [timmy_the_turtle.forward, timmy_the_turtle.backward, timmy_the_turtle.right, timmy_the_turtle.left]

#timmy_the_turtle.forward(20)

for _ in range(0, 1000):
    random_index = random.randint(0,3)
    timmy_the_turtle.pencolor(random.choice(COLORS))
    timmy_the_turtle.speed('fastest')
    timmy_the_turtle.pensize(10)
    if random_index in [0,1]:
        movements[random_index](20)
    if random_index in [2,3]:
        movements[random_index](90)






  # for number in range(3,11):
  #   timmy_the_turtle.pencolor(random.choice(COLORS))
  #   for num in range(0,number):
  #     timmy_the_turtle.forward(100)
  #     timmy_the_turtle.right(360/number)


screen = Screen()

screen.exitonclick()