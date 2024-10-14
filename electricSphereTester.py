import unittest
import math
import numpy as np
from electricSphere import getVMag, getUVec, getFieldMag, elecField, inside, zeroCondition

class TestElectricFieldCalculations(unittest.TestCase):
    
    def test_out(self):
        """test_out tests whether or not the elecField function can successfully calculate
        the electric field outside a sphere at the origin"""

        #axis are defined
        x=np.array(np.linspace(5,10,11))
        y=x
        z=x

        #radial distance from origin is defined.
        r=np.array([np.sqrt(3*i**2) for i in x])

        #par contains the parameters for the origin of the sphere, charge density, and radius
        par={"origin":np.array([0,0,0]),"charge density":1,"radius":1}
    
        #calc1 is the electric field according to the elecField function
        calc1=[getVMag(elecField(par["origin"],par["charge density"], par["radius"],np.array([x[i],y[i],z[i]]))) for i in range(len(x))]

        #calc2 is the electric field according to a theoretical equation
        calc2=[4/3*np.pi*par["radius"]**3*par["charge density"]/(4*np.pi*r[i]*(8.85*10)**-12) for i in range(len(r))]

        assert all([True for i in range(len(calc1)) if calc1[i]==calc2[i]])==True
    
    def test_in(self):
        """test_out tests whether or not the elecField function can successfully calculate
        the electric field inside a sphere at the origin"""

        #axis are defined
        x=np.array(np.linspace(0,10,11))
        y=x
        z=x

        #radial distance from origin is defined.
        r=np.array([np.sqrt(3*i**2) for i in x])

        #par contains the parameters for the origin of the sphere, charge density, and radius
        par={"origin":np.array([0,0,0]),"charge density":1,"radius":100}
    
        #calc1 is the electric field according to the elecField function
        calc1=[getVMag(elecField(par["origin"],par["charge density"], par["radius"],np.array([x[i],y[i],z[i]]))) for i in range(len(x))]

        #calc2 is the electric field according to a theoretical equation
        calc2=[4/3*np.pi*r[i]**3*par["charge density"]/(4*np.pi*r[i]*(8.85*10)**-12) for i in range(len(r))]

        assert all([True for i in range(len(calc1)) if calc1[i]==calc2[i]])==True
    
    def test_behavior(self):
        """test_behavior tests whether or not the electric field matches expected behavior
        While inside the radius, the field should increase in magnitude as the point at which
        the field is measured approaches the boundary of the sphere and should decrease as
        the point at which the field is measured moves away from the boundary"""

        #par contains the parameters for the origin of the sphere, charge density, and radius
        par={"origin":np.array([0,0,0]),"charge density":1,"radius":5}

        #axis are defined
        x=np.linspace(0,10,100)
        y=x
        z=x

        #ef will contain a list of electric field vectors
        ef=[]

        #magE will contain a list of the magnitude of the electric field vectors
        magE=[]

        #magV will contain a list of the magnitude of the separation vectors between point p and the origin
        magV=[]


        for i in range(len(x)):
            ef.append(elecField(par["origin"],par["charge density"],par["radius"],np.array([x[i],y[i],z[i]])))
            magV.append(np.sqrt(x[i]**2+y[i]**2+z[i]**2))
            magE.append(np.sqrt(ef[i][0])**2+ef[i][1]**2+ef[i][2]**2)

        # for each magnitude of the electric field, if point p is inside the radius of the sphere, then the magnitude of the electric field 
        # must be increasing. If point p is outside the radius of the sphere, then the magnitude of the electric field must be decreasing
        for i in range(1,len(magE)):
        
            if magV[i]<=par["radius"]:
                
                assert magE[i]>magE[i-1]
            else:
                assert magE[i]<magE[i-1]
    
    def test_notInner(self):
        """test_notInner tests whether or not the inside function can accurately determine if point p is outside the radius
        of the sphere"""

        o=np.array([0,0,0])
        v=np.array([10,10,10])
        r=5
        assert inside(r,(v-o))==r
    
    def test_inner(self):
        """test_Inner tests whether or not the inside function can accurately determine if point p is within the radius
        of the sphere"""

        o=np.array([0,0,0])
        v=np.array([10,10,10])
        r=100
        assert inside(r,(v-o))==getVMag(v)

    def test_zero(self):
        """test_zero tests whether or not the elecField function accounts for the separation vector being zero"""
        o=np.array([0,0,0])
        v=o
        r=1
        cd=1
        for i in range(2):
            assert elecField(o,cd,r,v)[i]==0
    
    def test_zeroCondition(self):
        "test_zeroCondition tests whether or no zeroCondition is functioning correctly for possible vectors."

        v=([0,0,1])
        assert len(zeroCondition(v))==2
        v=([0,1,1])
        assert len(zeroCondition(v))==1
        v=([1,1,1])
        assert len(zeroCondition(v))==0
    

    
if __name__=="__main__":
    unittest.main()
    
    


