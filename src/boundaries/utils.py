import numpy as np 
from math import sqrt

def distance(p1: np.array, p2: np.array):
    '''
    return distance between points
    '''
    return sqrt(sum((p1i-p2i)**2 for p1i, p2i in zip(p1, p2)))

# tests for distance (maybe later I move them to a dedicated test file)
if __name__ == "__main__":
    p1 = np.array([0, 0])
    p2 = np.array([1, 1])
    print(distance(p1,p2))

