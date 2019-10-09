# Input Matrix

# Enter Dimensions
R=int(input("Enter rows in matrix: "))
C=int(input("Enter columns in matrix: "))

# Function to swap rows
def rowswap(matrix, r1, r2):
    temprow=matrix[r1]
    matrix[r1]=matrix[r2]
    matrix[r2]=temprow

def findpivot(matrix, row):
    for j in range(C):
        if j!=0:
            break
    return j
def normalizepivot(matrix, R,C, start,pivotcolumn):
    pivot=matrix[start][pivotcolumn]
    for i in range(C):
        matrix[start][i]=matrix[start][i]/pivot
def normalizerows(matrix, R,C, row,pivotcolumn):
    for i in range(row+1,R):
        pivot=matrix[i][pivotcolumn]
        for j in range(pivotcolumn, C):
            matrix[i][j] = matrix[i][j]  - (matrix[row][j]* pivot)
# Function to convert the matrix in row echelon form
def rowechelon(matrix,R,C,startrow,pivotcolumn):
    if pivotcolumn<C and startrow<R:
        start=startrow
        pivotrow=startrow
        for i in range(startrow,R):
            if matrix[i][pivotcolumn]!=0:
                pivotrow = i
                break
        if start!=pivotrow:
            rowswap(matrix,start,pivotrow)
        print(matrix)
        if matrix[start][pivotcolumn] not in range(2):
            normalizepivot(matrix,R,C,start,pivotcolumn)
        normalizerows(matrix, R,C, startrow,pivotcolumn)
        rowechelon(matrix,R,C,startrow+1,pivotcolumn+1)

def reducerows(matrix, R,C,row, col):
    for i in range(row):
        pivot=matrix[i][col]
        for j in range(C):
            matrix[i][j]=matrix[i][j] - pivot*matrix[row][j]

def reducedrowechelon(matrix, R,C,row):
    for i in range(row, 0,-1):
        for j in range(C):
            if matrix[i][j]==1:
                reducerows(matrix,R,C,i,j)
#Initialize Matrix
matrix=[]

#Input Matrix
for i in range(R):
    row=[]
    for j in range(C):
        row.append(int(input()))
    matrix.append(row)

print(matrix)
rowechelon(matrix, R,C,0,0)
print("Row Echelon")
print(matrix)
reducedrowechelon(matrix, R,C,R-1)
print("Reduced Row Echelon")
print(matrix)
solution=[]
count=[]
solutionflag=''
for i in range(R-1,-1,-1):
    count.append(0)
for j in range(C-1):
    solution.append(0)
for i in range(R-1,-1,-1):
    for j in range(C-1):
        if matrix[i][j]!=0:
            count[i]=count[i]+1

    if count[i]==0 and matrix[i][C-1]!=0:
        solutionflag='no'
        break
    elif count[i]==0 and matrix[i][C-1]==0:
        solutionflag='yes'
    elif count[i]==1:
        solutionflag='yes'
    else:
        solutionflag='many'
        break
if solutionflag=='yes':
    for i in range(R):
            print(matrix[i][C - 1])

