from time import sleep
from turtle import Screen
from playa import PreciousLilOne
from turtle_killers import TurtleKillers
from safe_turtle_board import SafeTurtleBoard


screen = Screen()
screen.setup(width=600, height=650)
screen.tracer(0)

playa = PreciousLilOne()
turtle_killers = TurtleKillers()
safe_turtle_board = SafeTurtleBoard()

screen.listen()
screen.onkey(playa.go_up,'Up')
screen.onkey(playa.go_left, 'Left')
screen.onkey(playa.go_right, 'Right')
screen.onkey(playa.go_down, 'Down')
screen.onkey(playa.leap_forward, ' ')




game_is_on = True
while game_is_on:
    sleep(0.05)
    screen.update()

    turtle_killers.create_killers()
    turtle_killers.move_texans()

    # Dead Turtle
    for texan in turtle_killers.all_texans:
        if texan.distance(playa) < 20:
            sleep(1)
            safe_turtle_board.want_to_kill_more_turtles_ehh()
            safe_turtle_board.dead_turtle()
            playa.go_to_start()


    #Happy Turtle
    if playa.made_it_safe():
        playa.go_to_start()
        turtle_killers.next_turtle()
        safe_turtle_board.increase_texan_ignorance_level()



screen.exitonclick()