# Exercism triangle problem


def equilateral(sides):
    return len(sides) ==3 and all(side > 0 for side in sides) and sides[0] == sides[1] == sides[2]

def isosceles(sides):
    if len(sides) != 3 or not all(side > 0 for side in sides):
        return False
    a, b, c = sides
    if not (a + b > c and b + c > a and a + c > b):
        return False
    return a == b or b == c or a == c

def scalene(sides):
    if len(sides) != 3 or not all(side > 0 for side in sides):
        return False
    a, b, c = sides
    if not (a + b > c and b + c > a and a + c > b):
        return False
    return len(set(sides)) == 3