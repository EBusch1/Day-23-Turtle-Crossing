import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("grey")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_forward, "Up")
screen.onkeypress(player.move_backward, "Down")

game_is_on = True
while game_is_on:
    # print(len(car_manager.all_cars))
    time.sleep(0.1)
    screen.update()

    car_manager.spawn_car()
    car_manager.car_move()

    # detect successful crossing, rest player position and increment level
    if player.ycor() > 280:
        player.starting_position()
        car_manager.increase_speed()
        scoreboard.next_level()

    # detect collision with a car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            # print("ouch")
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
