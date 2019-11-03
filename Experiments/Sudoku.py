import numpy as np
import matplotlib.pyplot as plt

matrix = np.full((9, 9, 9), True)


def printsudoku(array):
    fig = plt.figure()
    ax = fig.gca()
    plt.gca().invert_yaxis()
    ax.set_xticks(np.arange(1, 10, 1), minor=True)
    ax.set_yticks(np.arange(0, 10, 1), minor=True)
    ax.grid(which='minor', lw=20)
    plt.grid()
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    for i in range(len(array)):
        plt.text((array[i][1] - 0.6), (array[i][0] - 0.3), array[i][2])


# entries = int(input('Enter Number of Entries:'))

array = [[1, 4, 6], [1, 6, 4], [1, 7, 7], [2, 1, 7], [2, 3, 6], [2, 9, 9], [3, 6, 5], [3, 8, 8], [4, 2, 7], [4, 5, 2],
         [4, 8, 9], [4, 9, 3], [5, 1, 8], [5, 9, 5], [6, 1, 4], [6, 2, 3], [6, 5, 1], [6, 8, 7], [7, 2, 5], [7, 4, 2],
         [8, 1, 3], [8, 7, 2], [8, 9, 8], [9, 3, 2], [9, 4, 3], [9, 6, 1]]

printsudoku(array)


def adjust(matrix, row, col, value):
    if matrix[row-1][col-1][value-1]:
        g1 = divmod(row-1, 3)[0] * 3
        g2 = divmod(col-1, 3)[0] * 3
        matrix[row - 1,:,value - 1] = False
        matrix[:,col - 1,value - 1] = False
        matrix[g1: g1 + 3,g2: g2 + 3,value - 1] = False
        print(np.any(matrix[:][:]))





print(matrix.shape)
adjust(matrix, 1, 4, 6)
print(matrix)