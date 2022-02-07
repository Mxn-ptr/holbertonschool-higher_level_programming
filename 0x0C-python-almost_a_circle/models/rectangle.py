#!/usr/bin/python3

""" Define a Rectangle class inherits from Base """
from models.base import Base


class Rectangle(Base):
    """ Represent a rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize the rectangle
            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
                x (int): horizontal position of the rectangle
                y (int): vertical position of the rectangle

            Raises:
                TypeError: if an input is not an int
                ValueError: if width or height are equal or less than 0
                ValueError: if x or y are less than 0 """
        self.validator_input(width=width, height=height, x=x, y=y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @staticmethod
    def validator_input(**kwargs):
        """ Function for validate the arg of the init function
            and for set value """
        for k, v in kwargs.items():
            if k == "width" or k == "height":
                if type(v) != int:
                    raise TypeError("{} must be an integer".format(k))
                if v <= 0:
                    raise ValueError("{} must be > 0".format(k))
            else:
                if type(v) != int:
                    raise TypeError("{} must be an integer".format(k))
                if v < 0:
                    raise ValueError("{} must be >= 0".format(k))

    @property
    def width(self):
        """ Get the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Change the width """
        self.validator_input(width=value)
        self.__width = value

    @property
    def height(self):
        """ Get the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Change the height """
        self.validator_input(height=value)
        self.__height = value

    @property
    def x(self):
        """ Get the horizontal position """
        return self.__x

    @x.setter
    def x(self, value):
        """ Change the horizontal position """
        self.validator_input(x=value)
        self.__x = value

    @property
    def y(self):
        """ Get the vertical position """
        return self.__y

    @y.setter
    def y(self, value):
        """ Change the vertical position """
        self.validator_input(y=value)
        self.__y = value

    def area(self):
        """ Return the area of the rectangle """
        return (self.__width * self.__height)

    def display(self):
        """ Display the rectangle with horizontal and vertical
            position with the character "#" """
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for m in range(self.__x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """ Represents the rectangle """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                        self.__y, self.__width,
                                                        self.__height))

    def update(self, *args, **kwargs):
        """ Change the dimensions or positions of the rectangle """
        if args and len(args) > 0:
            list = ["id", "width", "height", "x", "y"]
            for i, v in enumerate(args):
                setattr(self, list[i], v)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ Return the dictionary of the rectangle """
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }
