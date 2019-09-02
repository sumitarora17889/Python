import numpy as np

size=np.int(input("Enter Size of the array: "))
array=np.random.randint(1,1000,size)
print(array)

for i in range(size):
    key=array[i]
    print(i)
    for j in range(i)[::-1]:
        if(array[j]>key):
            array[j+1]=array[j]
            if j==0:
                array[0]=key
        else:
            array[j + 1] = key
            break

print(array)


