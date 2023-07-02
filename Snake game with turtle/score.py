from turtle import Turtle

with open("score_bo.txt") as s_f:
    h_s = int(s_f.read())


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0,280)
        self.scor = 0
        self.h_score = h_s
        self.color("white")
        self.hideturtle()
        self.scoreboard()


    def scoreboard(self):
        self.clear()
        self.write(f"score: {self.scor} High score: {self.h_score} ",False,align="Center" , font=('bahnschrift semibold',12,'bold'))

    with open("score_bo.txt") as s_f:
        h_scor = s_f.read()

    def reset_score(self):
        if self.scor > self.h_score:
            self.h_score = self.scor

        self.scor = 0
        self.scoreboard()
        self.score_txt(str(self.h_score))


    def score_txt(self,h_score):
        with open("score_bo.txt",mode="w") as s_h:
            s_h.write(h_score)




    # # def game_over(self):
    #     self.goto(0,30)
    #     self.clear()
    #     self.color("white")
    #     self.write("Game over", False, align="Center", font=('bahnschrift semibold', 12, 'bold'))
    #     self.goto(0,0)
    #     self.write(f"Your final score is {self.scor}" , False, align="Center", font=('bahnschrift semibold', 12, 'bold'))

    def score_refresh(self):
        self.scor += 1
        self.scoreboard()
