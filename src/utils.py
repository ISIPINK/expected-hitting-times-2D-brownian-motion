from collections import namedtuple
from math import sqrt

Position = namedtuple("Position", ["x", "y"])

def distance(p1: Position, p2: Position):
    '''
    return distance between points
    '''
    return sqrt(sum((p1i-p2i)**2 for p1i, p2i in zip(p1, p2)))

if __name__ == "__main__":
# tests for distance (maybe later I move them to a dedicated test file)
    p1 = Position(0, 0)
    p2 = Position(1, 0)
    p3 = Position(1, 1)

    print("this should be 1:",distance(p1, p2))
    print("this should be sqrt(2):",distance(p1, p3))

