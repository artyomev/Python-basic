"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle


class Car(Vehicle):
    engine = object

    def set_engine(self, engine: engine):
        self.engine = engine

