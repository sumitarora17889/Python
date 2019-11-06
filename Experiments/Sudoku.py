import numpy as np
import matplotlib.pyplot as plt

matrix = np.full((9, 9, 9), True)

sudokumat=np.zeros(shape=(9,9),dtype=int)

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
    for i in range(9):
        for j in range(9):
            if array[i][j]!=0:
                plt.text((j +1- 0.6), (i +1- 0.3), array[i][j])
    plt.show()

def printsudokufrommatrix(array):
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
            plt.text((j +1- 0.6), (i +1- 0.3), np.arange(1,10)[array[i][j]])
    plt.show()
# entries = int(input('Enter Number of Entries:'))

array = [[1, 4, 6], [1, 6, 4], [1, 7, 7], [2, 1, 7], [2, 3, 6], [2, 9, 9], [3, 6, 5], [3, 8, 8], [4, 2, 7], [4, 5, 2],
         [4, 8, 9], [4, 9, 3], [5, 1, 8], [5, 9, 5], [6, 1, 4], [6, 2, 3], [6, 5, 1], [6, 8, 7], [7, 2, 5], [7, 4, 2],
         [8, 1, 3], [8, 7, 2], [8, 9, 8], [9, 3, 2], [9, 4, 3], [9, 6, 1]]

for i in range(len(array)):
    sudokumat[array[i][0]-1][array[i][1]-1]=array[i][2]


def adjust(matrix, row, col, value):
    if matrix[row][col][value-1]:
        g1 = divmod(row, 3)[0] * 3
        g2 = divmod(col, 3)[0] * 3
        matrix[row,:,value - 1] = False
        matrix[:,col,value - 1] = False
        matrix[g1: g1 + 3,g2: g2 + 3,value - 1] = False
        matrix[row, col, :] = False
        matrix[row, col, value-1] = True
    else:
        return False
    return True


def solvesudoku(array):
    for i in range(9):
        for j in range(9):
            if array[i][j]!=0:
                if adjust(matrix, i, j, array[i][j])==False:
                    return False
    return True

print(sudokumat)

solvesudoku(sudokumat)
printsudoku(sudokumat)
printsudokufrommatrix(matrix)
print(matrix)

for i in range(1,10):
    for row in range(0,9):
        matrix[:][:][1]



# for i in range(9):
#     for j in range(9):
#         print(np.arange(1,10)[matrix[i][j]])