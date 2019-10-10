import numpy as np

import math

e=[]
for a in range(50):
    box = np.zeros(64);
    for i in range(64):
        A = np.random.uniform(1, 64)
        box[math.trunc(A)]=1
    print(box)
    emptybx=64-sum(box)
    e.append(64/emptybx)
    print(sum(e)/len(e))
