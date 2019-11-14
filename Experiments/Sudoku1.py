import numpy as np
import matplotlib.pyplot as plt

sets=set(np.arange(9))
grids = np.full((9, 9), sets)
rows= np.full((9, 9), sets)
columns=np.full((9, 9), sets)
matrix=np.zeros((9,9), dtype=int)
array = [[1, 4, 6], [1, 6, 4], [1, 7, 7], [2, 1, 7], [2, 3, 6], [2, 9, 9], [3, 6, 5], [3, 8, 8], [4, 2, 7], [4, 5, 2],
         [4, 8, 9], [4, 9, 3], [5, 1, 8], [5, 9, 5], [6, 1, 4], [6, 2, 3], [6, 5, 1], [6, 8, 7], [7, 2, 5], [7, 4, 2],
         [8, 1, 3], [8, 7, 2], [8, 9, 8], [9, 3, 2], [9, 4, 3], [9, 6, 1]]

def getgrid(row,col):
    rowgrid,rowpos=divmod(row,3)
    colgrid,colpos=divmod(col,3)
    return (rowgrid*3+colgrid),(rowpos*3+colpos)

def getpos(grid,pos):
    griddiv,gridmod=divmod(grid,3)
    posdiv,posmod=divmod(pos,3)
    return griddiv*3+posdiv,gridmod*3+posmod

def adjust(a):
    row=a[0]-1
    col=a[1]-1
    value=a[2]
    rowdiv,rowmod=divmod(row,3)
    coldiv,colmod=divmod(col,3)
    grid,pos=getgrid(row,col)
    for i in range(3):
        grids[value-1][rowdiv*3+i]=grids[value-1][rowdiv*3+i] - set(np.arange(9)[divmod(np.arange(9),3)[0]==rowmod])
        grids[value-1][3*i+coldiv]=grids[value-1][3*i+coldiv] - set(np.arange(9)[divmod(np.arange(9),3)[1]==colmod])
        rows[value-1][rowdiv*3+i]=rows[value-1][rowdiv*3+i]- set(np.arange(9)[divmod(np.arange(9),3)[0]==coldiv])
        columns[value - 1][coldiv * 3 + i] = rows[value - 1][coldiv * 3 + i] - set(
            np.arange(9)[divmod(np.arange(9), 3)[0] == rowdiv])
    for i in range(9):
        columns[value-1][i]=columns[value-1][i] - {row}
        rows[value-1][i]=rows[value-1][i] - {col}
        grids[i][grid]=grids[i][grid]-{pos}
    grids[value-1][grid]={pos}
    rows[value-1][row]={col}
    columns[value-1][col] ={row}

def insert(a):
    matrix[a[0]-1][a[1]-1]=a[2]
    adjust(a)

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

for a in array:
    insert(a)
print(grids)
printsudoku(matrix)
for i in range(9):
    for i in range(9):
        value=i+1
        for j in range(9):
            if len(grids[i][j])==0:
                print("No Solution Found")
            elif len(grids[i][j])==1:
                pos=grids[i][j].pop()
                grids[i][j].add(pos)
                rowval,colval=getpos(j,pos)
                if matrix[rowval][colval]==0:
                    insert((rowval+1,colval+1,value))
                elif matrix[rowval][colval]!=value:
                    print("Solution Error")
            if len(rows[i][j])==0:
                print("No Solution Found")
            elif len(rows[i][j])==1:
                colval=rows[i][j].pop()
                rows[i][j].add(colval)
                rowval=j
                if matrix[rowval][colval]==0:
                    insert((rowval+1,colval+1,value))
                elif matrix[rowval][colval]!=value:
                    print("Solution Error")
            if len(columns[i][j])==0:
                print("No Solution Found")
            elif len(columns[i][j])==1:
                rowval=columns[i][j].pop()
                columns[i][j].add(rowval)
                colval=j
                if matrix[rowval][colval]==0:
                    insert((rowval+1,colval+1,value))
                elif matrix[rowval][colval]!=value:
                    print("Solution Error")

print(matrix)
print(grids)
printsudoku(matrix)
print(len(np.nonzero(matrix)[0]))