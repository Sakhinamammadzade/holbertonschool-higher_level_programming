#!/usr/bin/python3
"""And now the Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Define new square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """method over"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str function """
        return f"[{__class__.__name__}] ({self.id})\
 {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns a key/value argument to attributes"""
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
