from collections import namedtuple
from math import acos
from math import pi

from .boundary import Boundary
from .utils import distance

Position = namedtuple("Position", ["x", "y"])


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

    def getUpPoint(self):
        return Position(self.a, self.b + self.beta)

    def getRightPoint(self):
        return Position(self.a + self.alpha, self.b)

    def getDownPoint(self):
        return Position(self.a, self.b - self.beta)

    def getLeftPoint(self):
        return Position(self.a-self.alpha, self.b)

    def isOn(self, pos: Position):
        return ((pos[0]-self.a)/self.alpha)**2+((pos[1]-self.b)/self.beta)**2 == 1

 def getTheta(self, pos: Position):
      '''
        Return theta (parametric represention of ellipse )of a position
        on the boundary.
        '''
       if not (self.isOn(pos)):
            raise ValueError("The position has to be on the ellipse")

        # first I scale my coordinates so that the ellipse becomes an unitcircle
        x_c = (pos.x-self.a)/self.alpha
        y_c = (pos.y-self.b)/self.beta
        theta_Q1 = acos(x_c)

        # then I figure out in which quadrant that I'm working with
        if (x_c >= 0 and y_c >= 0):
            return theta_Q1
        elif (x_c < 0 and y_c >= 0):
            return pi - theta_Q1
        elif (x_c <= 0 and y_c <= 0):
            return pi + theta_Q1
        else:
            return 2*pi - theta_Q1

    def getClosestOuterPoint(self, pos: Position) -> Position:
        """Returns the closest outer point"""
        outerPoints = [self.getUpPoint(), self.getRightPoint(), self.getDonwPoint(), self.getLeftPoint()]
        bestPoint = outerPoints[0]
        for outerPoint in outerPoints:
            bestPoint = outerPoint if distance(outerPoint, pos) < distance(bestPoint, pos) else bestPoint
        return bestPoint


    def getDistance(self, pos: Position) -> float:
        """Returns the distance of position to closest point on the boundary"""
        # TODO:write this function  <05-11-22, >
        '''
        this is difficult to write
        I maybe need:
        - a parameteric rep of the ellipse
        - an optimizer
        '''
        pass

    def isInside(self, pos: Position) -> bool:
        """ test whether a point is inside or not"""
        return ((pos[0]-self.a)/self.alpha)**2+((pos[1]-self.b)/self.beta)**2 < 1

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

    def __str__(self):
        return f"Ellipse(a={self.a}, alpha= {self.alpha}, b={self.b}, beta={self.beta})"

