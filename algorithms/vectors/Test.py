mat=[9.53125802, 1.86716702, 1.35296478, 0.91558412]

def diagonal(array, row, column):
    Diag=[]
    for i in range(row):

        print(i)
        row=[]
        for j in range(column):
            if i==j:
                row.append(array[i])
            else:
                row.append(0)
        Diag.append(row)
    return Diag

print(diagonal(mat,4,5))