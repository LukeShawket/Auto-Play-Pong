import threading
from turtle import Screen
from player import Player
from ball import Ball


RIGHT_POS = (450, 0)
LEFT_POS = (-450, 0)
BALL_RIGHT_POS = (400, 0)
BALL_LEFT_POS = (-400, 0)

# Create main screen
my_screen = Screen()
my_screen.title("Auto Play Pong")
my_screen.bgcolor("black")
my_screen.setup(1000, 600)

#create pc players for the right and left side of the table
player_right = Player("normal", RIGHT_POS)
player_left = Player("slow", LEFT_POS)
_ball = Ball(BALL_RIGHT_POS)

# Get the ball and players behavior from their classes
random_y = 0
def ball_fly_action(force, direction):
    _ball.fly(force, direction)

def player_right_action(pos):
    player_right.play(pos)

def player_left_action(pos):
    player_left.play(pos)


threads = []
is_game_on = True
ball_pos = ()
right_hit = False
left_hit = False
player_right_pos = 0
player_left_pos = 0

# main game loop
def game_loop():
    global is_game_on
    global ball_pos
    global player_right_pos
    global player_left_pos
    global right_hit
    global left_hit
    global random_y
    while is_game_on:
        my_screen.update()
        ball_pos = _ball.get_ball_pos()
        player_right_pos = player_right.get_player_pos()
        player_left_pos = player_left.get_player_pos()
        right_hit = player_right.hit(ball_pos)
        left_hit = player_left.hit(ball_pos)

        # when the right player hits the ball
        if right_hit:
            left_hit = False
            hit_right_force = player_right.get_hit_force()
            ball_thread = threading.Thread(target=ball_fly_action, args=(hit_right_force, -450))
            ball_thread.start()


            random_y = _ball.random_y
            left_thread = threading.Thread(target=player_left_action, args=(random_y,))
            left_thread.start()
            ball_thread.join()

        # when the left player hits the ball
        if left_hit:
            right_hit = False
            hit_right_force = player_right.get_hit_force()
            ball_thread = threading.Thread(target=ball_fly_action, args=(hit_right_force, 450))
            ball_thread.start()

            random_y = _ball.random_y
            right_thread = threading.Thread(target=player_right_action, args=(random_y,))
            right_thread.start()
            ball_thread.join()

        # detect if the game ended
        if _ball.xcor() < player_left.xcor() or _ball.xcor() > player_right.xcor():
            is_game_on = False

#main thread
main_thread = threading.Thread(target=game_loop)
main_thread.daemon = True
main_thread.start()


my_screen.exitonclick()
