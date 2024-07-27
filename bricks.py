from turtle import Turtle

COLORS = ["green", "yellow", "orange", "red", "brown", "gray"]
Y_POSITIONS = [0, 30, 60, 90, 120, 150]
X_INCREMENT = 21


class Bricks(Turtle):
    def __init__(self):
        super().__init__()
        self.bricks = []  # creates alist of bricks object for usage in methods of game
        self.bricks_counter = 0  # counter used for adding new bricks' color and y position  in level 2 and level 3
        self.create_new_brick(4)

    def create_new_brick(self, row):
        for index in range(row):  # ıf you want more bricks increase COLOR[],Y_POSITIONS  and range
            x_position = -423   # start point for first brick's center position
            while x_position < 355:  # limit for last brick's center position
                new_brick = Turtle()
                new_brick.shape("square")
                new_brick.color(COLORS[(index + self.bricks_counter) % len(COLORS)])
                new_brick.shapesize(1, 2.12, 0)
                new_brick.penup()
                new_brick.goto((x_position + X_INCREMENT * 2 + 10),
                               Y_POSITIONS[(index + self.bricks_counter) % len(Y_POSITIONS)])
                self.bricks.append(new_brick)
                x_position = new_brick.xcor()
        self.bricks_counter += row

    def brick_delete(self, index):
        removed_brick = self.bricks.pop(index)
        removed_brick.hideturtle()
