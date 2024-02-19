import time
from turtle import Screen

from Food import Food
from Scoreboard import Scoreboard
from Snake import Snake

screen = Screen()
screen.setup(500, 500)
screen.bgcolor("black")
screen.title("The hunger games: Snake Edition")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.change_food_location()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 240 or snake.head.xcor() < -240 or snake.head.ycor() > 240 or snake.head.ycor() < -240:
        is_game_on = False
        scoreboard.gameover()

    for body in snake.snakes:
        if body == snake.head:
            pass
        elif snake.head.distance(body) < 10:
            is_game_on = False
            scoreboard.gameover()

screen.exitonclick()
