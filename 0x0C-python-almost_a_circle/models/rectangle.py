#!/usr/bin/python3
""" Class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """Class of Rectangle

    Args:
        Base (Class): a super Class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """_summary_
        """
        return self.__width

    @width.setter
    def width(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        self.__width = value

    @property
    def height(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__height

    @height.setter
    def height(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        self.__height = value


r1 = Rectangle(10, 2)
print(r1.id)

r2 = Rectangle(2, 10)
print(r2.id)

r3 = Rectangle(10, 2, 0, 0, 12)
print(r3.id)
