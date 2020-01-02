# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 16:29:26 2019

@author: sj
"""
import numpy as np
import matplotlib.pyplot as plt
import random as r
x=[]
y=[]
cx=[]
cy=[]
n=int(input("Enter no. of coordinates"))
for i in range(0,n):
    x.append(r.randint(0,100))
    y.append(r.randint(0,100))
print(x,y)
plt.scatter(x, y,c='black')
plt.title('Scatter plot')
plt.xlabel('x')
plt.ylabel('y')

k=int(input("Enter value of k for k means clustering"))
for i in range(0,k):
    cx.append(r.randint(0,100))
    cy.append(r.randint(0,100))
print(cx)
print(cy)
def find(xc,yc,cx,cy):
    min=1000
    x=-1
    y=-1
    for i in range(0,k):
        if (cx[i]-xc)**2+(cy[i]-yc)**2<min:
            min=(cx[i]-xc)**2+(cy[i]-yc)**2
            x=cx[i]
            y=cy[i]
    return x,y
t=30

number_of_colors=k+1
color = ["#"+''.join([r.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]
xx='1'
while(t):
    t-=1
    pointallocation={}
    for i in range(0,n):
        xc=x[i]
        yc=y[i]
        cxc,cyc=find(xc,yc,cx,cy)
        if (cxc,cyc) not in pointallocation:
            pointallocation[(cxc,cyc)]=[(xc,yc)]
        else:
            pointallocation[(cxc,cyc)].append((xc,yc))
    
    for i in range(0,k):
        plt.scatter(cx[i],cy[i],c=color[-1])
        for j in pointallocation[(cx[i],cy[i])]:
            plt.scatter(j[0],j[1],c=color[i])
    cx=[]
    cy=[]
    for i in pointallocation:
        xavg=0
        yavg=0
        for j in range(0,len(pointallocation[i])):
            xavg+=pointallocation[i][j][0]
            yavg+=pointallocation[i][j][1]
        xavg/=len(pointallocation[i])
        yavg/=len(pointallocation[i])
        cx.append(xavg)
        cy.append(yavg)
    print(cx)
    print(cy)
    
    xx+='1'
    plt.savefig(xx+".png")