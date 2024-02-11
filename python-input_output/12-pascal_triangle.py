#!/usr/bin/python3
""" documentation """


def pascal_triangle(n):
    """ pascal triangle """
    triangle = [[1]*(i+1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    return triangle
