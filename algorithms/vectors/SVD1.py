import numpy as np
import math
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

A=np.random.randint(1,4,size=[4,5])
A=np.matrix([[2,4],[1,3],[0,0],[0,0]])
print("========A========\r\n")
print(A)
print("========A========\r\n")

AAT=np.matmul(A,A.T)
# print("========AAT========\r\n")
# print(AAT)
# print("========AAT========\r\n")

ATA=np.matmul(A.T,A)
# print("========ATA========\r\n")
#
# print(ATA)
# print("========ATA========\r\n")

evalues,evectors=np.linalg.eig(AAT)
# print("========Evalues========\r\n")
# print(evalues)
# print("\r\n")
sort_index=np.argsort(evalues,kind = 'stable')
sort_index=np.flip(sort_index)
Sigma=diagonal(np.sqrt(evalues[sort_index]),4,2)
# print(Sigma)


# print("========Evalues========\r\n")
# print("========evectors========\r\n")
U=evectors[sort_index]
# print(U)
# print("========evectors========\r\n")


evalues,evectors=np.linalg.eig(ATA)


# print("========Eigens========\r\n")
# print("========Evalues========\r\n")
# print(evalues)
sort_index=np.argsort(evalues,kind = 'stable')
sort_index=np.flip(sort_index)
V=evectors.T[sort_index]
# print(evalues[sort_index])
#
# print("========Evalues========\r\n")
#
# print("========evectors========\r\n")
# print(evectors)
# print(V)
# print("========evectors========\r\n")

print("========U========\r\n")
print(U)
# print(np.matmul(np.matmul(U,Sigma),V.T))
print("========U========\r\n")
print("========Sigma========\r\n")
print(Sigma)
# print(np.matmul(np.matmul(U,Sigma),V.T))
print("========Sigma========\r\n")
print("========V========\r\n")
print(V)
print(np.matmul(np.matmul(U,Sigma),V.T))
print("========V========\r\n")

US,SS,VS=np.linalg.svd(A)
print("========SVD Formula========\r\n")

print("========U SVD Formula========\r\n")

print(US)
print("========U SVD Formula========\r\n")
print("========Sigma SVD Formula========\r\n")
SSVD=diagonal(SS,4,2)
print(SSVD)
print("========Sigma SVD Formula========\r\n")
print("========V SVD Formula========\r\n")

print(VS.T)
print("========V SVD Formula========\r\n")

# SSVD=diagonal(SS, 4,5)
print(np.matmul(np.matmul(US,SSVD),VS.T))

