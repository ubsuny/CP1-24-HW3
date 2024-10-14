import numpy as np
import matplotlib.pyplot as plt

v=lambda r:4/3*np.pi*r**3

a=lambda r: r**2*np.pi*4

sv=lambda p,o: p-o

def getQenc(cd,r):
    return v(r)*cd

def getVMag(v):
    return np.sqrt(v[0]**2+v[1]**2+v[2]**2)

def getUVec(v,m):
    return v/m

def getFieldMag(cd,r,m):
    eps=8.85*10**-12
    return v(r)*cd/(eps*a(m))

def elecField(o,cd,r,p):
    m=getVMag(sv(p,o))
    return getFieldMag(cd,r,m)*getUVec(m,sv(p,o))






    





