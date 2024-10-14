import unittest
import math
import numpy as np
from electricSphere import getVMag, getUVec, getFieldMag, elecField, inside, zeroCondition

class TestElectricFieldCalculations(unittest.TestCase):
    
    def test_out(self):
        x=np.array(np.linspace(5,10,11))
        y=x
        z=x
        r=np.array([np.sqrt(3*i**2) for i in x])
        par={"origin":np.array([0,0,0]),"charge density":1,"radius":1}
    
        calc1=[getVMag(elecField(par["origin"],par["charge density"], par["radius"],np.array([x[i],y[i],z[i]]))) for i in range(len(x))]
        calc2=[4/3*np.pi*par["radius"]**3*par["charge density"]/(4*np.pi*r[i]*(8.85*10)**-12) for i in range(len(r))]
        assert all([True for i in range(len(calc1)) if calc1[i]==calc2[i]])==True
    
    def test_in(self):
        x=np.array(np.linspace(0,10,11))
        y=x
        z=x
        r=np.array([np.sqrt(3*i**2) for i in x])
        par={"origin":np.array([0,0,0]),"charge density":1,"radius":100}
    
        calc1=[getVMag(elecField(par["origin"],par["charge density"], par["radius"],np.array([x[i],y[i],z[i]]))) for i in range(len(x))]
        calc2=[4/3*np.pi*r[i]**3*par["charge density"]/(4*np.pi*r[i]*(8.85*10)**-12) for i in range(len(r))]
        assert all([True for i in range(len(calc1)) if calc1[i]==calc2[i]])==True
    
    def test_behavior(self):
        
        par={"origin":np.array([0,0,0]),"charge density":1,"radius":5}
        x=np.linspace(0,10,100)
        y=x
        z=x
        ef=[]
        magE=[]
        magV=[]
        for i in range(len(x)):
            ef.append(elecField(par["origin"],par["charge density"],par["radius"],np.array([x[i],y[i],z[i]])))
            magV.append(np.sqrt(x[i]**2+y[i]**2+z[i]**2))
            magE.append(np.sqrt(ef[i][0])**2+ef[i][1]**2+ef[i][2]**2)
        for i in range(1,len(magE)):
        
            if magV[i]<=par["radius"]:
                
                assert magE[i]>magE[i-1]
            else:
                assert magE[i]<magE[i-1]
    
    def test_notInner(self):
        o=np.array([0,0,0])
        v=np.array([10,10,10])
        r=5
        assert inside(r,(v-o))==r
    
    def test_inner(self):
        o=np.array([0,0,0])
        v=np.array([10,10,10])
        r=100
        assert inside(r,(v-o))==getVMag(v)

    def test_zero(self):
        o=np.array([0,0,0])
        v=o
        r=1
        cd=1
        for i in range(2):
            assert elecField(o,cd,r,v)[i]==0
    
    def test_zeroCondition(self):
        v=([0,0,1])
        assert len(zeroCondition(v))==2
        v=([0,1,1])
        assert len(zeroCondition(v))==1
        v=([1,1,1])
        assert len(zeroCondition(v))==0
    

    
if __name__=="__main__":
    unittest.main()
    
    


