import numpy as np
from ohm import ohmscur, ohmsres, ohvol, batch_ohm
def ohmscur():
    """This tests the ohmscur function"""
    assert ohmscur(2,3)==1.5
def ohmsres():
    """This tests the ohmsres function"""
    assert ohmsres(2,1)==2.0
def ohvol():
    """This tests the ohmsvol function"""
    assert ohvol(3,1)==3.0
curlis=[1,2,3];reslis=[2,3,4];volist=[2.0,6.0,12.0]
from ohm import ohvol
def batch_ohm():
    """This tests the batch_ohmsl function curlist is the list of currents, reslis is the list of resistances, volist is the expected voltages"""
    assert batch_ohm(curlis,reslis,ohvol)==volist