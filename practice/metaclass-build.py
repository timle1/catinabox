from abc import (ABCMeta,
          abstractmethod)

class Vehicle(metaclass=ABCMeta):

    @abstractmethod
    def change_gear(self):
        pass

    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):

    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def change_gear(self):
        print("Changing gear")

    def start_engine(self):
        print("Changing engine")

car = Car("Audi", "A4", "white")
print(isinstance(car, Vehicle))
