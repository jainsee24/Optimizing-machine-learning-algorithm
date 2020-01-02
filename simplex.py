import numpy as np 
from fractions import Fraction
A = np.array([[-2, 2, 1, -1, 0], [1, 4, -1, 0, -1]]) 
b = np.array([1, 1])		 
c = np.array([2, 9, 3, 0, 0])			 
Bi=[2,5]
Ni=[1,3,4]
At=A.T
print(At)

answer=[0]*5
t=2
while t:
    print("-------------")
    B=[]
    for i in Bi:
        B.append(At[i-1])
    B=np.array(B).T
    print(B)

    t-=1
    N=[]
    for i in Ni:
        N.append(At[i-1])
    N=np.array(N).T
    print(N)
    Cb=[]
    for i in Bi:
        Cb.append(c[i-1])
    Cb=(np.array(Cb))
    print(Cb)
    Cn=[]
    for i in Ni:
        Cn.append(c[i-1])
    Cn=(np.array(Cn))
    #print(Cn)
    Binv=np.linalg.inv(B)
    #print(Binv)
    xb=np.dot(Binv,b)
    #print(xb)
    lemda=np.dot(Binv.T,Cb)
    print(lemda)
    mu=np.subtract(Cn,np.dot(N.T,lemda))
    print(mu)
    q=-1
    for i in range(0,len(Ni)):
        if mu[i]<0:
            q=i
    if q==-1:
        o=0
        print("Hell,,Yes")
        for i in Bi:
            answer[i]=xb[o]
            o+=1
        break
    Aq=np.array(At[Ni[q]-1])
    print(Aq)
    d=np.dot(Binv,Aq)
    print(d)
    xq=100000
    for i in range(0,len(Bi)):
        if d[i]>0:
            xq1=np.float(xb[i]/d[i])
            if xq1<xq:
                xq=xq1
                xqi=Bi[i]
    print(xq,xqi)
    index1=Bi.index(xqi)
    index2=q
    print(index1,index2)
    Bi[index1],Ni[index2]=Ni[index2],Bi[index1]
    print(Bi)
    print(Ni)
print(answer)