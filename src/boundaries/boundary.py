from abc import ABC, abstractmethod
from collections import namedtuple

Position = namedtuple("Position", ["x", "y"])

class Boundary(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def getDistance(self, pos: Position) -> float:
        """Returns the distance of position to closest point on the boundary"""
        pass

    @abstractmethod
    def isInside(self, pos: Position) -> bool:
        """tests if a position is inside the boundary"""
        pass

    @abstractmethod
    def getxLimits(self) -> list:
        """Gets the xlimits for plotting the boundary"""
        pass

    @abstractmethod
    def getyLimits(self) -> list:
        """Gets the ylimits for plotting the boundary"""
        pass

    @abstractmethod
    def getAspect(self) -> float:
        """Gets the aspect for plotting the boundary"""
        pass

