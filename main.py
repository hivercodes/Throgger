import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Throgger")
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.move, "Up")

carmanager = CarManager()
timer = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carmanager.make_car()
    carmanager.move()





















screen.exitonclick()