import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class TurtleKillers:

    def __init__(self):
        self.all_texans = []
        self.texan_speed = STARTING_MOVE_DISTANCE

    def create_killers(self):
        random_chance = random.randint(1, 100)
        if random_chance <= 20:
            new_texan = Turtle('square')
            new_texan.shapesize(stretch_wid=1, stretch_len=2)
            new_texan.penup()
            new_texan.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_texan.goto(300, random_y)
            new_texan.speed = self.texan_speed
            self.all_texans.append(new_texan)
        elif random_chance == 69:
            new_texan = Turtle('classic')
            new_texan.shapesize(stretch_wid=1, stretch_len=2)
            new_texan.penup()
            new_texan.color('skyblue')
            random_y = random.randint(-250, 250)
            new_texan.goto(300, random_y)
            new_texan.speed = (self.texan_speed * 3)
            self.all_texans.append(new_texan)
    
    def move_texans(self):
        for texan in self.all_texans:
                texan.backward(texan.speed)


    def next_turtle(self):
        self.texan_speed += MOVE_INCREMENT


