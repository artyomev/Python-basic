from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    # weight = 0
    # fuel = 0
    # fuel_consumption = 0
    # started = False

    def __init__(self,
                 weight=0,
                 fuel=0,
                 fuel_consumption=0,
                 ):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError('Отсутствует топливо!')


    def move(self, distance):
        if self.fuel - self.fuel_consumption * distance >= 0:
            self.fuel -= self.fuel_consumption * distance
        else:
            raise NotEnoughFuel('Недостаточно топлива!')

