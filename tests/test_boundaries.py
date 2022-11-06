#still have to find a way to do this without sys
import numpy as np
import sys
sys.path.insert(0, '..')

import src.boundaries as boundaries

recy = boundaries.Rectangle(radius1= 10, radius2 = 20)
pos1 = np.array([0,0]) 
pos2 = np.array([20,0]) 
print(recy.isInside(pos1))
print(recy.isInside(pos2))
