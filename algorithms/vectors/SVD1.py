import numpy as np

def diagonal(array, row, column):
    Diag=[]
    for i in range(row):
        for j in range(column):
            if i==j:
                Diag[i][j]=array[i]
            else:
                Diag[i][j]=0
    return Diag

A=np.random.randint(1,4,size=[4,5])
print(A)

AAT=np.matmul(A,A.T)

print(AAT)

ATA=np.matmul(A.T,A)

print(ATA)
evalues,evectors=np.linalg.eig(AAT)


index=np.argsort(evalues)
print(index[::-1])
print(index)
S=evalues[index[::-1]]

U=evectors[index[::-1]].T
evalues,evectors=np.linalg.eig(ATA)

index=np.argsort(evalues)
S1=evalues[index[::-1]]
V=evectors[index[::-1]]

print(U)
print(np.sqrt(S))
print(np.sqrt(S1))
print(V)

US,SS,VS=np.linalg.svd(A)

print("tes")
print(US)
print(SS)
print(VS)

SSVD=diagonal(SS, 4,5)
print(np.matmul(np.matmul(US,SSVD),VS).astype(int))

