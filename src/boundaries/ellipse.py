from .boundary import Boundary
import numpy as np

class Ellipse(Boundary):
    def __init__(self, a: float, alpha: float, b: float, beta: float) -> None:
        """
        Init a ellipse object. The parameters come from
        ((position[0]-self.a)/self.alpha)**2+((position[0]-self.b)/self.beta)**2 = 1
        """
        if alpha == 0 or beta == 0:
            raise Exception("alpha/beta of an ellipse must be non zero")
        self.a = a
        self.b = b
        self.alpha = alpha
        self.beta = beta

    def getDistance(self, position: np.array) -> float:
        """Returns the distance of position to closest point on the boundary"""
        # TODO:write this function  <05-11-22, > 
        pass

    def isInside(self, pos: np.array) -> bool:
        """ test whether a point is inside or not"""
        return ((pos[0]-self.a)/self.alpha)**2+((pos[0]-self.b)/self.beta)**2 < 1

    def getxLimits(self) -> list:
        """Gets the xlimits for plotting the boundary"""
        return [(self.a-self.alpha)*1.2, (self.a+self.alpha)*1.2]

    def getyLimits(self) -> list:
        """Gets the ylimits for plotting the boundary"""
        return [(self.b-self.beta)*1.2, (self.b+self.beta)*1.2]

    def getAspect(self) -> float:
        """Gets the aspect for plotting the boundary"""
        # TODO: maybe its reverse 
        return self.beta/self.alpha

