import math

def circle_area(radius):
    res = []
    for m1 in radius:
        circle = math.pi * float(m1) ** 2
        res.append("%.2f" % circle)
    return res

def circle_line(radius):
    res = []
    for m1 in radius:
        circleline = math.pi * float(m1)
        res.append("%.2f" % circleline)
    return res
