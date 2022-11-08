from .boundary import Boundary

from collections import namedtuple


Position = namedtuple("Position", ["x", "y"])

class Rectangle(Boundary):
    def __init__(self, radius1: float, radius2: float) -> None:
        """Init a rectangle object with radiusi =sidei/2 radius cm"""
        if radius1 <= 0 or radius2 <= 0:
            raise Exception(
                "the radiuses of a rectangle must be strictly positive")
        self.radius1 = radius1
        self.radius2 = radius2

    def getDistance(self, pos: Position) -> float:
        """Returns the distance of position to closest point on the rectangle (works inside the rectangle)"""
        return min(abs(pos[0]-self.radius1), abs(pos[1]-self.radius2), abs(pos[0]+self.radius1), abs(pos[1]+self.radius2))

    def isInside(self, pos: Position) -> bool:
        """tests if a position is inside the rectangle"""
        return not(pos[0] > self.radius1 or pos[0] < -self.radius1 or pos[1] > self.radius2 or pos[1] < -self.radius2)

    def getxLimits(self) -> list:
        return [-self.radius1*1.2, self.radius1*1.2]

    def getyLimits(self) -> list:
        return [-self.radius2*1.2, self.radius2*1.2]

    def getAspect(self) -> float:
        return self.radius1/self.radius2

