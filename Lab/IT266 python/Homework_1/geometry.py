import math

def circle_area(radius=1):
    res = math.pi * radius ** 2
    return res

def circle_line(radius=1):
    res = math.pi * radius 
    return res

def rectangle_area(width =1, height=1):
    res = width  * height
    return res

def rectangle_line(width =1, height=1):
    res = 2 * (width  * height)
    return res

def triangle_area(side_a=1, width=1, height=1):
    res = 0.5 * (width * height)
    return res

def triangle_line(side_a=1, side_b=1, side_c=1):
    res = side_a + side_b + side_c
    return res