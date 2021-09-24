from turtle import Screen, Turtle
import time

# Planning
#   Create a snake body 0,0, 20 to left, 20 to left
#   Move the snake
#   Control the snake
#   Detect collision with food
#   Create a scoreboard
#   Detect collision with wall
#   Detect collision with tail

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)
x_coordinates = [0, -20, -40]

segments = []

for index in range(3):
    square = Turtle('square')
    square.color('white')
    square.penup()
    square.goto(x_coordinates[index], 0)
    segments.append(square)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num -1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

screen.exitonclick()
