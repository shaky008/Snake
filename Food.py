import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.change_food_location()

    def change_food_location(self):
        random_x = random.randint(-230, 230)
        random_y = random.randint(-230, 230)
        self.goto(x=random_x, y=random_y)

