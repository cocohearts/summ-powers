import fractions
import math
import numpy as np
def com(a,b):
    d = 1
    for r in range(a-b+1,a+1):
        d = r * d
    return d/math.factorial(b)
def core(x):
#Start eval (k+1)^{n+1}-1
    if x == 0:
        return np.array([1,0])
    r=[]
    for m in range(1,x+1):
        r.append(com((x+1),m))
    r.append(0)
    r=np.array(r)
#Finish eval (k+1)^{n+1}-1
#For front-appending zeroes
    a=[]
    for r in range(x-1):
#a's zero "buildup"
        a.append(0)
    for k in range(x):
#actual frontending
        g=np.concatenate(a,core(k))
#yay!! final subtraction
        r=r-(com(x+1,k)*g)
#preparing a for the next iteratioin
        np.delete(a,0)
    return r
#Tests:
if com(3,2)==3 and com(5,3)==10 and com(16,5)==4368:
    print(1)
else:
    print("Combo failed")
print(core(3))
