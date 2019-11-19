import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

color = np.zeros((9, 9),dtype=int)
array= [[1,2,8],[1,5,7],[1,9,9],
        [2,2,5],[2,5,2],[2,6,6],
        [3,2,2],[3,6,8],[3,7,5],
        [4,8,3],[4,9,7],
        [5,1,9],[5,3,6],[5,7,4],[5,9,1],
        [6,1,3],[6,2,1],
        [7,3,1],[7,4,3],[7,8,9],
        [8,4,1],[8,5,6],[8,8,8],
        [9,1,5],[9,5,8],[9,8,6]
        ]
# array = [[1, 4, 6], [1, 6, 4], [1, 7, 7], [2, 1, 7], [2, 3, 6], [2, 9, 9], [3, 6, 5], [3, 8, 8], [4, 2, 7], [4, 5, 2],
#          [4, 8, 9], [4, 9, 3], [5, 1, 8], [5, 9, 5], [6, 1, 4], [6, 2, 3], [6, 5, 1], [6, 8, 7], [7, 2, 5], [7, 4, 2],
#          [8, 1, 3], [8, 7, 2], [8, 9, 8], [9, 3, 2], [9, 4, 3], [9, 6, 1]]
def creatematrix(arr):
    matrix=np.zeros((9,9), dtype=int)
    for a in arr:
        matrix[a[0] - 1][a[1] - 1] = a[2]
        color[a[0] - 1][a[1] - 1]=1
    return matrix

def newmat(matrix,a):
    matrix1=matrix.copy()
    matrix1[a[0]-1][a[1]-1]=a[2]
    return matrix1

def getgrid(row,col):
    rowgrid,rowpos=divmod(row,3)
    colgrid,colpos=divmod(col,3)
    return (rowgrid*3+colgrid),(rowpos*3+colpos)

def getpos(grid,pos):
    griddiv,gridmod=divmod(grid,3)
    posdiv,posmod=divmod(pos,3)
    return griddiv*3+posdiv,gridmod*3+posmod

def adjustgrid(grids, a):
    row=a[0]-1
    col=a[1]-1
    value=a[2]
    rowdiv,rowmod=divmod(row,3)
    coldiv,colmod=divmod(col,3)
    grid,pos=getgrid(row,col)
    for i in range(3):
        grids[value-1][rowdiv*3+i]=grids[value-1][rowdiv*3+i] - set(np.arange(9)[divmod(np.arange(9),3)[0]==rowmod])
        grids[value-1][3*i+coldiv]=grids[value-1][3*i+coldiv] - set(np.arange(9)[divmod(np.arange(9),3)[1]==colmod])
    for i in range(9):
        grids[i][grid]=grids[i][grid]-{pos}
    grids[value - 1][grid] = {pos}

def adjustcolumn(columns, a):
    row = a[0] - 1
    col = a[1] - 1
    value = a[2]
    rowdiv, rowmod = divmod(row, 3)
    coldiv, colmod = divmod(col, 3)
    for i in range(3):
        columns[value - 1][coldiv * 3 + i] = columns[value - 1][coldiv * 3 + i]  - set( np.arange(9)[divmod(np.arange(9), 3)[0] == rowdiv])
    for i in range(9):
        columns[value-1][i]=columns[value-1][i] - {row} # Same number cannot be added in any column of the same row
        columns[i][col]=columns[i][col] - {row} # Remove current cell as a possible place from all other number's prospect
    columns[value-1][col] ={row}

def adjustrow(rows, a):
    row = a[0] - 1
    col = a[1] - 1
    value = a[2]
    rowdiv, rowmod = divmod(row, 3)
    coldiv, colmod = divmod(col, 3)
    for i in range(3):
        rows[value-1][rowdiv*3+i]=rows[value-1][rowdiv*3+i]- set(np.arange(9)[divmod(np.arange(9),3)[0]==coldiv])
    for i in range(9):
        rows[value-1][i]=rows[value-1][i] - {col}
        rows[i][row]=rows[i][row] -{col}
    rows[value-1][row]={col}

