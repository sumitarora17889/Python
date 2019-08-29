import numpy as np
A=np.random.randint(1,100,size=[4,5])
print(A)

AAT=np.matmul(A,A.T)

print(AAT)

ATA=np.matmul(A.T,A)

print(ATA)
evalues,evectors=np.linalg.eig(AAT)

print(evalues)

print(len(A))
print(evectors)
