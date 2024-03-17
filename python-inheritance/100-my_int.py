#!/usr/bin/python3
"""MyInt eq and ne methods"""


class MyInt(int):
    def __eq__(self, other):
        """override the == operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """override the != operator"""
        return super().__eq__(other)
