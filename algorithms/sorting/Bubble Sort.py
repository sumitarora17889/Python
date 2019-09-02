import numpy as np

size=np.int(input("Enter Size of the array: "))
array=np.random.randint(1,1000,size)
print(array)

def swap(a,i,j):
    key=a[i]
    a[i]=a[j]
    a[j]=key

for i in range(size):
    for j in range(size):
        if array[i]<array[j]:
            swap(array, i,j)
print(array)