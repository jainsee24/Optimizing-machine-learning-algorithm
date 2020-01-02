# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 20:13:09 2019

@author: sj
"""
e=0.000001
def f(x1,x2):
    return 100*(x2-x1**2)**2+(1-x1)**2
def delf(x1,x2):
    return -400*(x2-x1**2)*x1-2*(1-x1),200*(x2-x1**2)
def findalpha(d1,d2,a1,b1):
    def fi(al):
        return 100*(-al*d2+b1-(-al*d1+a1)**2)**2+(1-a1+al*d1)**2
    a=-10000
    c=10000
    b=(a+c)/2
    x0=10**9
    while 1:
        fa=fi(a)
        fb=fi(b)
        fc=fi(c)
        xbar=((b**2-c**2)*fa+(c**2-a**2)*fb+(a**2-b**2)*fc)/(2*((b-c)*fa+(c-a)*fb+(a-b)*fc))
        if abs(xbar-x0)<e:
            break
        if xbar<b and xbar>a:
            if fi(xbar)<=fb:
                c=b
                b=xbar
            else:
                a=xbar
        if xbar>b and xbar<c:
            if fi(xbar)<=fb:
                a=b
                b=xbar
            else:
                c=xbar
        x0=xbar
    print(x0)
    return x0
a0=-2
b0=1
t=10
while t:
    t-=1
    dela,delb=delf(a0,b0)
    alpha=findalpha(dela,delb,a0,b0)
    anew=a0-alpha*dela
    bnew=b0-alpha*delb
    if abs(a0-anew)<e and abs(b0-bnew)<e:
        break
    a0=anew
    b0=bnew
    print(a0,b0,alpha)
