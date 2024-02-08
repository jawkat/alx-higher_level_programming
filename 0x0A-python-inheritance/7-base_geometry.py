#!/usr/bin/python3
"""create an ampty class BaseGeometry
"""


class BaseGeometry:
    """create an ampty class BaseGeometry
    """
    def area(self):
        """raises an exception with the msg area is not implemented
        """
        raise Exception("Area is not implemented")

    def integer_validator(self, name, value):
        """validates the value

        Args:
            name (_type_): _description_
            value (_type_): _description_
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
