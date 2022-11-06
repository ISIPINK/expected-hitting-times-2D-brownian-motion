import unittest
import numpy as np
import sys #still have to find a way to do this without sys

sys.path.insert(0, '..')
import src.boundaries as boundaries

# TODO add test for important methods
class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.recy = boundaries.Rectangle(radius1= 10, radius2 = 20)
        self.pos1 = np.array([0,0]) 
        self.pos2 = np.array([20,0]) 

    def test_isInside(self):
        self.assertTrue(self.recy.isInside(self.pos1))
        self.assertFalse(self.recy.isInside(self.pos2))

class TestEllipse(unittest.TestCase):

    def setUp(self):
        self.elly = boundaries.Ellipse(a=0,alpha=1,b=0,beta=1)
        self.pos1 = np.array([0,0]) 
        self.pos2 = np.array([2,0]) 

    def test_isInside(self):
        self.assertTrue(self.elly.isInside(self.pos1))
        self.assertFalse(self.elly.isInside(self.pos2))

if __name__ == '__main__':
    unittest.main()
