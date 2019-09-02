import numpy as np
def diagonal(array, row, column):
    Diag=[]
    for i in range(row):
        row=[]
        for j in range(column):
            if i==j:
                row.append(array[i])
            else:
                row.append(0)
        Diag.append(row)
    return Diag

# A=np.random.randint(1,4,size=[4,5])
A=np.matrix([[2,4],[1,3],[0,0],[0,0]])
print("========A========\r\n")
print(A)
print("========A========\r\n")

AAT=np.matmul(A,A.T)
print("========AAT========\r\n")
print(AAT)
print("========AAT========\r\n")

ATA=np.matmul(A.T,A)
print("========ATA========\r\n")

print(ATA)
print("========ATA========\r\n")

evalues,evectors=np.linalg.eig(AAT)
print("========Evalues========\r\n")

print(evalues)

print("========Evalues========\r\n")

print("========evectors========\r\n")
print(evectors)
print("========evectors========\r\n")

index=np.argsort(evalues)
print("========Descending Sorting Index reverse========\r\n")
print(index[::-1])
print("========Descending Sorting Index reverse========\r\n")

# print("========Sorting Index========\r\n")
#
# print(index)
# print("========Sorting Index========\r\n")

S=evalues[index[::-1]]

U=evectors[index[::-1]]
evalues,evectors=np.linalg.eig(ATA)

index=np.argsort(evalues)
S1=evalues[index[::-1]]
V=evectors[index[::-1]]


print("========Eigens========\r\n")
print("========Evalues========\r\n")

print(evalues)

print("========Evalues========\r\n")

print("========evectors========\r\n")
print(evectors)
print("========evectors========\r\n")
print("========U========\r\n")

print(U)
print("========U========\r\n")
print("========S========\r\n")
S=np.sqrt(S)
print(S)
print("========S========\r\n")

print("========V========\r\n")

print(V)
print("========V========\r\n")
SSVD=diagonal(S,4,2)
print(np.matmul(np.matmul(U.T,SSVD),V))

US,SS,VS=np.linalg.svd(A)
print("========SVD Formula========\r\n")

print("========U SVD Formula========\r\n")

print(US)
print("========U SVD Formula========\r\n")
print("========Sigma SVD Formula========\r\n")
SSVD=diagonal(SS,4,2)
print(SS)
print("========Sigma SVD Formula========\r\n")
print("========V SVD Formula========\r\n")

print(VS)
print("========V SVD Formula========\r\n")

# SSVD=diagonal(SS, 4,5)
print(np.matmul(np.matmul(US,SSVD),VS))

