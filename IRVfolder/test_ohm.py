"""
test_ohm.py

This is the test module for the functions defined in ohm.py
"""
from ohm import ohmscur, ohmsres, ohvol, batch_ohm
def test_ohmscur():
    """This tests the ohmscur function"""
    assert ohmscur(2, 3)==1.5
def test_ohmsres():
    """This tests the ohmsres function"""
    assert ohmsres(2, 1)==2.0
def test_ohvol():
    """This tests the ohmsvol function"""
    assert ohvol(3, 1)==3.0
curlis=[1, 2, 3]
reslis=[2, 3, 4]
"""curlist is the list of currents, reslis is the list of resistances"""
volist=[2.0, 6.0, 12.0]
"""volist is the expected voltages"""
def test_batch_ohm():
    """This tests the batch_ohmsl function"""
    assert batch_ohm(curlis, reslis, ohvol)==volist
