import unittest
import math
import numpy as np
from electricSphere import getVMag, getUVec, getFieldMag, elecField, inside

class TestElectricFieldCalculations(unittest.TestCase):
    
    def test_behavior(self):
        
        par={"origin":np.array([0,0,0]),"charge density":1,"radius":5}
        x=np.linspace(.2,10,100)
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



if __name__=="__main__":
    unittest.main()
    
    


