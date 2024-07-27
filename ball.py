from turtle import Turtle
import math
import time
import pygame

pygame.mixer.init()
paddle_sound = pygame.mixer.Sound("paddle.wav")
brick_sound = pygame.mixer.Sound("bricks.wav")


class Ball(Turtle):
    def __init__(self, ):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1, 1, 0)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.07
        self.position = (0, -240)
        self.goto(self.position)
        self.showturtle()

    def move(self):
        old_x = self.xcor()
        old_y = self.ycor()
        new_x = old_x + self.x_move
        new_y = old_y + self.y_move
        self.goto(new_x, new_y)
        return old_x

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(self.position)

    def detect_bricks(self, brick):  # calculates distance and checks is there a collision and which side of brick
        brick_x = brick.xcor()  # x coordinate
        brick_y = brick.ycor()
        brick_w = 42
        brick_h = 22
        ball_x = self.xcor()
        ball_y = self.ycor()
        ball_r = 11
        left = brick_x - brick_w / 2
        right = brick_x + brick_w / 2
        top = brick_y + brick_h / 2
        bottom = brick_y - brick_h / 2
        closest_x = max(left, min(ball_x, right))
        closest_y = max(bottom, min(ball_y, top))
        distance = math.sqrt((closest_x - ball_x) ** 2 + (closest_y - ball_y) ** 2)
        collision = distance < ball_r

        if collision:
            brick_sound.play()
            distance_to_left = ball_x - left
            distance_to_right = right - ball_x
            distance_to_bottom = ball_y - bottom
            distance_to_top = top - ball_y
            min_distance = min(distance_to_left, distance_to_right, distance_to_bottom, distance_to_top)
            if min_distance == distance_to_left:
                collision_side = "left"
            elif min_distance == distance_to_right:
                collision_side = "right"
            elif min_distance == distance_to_bottom:
                collision_side = "bottom"
            else:
                collision_side = "top"
        else:
            collision_side = "no"
        return collision, collision_side

    def detect_paddle(self, paddle_l, old_ball_x):  # checks is there a collision and which part of brick and ball dir.
        p_side = ""
        b_side = ""
        ball_x = self.xcor()
        paddle_x = paddle_l[1].xcor()
        if abs((paddle_x - ball_x)) <= 94:
            paddle_sound.play()
            if (paddle_x - ball_x) > 41:
                p_side = "left"
            elif (paddle_x - ball_x) < -41:
                p_side = "right"
            elif abs((paddle_x - ball_x)) < 41:
                p_side = "center"
            if ball_x - old_ball_x > 0:
                b_side = "left"
            else:
                b_side = "right"
            return p_side, b_side, True
        else:
            p_side = ""
            return p_side, b_side, False

    def ball_speed(self, start_time):
        end_time = time.time()
        time_elapsed = end_time - start_time  # elapsed time
        if time_elapsed >= 120:
            self.move_speed = 0.02
        elif time_elapsed >= 80:
            self.move_speed = 0.03
        elif time_elapsed >= 50:
            self.move_speed = 0.04
        elif time_elapsed >= 30:
            self.move_speed = 0.05
        elif time_elapsed >= 15:
            self.move_speed = 0.06
        else:
            self.move_speed = 0.07
        return self.move_speed
