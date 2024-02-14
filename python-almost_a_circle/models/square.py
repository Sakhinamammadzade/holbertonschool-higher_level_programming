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
