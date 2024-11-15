from turtle import Turtle
from random import choice
import threading

class Player(Turtle):
    def __init__(self, level, position):
        super().__init__()
        self.level = level
        self._player = Turtle()
        self._player.penup()
        self._player.goto(position)
        self._player.shape("square")
        self._player.shapesize(6, 1)
        self._player.color("white")
        self._player.speed(level)
        self.origin = position

    def get_player_pos(self):
        return self._player.pos()

    def get_hit_force(self):
        if self.level == "normal":
            return choice(("slow", "slow", "slow", "slowest", "slow", "slow"))
        elif self.level == "slow":
            return choice(("slow", "slowest", "slow", "slowest", "slow", "slowest"))
        else:
            return choice(("slow", "slowest", "slowest", "slowest", "slowest", "slowest"))

    def hit(self, position):
        if self._player.distance(position) <= 50:
            return True

    def play(self, ball_pos_y):
        self._player.goto((self._player.xcor(), ball_pos_y))

