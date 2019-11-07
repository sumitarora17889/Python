import numpy as np
import matplotlib.pyplot as plt

set=set(np.arange(1,10))
matrix = np.full((9, 9), set)
print(matrix)

def printsudoku(matrix):
    fig = plt.figure()
    ax = fig.gca()
    plt.gca().invert_yaxis()
    ax.set_xticks(np.arange(1, 10, 1), minor=True)
    ax.set_yticks(np.arange(0, 10, 1), minor=True)
    ax.grid(which='minor', lw=20)
    plt.grid()
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    for i in range(9):
        for j in range(9):
            plt.text((j+0.4), (i +0.7), matrix[i][j])
    plt.show()


# entries = int(input('Enter Number of Entries:'))

array = [[1, 4, 6], [1, 6, 4], [1, 7, 7], [2, 1, 7], [2, 3, 6], [2, 9, 9], [3, 6, 5], [3, 8, 8], [4, 2, 7], [4, 5, 2],
         [4, 8, 9], [4, 9, 3], [5, 1, 8], [5, 9, 5], [6, 1, 4], [6, 2, 3], [6, 5, 1], [6, 8, 7], [7, 2, 5], [7, 4, 2],
         [8, 1, 3], [8, 7, 2], [8, 9, 8], [9, 3, 2], [9, 4, 3], [9, 6, 1]]

printsudoku(matrix)


def adjust(matrix, row, col, value):
    if value in matrix[i][j]:
        g1 = divmod(row-1, 3)[0] * 3
        g2 = divmod(col-1, 3)[0] * 3
        matrix[row - 1,:,value - 1] = False
        matrix[:,col - 1,value - 1] = False
        matrix[g1: g1 + 3,g2: g2 + 3,value - 1] = False
        matrix[row - 1, col-1, :] = False
        matrix[row - 1, col-1, value-1] = True
    else:
        return False
    return True


def solvesudoku(array):
    for i in range(len(array)):
        if adjust(matrix, array[i][0], array[i][1], array[i][2])==False:
            return False
    return True

# solvesudoku(array)
#
# for i in range(9):
#     for j in range(9):
#         print(np.arange(1,10)[matrix[i][j]])