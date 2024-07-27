from turtle import Turtle, Screen


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.record_s = 0
        self.level = 1
        self.life_count = "❤❤❤"
        self.font = ("courier", 12, "normal")
        self.life_pos = (-360, 270)
        self.level_pos = (-100, 270)
        self.speed_pos = (0, 270)
        self.record_pos = (230, 270)
        self.score_pos = (340, 270)
        self.speed = 1
        self.read_record()
        self.update_scoreboard()
        self.screen = Screen()

    def update_scoreboard(self):
        self.clear()
        self.goto(self.life_pos)
        self.write(self.life_count, align="center", font=self.font, )
        self.goto(self.level_pos)
        self.write(f"Level: {self.level}", align="center", font=self.font, )
        self.goto(self.speed_pos)
        self.write(f"Speed: {self.speed}", align="center", font=self.font, )
        self.goto(self.record_pos)
        self.write(f"Record: {self.record_s}", align="center", font=self.font)
        self.goto(self.score_pos)
        self.write(f"Score: {self.score}", align="center", font=self.font)

    def read_record(self):
        try:
            with open("records.txt", 'r', encoding='utf-8') as file:
                self.record_s = int(file.readline().strip())
                record = int(self.record_s) if self.record_s else 0
        except FileNotFoundError:
            self.record_s = 0

    def check_record(self):
        if self.score > self.record_s:
            self.record_s = self.score
            with open("records.txt", 'w', encoding='utf-8') as file:
                file.write(f"{self.record_s}")
            self.update_scoreboard()

    def point(self, brick):
        if brick.color()[0] == "green":
            self.score += 4
        elif brick.color()[0] == "yellow":
            self.score += 5
        elif brick.color()[0] == "orange":
            self.score += 6
        elif brick.color()[0] == "red":
            self.score += 7
        self.update_scoreboard()
        return self.score

    def you_win(self):
        self.clear()
        self.goto(0, 0)
        self.write("You Win'''", align="center", font=("courier", 80, "normal"))
        self.screen.update()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("courier", 80, "normal"))
        self.goto(self.score_pos)
        self.write(f"Score: {self.score}", align="center", font=self.font)
        self.screen.update()

    def level_check(self):
        self.level += 1
        self.update_scoreboard()
        return self.level

    def speed_write(self, temp_speed):
        if temp_speed == 0.07:
            self.speed = 1
        elif temp_speed == 0.06:
            self.speed = 2
        elif temp_speed == 0.05:
            self.speed = 3
        elif temp_speed == 0.04:
            self.speed = 4
        elif temp_speed == 0.03:
            self.speed = 5
        elif temp_speed == 0.02:
            self.speed = 6
        self.update_scoreboard()
