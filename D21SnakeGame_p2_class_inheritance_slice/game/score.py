# Iska seedha matlab hai: Score class khud ek Turtle ban chuki hai.

# Hume alag se t = Turtle() banakar baar-baar t.goto() ya t.penup() likhne ki zaroorat nahi padti.

# Score class ko Turtle ki saari abilities (move karna, text likhna, color change karna) directly self ke zariye mil jaati hain.

# ________________________________
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()     
        self.score = 0            
        self.color("#FFF4E6")       
        self.penup()              
        self.goto(0, 265)         # 5. Screen ke top center par position set karta hai
        self.hideturtle()
        self.update_scoreboard()  # 7. Initial score print karta hai

    def update_scoreboard(self):
        self.clear()              # 8. Purana score mitata hai taaki overlapping na ho
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self,points=1):
        self.score += points
        self.update_scoreboard()  # Score badhakar screen par refresh karta hai

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)