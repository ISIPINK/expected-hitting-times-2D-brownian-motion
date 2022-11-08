import unittest
import sys  # still have to find a way to do this without sys
from collections import namedtuple

sys.path.insert(0, '..')

import src.boundaries as boundaries

Position = namedtuple("Position", ["x", "y"])

class TestRectangle(unittest.TestCase):

    '''
    tests the class Rectangle
    '''

    def setUp(self):
        self.recy = boundaries.Rectangle(radius1=10, radius2=20)
        self.pos1 = Position(0, 0)
        self.pos2 = Position(20, 0)
        self.pos3 = Position(5, 5)


    def test_getDistance(self):
        self.assertEqual(self.recy.getDistance(self.pos1), 10)
        self.assertEqual(self.recy.getDistance(self.pos2), 10)
        self.assertEqual(self.recy.getDistance(self.pos3), 5)

    def test_isInside(self):
        self.assertTrue(self.recy.isInside(self.pos1))
        self.assertFalse(self.recy.isInside(self.pos2))
        self.assertTrue(self.recy.isInside(self.pos3))

    # other methods are for plotting purposes only


class TestEllipse(unittest.TestCase):
    '''
    tests the class Ellipse
    '''

    def setUp(self):
        # elly the unit circle gets unittested
        self.elly = boundaries.Ellipse(a=0, alpha=1, b=0, beta=1)
        self.pos1 = Position(0, 0)
        self.pos2 = Position(2, 0)
        self.pos3 = Position(1, 0)

    def test_isInside(self):
        self.assertTrue(self.elly.isInside(self.pos1))
        self.assertFalse(self.elly.isInside(self.pos2))
        self.assertFalse(self.elly.isInside(self.pos3))

    def test_isOn(self):
        self.assertFalse(self.elly.isOn(self.pos1))
        self.assertFalse(self.elly.isOn(self.pos2))
        self.assertTrue(self.elly.isOn(self.pos3))

    def test_getTheta(self):
        with self.assertRaises(ValueError):
            self.elly.getTheta(self.pos1)

        with self.assertRaises(ValueError):
            self.elly.getTheta(self.pos2)

        self.assertEqual(self.elly.getTheta(self.pos3),0)
        
    def test_getDistance(self):
        smallestFactor = min(self.elly.alpha, self.elly.beta)
        self.assertTrue(smallestFactor - 0.01 <=self.elly.getDistance(self.pos1) <= smallestFactor + 0.01)
        

if __name__ == '__main__':
    unittest.main()
