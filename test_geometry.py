from unittest import TestCase
from geometry import Circle
from geometry import Rectangle
import math


class Test(TestCase):
    def test_circle(self):
        # Define instance of Circle
        wheel = Circle(1)
        # Test __str__
        self.assertEqual(wheel.__str__(), "Circle of radius 1.")
        # Test area
        self.assertEqual(wheel.area(), math.pi)
        # Test circumference
        self.assertEqual(wheel.circumference(), 2 * math.pi)

    def test_rectangle(self):
        # Define instance of rectangle
        box = Rectangle(10, 5)
        # Test __str__
        self.assertEqual(box.__str__(), "Rectangle of length 10 and width 5.")
        # Test area
        self.assertEqual(box.area(), 50)
        # Test perimeter
        self.assertEqual(box.perimeter(), 30)
