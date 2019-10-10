import numpy as np

R=int(input("Enter rows in matrix: "))
A=np.random.randint(1,500,size=[R,R])
print(A)
# 1 2 4
# 3 8 14
# 2 6 13
# A=[[1,2,4],[3,8,14],[2,6,13]]

# U00       U01                 U02
# L10U00    L10U01 + U11        L10U02 + U12
# L20U00    L20U01 + L21U11     L20U02 + L21U12 + U22

L=[]

L=np.zeros(shape=(R,R))
U=np.zeros(shape=(R,R))

for i in range(R):
    for j in range(i,R):
        L[j][i]=A[j][i]
        U[i][j]=A[i][j]
        for k in range(0,i):
            U[i][j]=U[i][j]-(L[i][k]*U[k][j])
            L[j][i]=L[j][i]-(L[j][k]*U[k][i])
        L[j][i]=L[j][i]/U[i][i]
print("========L========\r\n")
print(L)
print("========L========\r\n")
print("========U========\r\n")
print(U)
print("========U========\r\n")

aat=np.dot(L, U)

print("========U========\r\n")
print(aat)
print("========U========\r\n")



