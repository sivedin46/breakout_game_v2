from turtle import Turtle

MOVE_INC = 50


class Paddle(Turtle):
    def __init__(self):   # creates three paddle and a list of paddles for other methods' usage
        super().__init__()
        self.center = Turtle()
        self.center.shape("square")
        self.center.color("white")
        self.center.penup()
        self.center.shapesize(stretch_wid=1, stretch_len=4, outline=0)
        self.center.goto(0, -290)
        self.center.showturtle()

        self.left = Turtle()
        self.left.shape("square")
        self.left.color("white")
        self.left.penup()
        self.left.shapesize(stretch_wid=1, stretch_len=2, outline=0)
        self.left.goto(-61.5, -290)
        self.left.showturtle()

        self.right = Turtle()
        self.right.shape("square")
        self.right.color("white")
        self.right.penup()
        self.right.shapesize(stretch_wid=1, stretch_len=2, outline=0)
        self.right.goto(61.4, -290)
        self.right.showturtle()
        self.paddle_l = [self.left, self.center, self.right]

    def go_right(self):
        if self.right.xcor() < 360:
            for pad in self.paddle_l:
                new_x = pad.xcor()
                pad.goto(new_x + MOVE_INC, pad.ycor())

    def go_left(self):
        if self.left.xcor() > -360:
            for pad in self.paddle_l:
                new_x = pad.xcor()
                pad.goto(new_x - MOVE_INC, pad.ycor())

    def reset_position(self):
        self.left.goto(-60, -290)
        self.center.goto(0, -290)
        self.right.goto(60, -290)
