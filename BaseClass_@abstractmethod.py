# from abc import ABCMeta ,abstractmethod
# class Shape(metaclass=ABCMeta)

# easiy waY !
from abc import ABC , abstractmethod

class Shape(ABC):
    @abstractmethod
    def print_area(self):
        return 0

class Rectangle(Shape):
    shape='Rectangle'
    side=4
    def __init__(self):
        self.breadth=6
        self.length=7
    def print_area(self):
        return self.breadth * self.length


rect1=Rectangle()
# shp=Shape() # TODO  we do not make abstract bass class instance or object

print(rect1.print_area())
input()