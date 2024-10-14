import numpy as np
import matplotlib.pyplot as plt

v=lambda r:4/3*np.pi*r**3
"""v is the volume of the sphere"""

a=lambda r: r**2*np.pi*4
"""a is the surface area of a sphere with radius defined by r"""

sv=lambda p,o: p-o
"""sv is the separation vector between p and o"""

qe=lambda cd,r: v(r)*cd
"""qe is the charge enclosed by the sphere"""

def getVMag(v):
    """getVMag returns the magnitude of a 3D vector"""
    return np.sqrt(v[0]**2+v[1]**2+v[2]**2)

    
def getUVec(v,m):
    """getUVec returns the unit vector of vector v. m is the magnitude of that vector"""
    return v/m

def inside(r,v):
    """inside determines whether or not the vector v has greater magnitude r and returns either the magnitude of v or r"""
    if r>=getVMag(v):
        return getVMag(v) 
    else:
        return r

def getFieldMag(cd,r,m):
    """getFieldMag returns the magnitude of the electric field"""
    eps=8.85*10**-12
    return qe(cd,r)/(eps*a(m))

def zeroCondition(v):
    """zeroCondition returns a list with a number of elements defined by whether or not the elements of v are zero"""
    return [True for i in v if i==0]

def elecField(o,cd,r,p):
    """elecField returns a vector which defines the electric field of a sphere which has its center located at point o, 
    a charge density cd, and a radius r at point p."""

    m=getVMag(sv(p,o)) #m is the magnitude of the separation vector between p and o

    r=inside(r,sv(p,o)) #if point p is inside the sphere, the radius is reduced to the magnitude of the separation vector

    if len(zeroCondition(sv(p,o)))==3:#if the separation vector is zero, a 3-dimensional zero vector is returned.
        return np.array([0,0,0])
    
    return getFieldMag(cd,r,m)*getUVec(m,sv(p,o))

def getField(o,cd,r,p):
    """getField just prints out the result of elecField in an easily readable way."""
    e=elecField(o,cd,r,p)
    return "The electric Field is defined by the vector["+str(e[0])+"x,", str(e[1])+"y,",str(e[2])+"z] V/m"








    





