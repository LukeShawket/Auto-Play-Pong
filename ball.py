import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self._ball = Turtle()
        self._ball.penup()
        self._ball.goto(position)
        self._ball.shape("circle")
        self._ball.shapesize(1)
        self._ball.color("white")
        self.random_y = 0
        self.randomize = random

    def get_ball_pos(self):
        return self._ball.pos()

    def fly(self, speed, direction):
        self.random_y = self.randomize.randrange(-250, 250)
        self._ball.speed(speed)
        self._ball.goto((direction, self.random_y))



