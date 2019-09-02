# import numpy
import numpy as np

A=np.random.randint(0,40,10);

print(A)

def exchange(A, i, j):
    x=A[i]
    A[i]=A[j]
    A[j]=x

def partition(A, start, end):
    x=A[end]
    i=start-1
    for j in range(start,end-1):
        if A[j] < x:
            i=i+1
            # exchange(A,i,j)
    exchange(A,i+1,end)
    return i+1

def quicksort(A, start, end):
    print("\r\nStart: "+str(start)+"\tEnd:"+str(end))
    if start < end :
        pivot=partition(A,start,end)
        print("\r\n"+str(pivot)+":\t"+str(A[pivot]))
        print(A)
        A=quicksort(A, start, pivot-1)
        A=quicksort(A,pivot+1,end)
    return A

A=quicksort(A,0,len(A)-1)

print(A)




