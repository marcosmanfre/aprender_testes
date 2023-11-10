import pytest
import source.shapes as shapes
import math

class TestCircle:


    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = shapes.Circle(10)


    def teardown_method(self, method):
        print(f"Tearing down {method}")

    def test_radius(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_two(self):
        assert True