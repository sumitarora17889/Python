import numpy as np
import matplotlib.pyplot as plt

set=set(np.arange(1,10))
grids = np.full((9, 9), set)
rows= np.full((9, 9), set)
columns=np.full((9, 9), set)
matrix=np.zeros((9,9), dtype=int)
array = [[1, 4, 6], [1, 6, 4], [1, 7, 7], [2, 1, 7], [2, 3, 6], [2, 9, 9], [3, 6, 5], [3, 8, 8], [4, 2, 7], [4, 5, 2],
         [4, 8, 9], [4, 9, 3], [5, 1, 8], [5, 9, 5], [6, 1, 4], [6, 2, 3], [6, 5, 1], [6, 8, 7], [7, 2, 5], [7, 4, 2],
         [8, 1, 3], [8, 7, 2], [8, 9, 8], [9, 3, 2], [9, 4, 3], [9, 6, 1]]

def adjust(a):


def insert(a):
    matrix[a[0]][a[1]]=a[2]
    adjust(a)


