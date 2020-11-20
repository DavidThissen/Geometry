"""
The module geometry provides classes for circles and rectangles.
"""

import math


class Circle:
    """
    The Circle class provide methods for circle manipulation.
    """

    def __init__(self, radius: float):
        """
        Creates instance of type Circle
        :param radius: a float
        :return: none
        """

        self.radius = radius

    def __str__(self):
        """
        Returns a string description of Circle instance
        :return: str
        """
        return "Circle of radius " + format(self.radius) + "."

    def area(self) -> float:
        """
        Calculates area of circle.
        :return: float
        """

        return math.pi * self.radius ** 2

    def circumference(self) -> float:
        """
        Calculates circumference of circle.
        :return: float
        """
        return 2*math.pi*self.radius


class Rectangle:
    """
    The Rectangle class provide methods for rectangle manipulation.
    """

    def __init__(self, length: float, width: float):
        """
        Creates instance of type Rectangle
        :param length: a float
        :param width: a float
        :return: none
        """

        self.length = length
        self.width = width

    def __str__(self):
        """
        Returns a string description of Rectangle instance
        :return: str
        """
        return "Rectangle of length " + format(self.length) + " and width " + format(self.width) + "."

    def area(self) -> float:
        """
        Calculates area of rectangle.
        :return: float
        """

        return self.length*self.width

    def perimeter(self) -> float:
        """
        Calculates perimeter of rectangle.
        :return: float
        """
        return 2*(self.length+self.width)
