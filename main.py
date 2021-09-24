from turtle import Screen
from snake import Snake
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

snake = Snake()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
