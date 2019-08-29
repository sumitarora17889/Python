import numpy as np
import math
R= int(input("enter Rows: "))
C= int(input("Enter Columns: "))

print(R)
print(C)

matrix=[]

for i in range(R):
    row=[]
    for j in range(C):
        row.append(int(input("Enter Mat[%d][%d]: "%(i,j))))
    matrix.append(row)

print(matrix)
mat=np.array(matrix)

print(mat)
aat=np.dot(mat, mat.T)
ata=np.dot(mat.T, mat)
print(aat)
print(ata)
eval,evect=np.linalg.eig(aat)
sort_index = np.argsort(eval)
eigata=np.linalg.eig(ata)
print(eigata)
diag=[]
for i in range(len(eval)):
    row=[]
    for j in range(len(eval)):
        if i==j :
            row.append(math.sqrt(eval[sort_index[i]]))
        else:
            row.append(0)
    diag.append(row)
u=[]
for i in range(len(eval)):
    u.append(evect[:,sort_index[i]])
u=np.array(u).T
eval,evect=np.linalg.eig(ata)
sort_index = np.argsort(eval)
v=[]
for i in range(len(eval)):
    v.append(evect[:,sort_index[i]])
v=np.array(v)
print("Now are the answers\n\n\n")
print("U")
print(u)
print("\ndiag")
print(diag)
print("\nV")
print(v)
print("\nMultiplication")
print(np.dot(np.dot(u,diag),v))

print("\n\nNow comes the svd")
Uvec,Sigma,Vvec=np.linalg.svd(mat)
print("U")
print(Uvec)
print("\ndiag")
print(Sigma)
print("\nV")
print(Vvec)
print("\nMultiplication")
diagonal=[]
for i in range(len(Sigma)):
    row=[]
    for j in range(len(Sigma)):
        if i==j :
            row.append(Sigma[i])
        else:
            row.append(0)
    diagonal.append(row)

print(np.dot(np.dot(Uvec,diagonal),Vvec))
