from turtle import Turtle, Screen
import os
ALIGNMENT = 'center'
FONT = ("Papyrus", 24, "bold")
screen = Screen()

class SafeTurtleBoard(Turtle):
    david_point_file = 'Happy_Turtles.txt'

    def __init__(self):
        super().__init__()
        self.level = 0
        self.most_saved_turtles = 0
        self.color('pink')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_safe_turtle_board()
        self.loading_point_daddy()

    def update_safe_turtle_board(self):
        self.clear()
        if self.level == 0:
            self.loading_point_daddy()
        self.goto(0, 270)
        self.write(f'Turtles Saved:{self.level} High Score: {self.most_saved_turtles}', align=ALIGNMENT, font=FONT)

    def high_turtle_score(self):
        if self.level >= self.most_saved_turtles:
            self.most_saved_turtles = self.level
        self.level = 0
        self.update_safe_turtle_board()


    def want_to_kill_more_turtles_ehh(self):
        self.goto(0, 0)
        self.write('kill more turtles? (y/n)', align='center', font=FONT)
        screen.onkey(self.high_turtle_score, 'y')
        screen.onkey(screen.exitonclick, 'n')

    def increase_texan_ignorance_level(self):
        self.level += 1
        if self.level >= self.most_saved_turtles:
            self.most_saved_turtles = self.level
        self.update_safe_turtle_board()

    def dead_turtle(self):
        self.goto(0, 40)
        self.write(f'DEAD TURTLE', align="center", font=FONT)
        self.save_the_chosen_one()


    def loading_point_daddy(self):
        filepath = os.path.join(os.path.dirname(__file__), self.david_point_file)
        try:
            with open(filepath, 'r') as f:
                self.most_saved_turtles = int(f.read())
        except FileNotFoundError:
            pass

    def save_the_chosen_one(self):
        filepath = os.path.join(os.path.dirname(__file__), self.david_point_file)
        with open(filepath, 'w') as f:
            f.write(str(self.most_saved_turtles))
