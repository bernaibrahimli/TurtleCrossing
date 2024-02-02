from turtle import Screen
from player import Player
from car_manager import CarManager
import time
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.setup(600,600)
screen.bgpic("rsz_1rsz_bg1.png")
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.onkeypress(fun=player.move, key="Up")
screen.onkeypress(fun=player.down, key="Down")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.make_car()
    car_manager.move_car()

    #detect crash
    for car in car_manager.new_car:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on =False

    #level up
    if player.ycor() > 200:
        player.level_up()
        car_manager.sped_up()
        scoreboard.update_sb(player.level)


screen.exitonclick()