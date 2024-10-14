import numpy as np
import matplotlib.pyplot as plt

v=lambda r:4/3*np.pi*r**3

a=lambda r: r**2*np.pi*4

sv=lambda p,o: p-o

qe=lambda cd,r: v(r)*cd

def getVMag(v):
    return np.sqrt(v[0]**2+v[1]**2+v[2]**2)

def getUVec(v,m):
    return v/m

def inside(r,v):
    if r>=getVMag(v):
        return getVMag(v)
    else:
        return r

def getFieldMag(cd,r,m):
    eps=8.85*10**-12
    return qe(cd,r)/(eps*a(m))

def zeroCondition(v):
    return [True for i in v if i==0]

def elecField(o,cd,r,p):
    m=getVMag(sv(p,o))
    r=inside(r,sv(p,o))
    if len(zeroCondition(sv(p,o)))==3:
        return np.array([0,0,0])
    return getFieldMag(cd,r,m)*getUVec(m,sv(p,o))








    





