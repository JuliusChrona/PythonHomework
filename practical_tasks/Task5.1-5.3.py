import math
from abc import abstractmethod, ABC


class GeometricFigure(ABC):

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_square(self):
        pass


class Circle(GeometricFigure):
    def __init__(self, radius):
        self.radius = radius

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def get_square(self):
        return math.pi * self.radius ** 2


class Rectangle(GeometricFigure):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_square(self):
        return (self.length + self.width) * 2

    def get_perimeter(self):
        return self.length * self.width

    def get_length_of_diagonal(self):
        diagonal_length = math.sqrt(self.length ** 2 + self.width ** 2)
        return diagonal_length

    def fits_in_circle(self, radius):
        return True if self.get_length_of_diagonal() <= 2 * radius else False
