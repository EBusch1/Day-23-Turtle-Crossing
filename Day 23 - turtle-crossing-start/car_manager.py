from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def spawn_car(self):
        random_chance = random.randint(1, 4)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.speed("fastest")
            new_car.shapesize(stretch_wid=None, stretch_len=2, outline=None)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(x=300, y=random.randint(-250, 250))
            self.all_cars.append(new_car)

    def car_move(self):
        for car in self.all_cars:
            car.back(self.move_speed)

            if car.xcor() < -340:
                self.all_cars.remove(car)

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT
