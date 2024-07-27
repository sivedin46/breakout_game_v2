from turtle import Screen
from ball import Ball
from scoreboard import Scoreboard
from bricks import Bricks
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=820, height=620)   # screensize 800x600 (print(screen.screensize)
screen.setworldcoordinates(-400, -300, 400, 300)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)


paddle = Paddle()
ball = Ball()
bricks = Bricks()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle.go_right, "Right")
screen.onkeypress(paddle.go_left, "Left")

game_on = True
time_start = time.time()  # starting to get time info for calculating elapsed seconds for game speed
while game_on:
    if scoreboard.life_count:
        if len(bricks.bricks) > 0:
            time.sleep(ball.move_speed)
            ball.ball_speed(time_start)
            scoreboard.speed_write(ball.move_speed)
            screen.update()
            temp_ball_x = ball.move()   # getting ball x position for future use in paddle collision
            for index, brick in enumerate(bricks.bricks):
                col, col_side = ball.detect_bricks(brick)  # control for all bricks for ball collision
                if col:
                    if col_side == "left" or col_side == "right":
                        ball.bounce_x()
                    if col_side == "top" or col_side == "bottom":
                        ball.bounce_y()
                    scoreboard.point(brick)
                    bricks.brick_delete(index)
            if ball.ycor() > 290:  # top side of screen-ball collision detection
                ball.bounce_y()
            if ball.ycor() < -290:  # bottom side of screen-ball collision detection.You lost one life or game over
                ball.reset_position()  # reset time, paddle-ball position,speed
                paddle.reset_position()
                time_start = time.time()
                get_speed = ball.ball_speed(time_start)
                scoreboard.speed_write(get_speed)
                scoreboard.life_count = scoreboard.life_count[:-1]
                scoreboard.update_scoreboard()
                time.sleep(0.5)
            if ball.ycor() < -268:  # paddle-ball collision detection
                pad_side, ball_side, collision = ball.detect_paddle(paddle.paddle_l, temp_ball_x)
                # print(side,collision)
                if collision:
                    if (ball_side == "right" and pad_side == "right") or (ball_side == "left" and pad_side == "left"):
                        ball.bounce_y()
                        ball.bounce_x()
                    else:
                        ball.bounce_y()

            if ball.xcor() > 380 or ball.xcor() < -390:  # left-right side of screen-ball collision detection
                ball.bounce_x()

        else:   # all bricks deleted so do initialize for new level
            level_check = scoreboard.level_check()
            ball.reset_position()
            paddle.reset_position()
            time_start = time.time()
            ball.ball_speed(time_start)
            scoreboard.speed_write(ball.move_speed)
            if level_check == 2:
                bricks.bricks_counter = 0
                bricks.create_new_brick(5)
            elif level_check == 3:
                bricks.bricks_counter = 0
                bricks.create_new_brick(6)
            else:
                scoreboard.you_win()
    else:  # if you don't have life game over
        scoreboard.check_record()
        screen.clearscreen()
        screen.bgcolor("black")
        scoreboard.game_over()
        game_on = False

screen.exitonclick()
