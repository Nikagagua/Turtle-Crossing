from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        probability = randint(1, 10)
        if probability <= 3:
            new_car = Turtle("square")
            new_car.color(COLORS[randint(0, 5)])
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(300, randint(-250, 250))

            while any(new_car.distance(car) < 40 for car in self.cars):
                new_car.goto(300, randint(-250, 250))

            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
