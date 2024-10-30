#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math

class Shape(ABC):
	@abstractmethod
	def area(self):
		pass

	@abstractmethod
	def perimeter(self):
		pass

class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius

	def area(self):
		return abs(math.pi * (self.radius ** 2))
	
	def perimeter(self):
		return abs((self.radius * 2) * math.pi)
	
class Rectangle(Shape):
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def area(self):
		return self.width * self.height
	
	def perimeter(self):
		return (self.width + self.height) * 2
	
def shape_info(object):
	print(f"Area: {object.area()}")
	print(f"Perimeter: {object.perimeter()}")