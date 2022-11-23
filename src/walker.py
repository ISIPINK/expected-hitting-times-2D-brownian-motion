from utils import Position
from abc import ABC, abstractmethod
from random import randint

class Walker(ABC):

    """Base class for walker with different type of movements  """

    def __init__(self, pos:Position):
        self.position = pos

    @abstractmethod
    def walk1s(self):
        """TODO: this defines how the walker moves in 1 s = 1 time unit
        :returns: void

        """
        pass

class RandomWalker(Walker):

    """Walker that does standard random walk in 2D"""

    def __init__(self, pos: Position = Position(0,0), stepLenght: float = 1):
        Walker.__init__(self, pos)
        self.stepLenght = stepLenght

    def walk1s(self):
        randChoice = randint(0, 3)
        if randChoice == 0:
            self.position[0] += 1
        elif randChoice == 1:
            self.position[0] -= 1
        elif randChoice == 2:
            self.position[1] += 1
        elif randChoice == 3:
            self.position[1] -= 1

        
if __name__ == "__main__":  
    print("hello")