def adjustcell(cells, a):
    row=a[0]-1
    col=a[1]-1
    value=a[2]
    rowdiv, rowmod = divmod(row, 3)
    coldiv, colmod = divmod(col, 3)
    for i in range(9):
        cells[row][i]=cells[row][i] - {value}
        cells[i][col] = cells[i][col] - {value}
    for i in range(3):
        for j in range(3):
            cells[rowdiv*3+i][coldiv*3+j]=cells[rowdiv*3+i][coldiv*3+j]- {value}
    cells[row][col]={value}

def adjust(grids, columns, rows, cells, a):
    adjustgrid(grids, a)
    adjustcolumn(columns,a)
    adjustrow(rows, a)
    adjustcell(cells, a)



def solvesudoku(matrix):
    grids = np.full((9, 9), set(np.arange(9)))
    rows = np.full((9, 9), set(np.arange(9)))
    columns = np.full((9, 9), set(np.arange(9)))
    cells = np.full((9, 9), set(np.arange(1, 10)))
    for i in range(9):
        for j in range(9):
            if matrix[i][j]!=0:
                adjust(grids, columns, rows, cells, (i+1,j+1,matrix[i][j]))
    counter=1
    while counter > 0:
        counter = 0
        for i in range(9):
            value = i + 1
            for j in range(9):
                if len(grids[i][j])==0:
                    return False
                elif len(grids[i][j])==1:
                    pos=grids[i][j].pop()
                    grids[i][j].add(pos)
                    rowval,colval=getpos(j,pos)
                    if matrix[rowval][colval]==0:
                        matrix[rowval][colval] = value
                        adjust(grids, columns, rows, cells, (rowval+1,colval+1,value))
                        counter=counter+1
                    elif matrix[rowval][colval]!=value:
                        return False
                if len(rows[i][j])==0:
                    return False
                elif len(rows[i][j])==1:
                    colval=rows[i][j].pop()
                    rows[i][j].add(colval)
                    rowval=j
                    if matrix[rowval][colval]==0:
                        matrix[rowval][colval] = value
                        adjust(grids, columns, rows, cells, (rowval + 1, colval + 1, value))
                        counter = counter + 1
                    elif matrix[rowval][colval]!=value:
                        return False
                if len(columns[i][j])==0:
                    return False
                elif len(columns[i][j])==1:
                    rowval=columns[i][j].pop()
                    columns[i][j].add(rowval)
                    colval=j
                    if matrix[rowval][colval]==0:
                        matrix[rowval][colval] = value
                        adjust(grids, columns, rows, cells, (rowval + 1, colval + 1, value))
                        counter = counter + 1
                    elif matrix[rowval][colval]!=value:
                        return False
        for i in range(9):
            for j in range(9):
                if len(cells[i][j])==0:
                    return False
                elif len(cells[i][j])==1:
                    value=cells[i][j].pop()
                    cells[i][j].add(value)
                    if matrix[i][j]==0:
                        matrix[i][j] = value
                        adjust(grids, columns, rows, cells, (i + 1, j + 1, value))
                        counter = counter + 1
                    elif matrix[i][j]!=value:
                        return False
    for i in range(9):
        for j in range(9):
            if matrix[i][j]==0:
                for val in cells[i][j]:
                     if type(solvesudoku(newmat(matrix,(i+1, j+1, val)))).__name__!='bool':
                         matrix= solvesudoku(newmat(matrix,(i+1, j+1, val)))
                         break
    return  matrix

def printmatrix(matrix):
    plt.close('all')
    font1 = FontProperties()
    fig = plt.figure()
    ax = fig.gca()
    plt.gca().invert_yaxis()
    ax.set_xticks(np.arange(1, 10, 1), minor=True)
    ax.set_yticks(np.arange(0, 10, 1), minor=True)
    ax.set_xticks(np.arange(0, 10, 3), minor=False)
    ax.set_yticks(np.arange(0, 10, 3), minor=False)
    ax.grid(which='minor', linewidth=1)
    ax.grid(which='major', linewidth=2)
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    for i in range(9):
        for j in range(9):
            if color[i][j]==1 :
                font1.set_weight('bold')
            else:
                font1.set_weight('normal')
            plt.text((j + 0.4), (i + 0.7), matrix[i][j], fontproperties=font1)
    plt.show()


printmatrix(solvesudoku(creatematrix(array)))
