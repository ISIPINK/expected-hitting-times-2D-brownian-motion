from abc import ABC, abstractmethod
import numpy as np

class Boundary(ABC):
    @abstractmethod
    def __init__(self ):
        pass

    @abstractmethod
    def getDistance(self, position: np.array) -> float:
        """Returns the distance of position to closest point on the boundary"""
        pass

    @abstractmethod
    def isInside(self, position: np.array) -> bool:
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

