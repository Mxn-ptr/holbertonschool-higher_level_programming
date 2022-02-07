#!/usr/bin/python3

""" Define a Square class inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Represents a Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize the square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Return the representation of the square """
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                                                  self.x, self.y, self.width))

    @property
    def size(self):
        """ Get the size of the square """
        return self.width

    @size.setter
    def size(self, value):
        """ Change the size of the square """
        self.validator_input(width=value)
        self.validator_input(height=value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Change dimnensions, id or positions of the square """
        if args and len(args) > 0:
            list = ["id", "size", "x", "y"]
            for i, j in enumerate(args):
                setattr(self, list[i], j)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ Return the dictionary of the square """
        return {
            "id": self.id,
            "size": self.width,
            "y": self.y,
            "x": self.x
        }
