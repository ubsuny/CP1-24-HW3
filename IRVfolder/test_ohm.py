import numpy as np

from IRVfolder.ohm import ohmscur, ohmsres, ohmsvol

def ohmscur():
    """ This test the ohmscur function """
    assert ohmscur(2,3)==1.5

def ohmsres():
    """ This test the ohmsres function """
    assert ohmsres(2,1)==2.0

def ohmsvol():
    """ This test the ohmsvol function """
    assert ohmsvol(3,1)==3.0