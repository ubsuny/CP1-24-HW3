import numpy as np
def ohmscur(r,v):
    """This function finds current using ohms law"""
    div = lambda x,y: x/y
    if int(r)==0:
        raise ZeroDivisionError("Your resistance cannot be zero when finding current, try again")
    else:
        print ("Your current is",div(v,r))
        return div(v,r)
def ohmsres(i,v):
    """This function finds resistance using ohms law"""
    div = lambda x,y: x/y
    if int(i)==0:
        raise ZeroDivisionError("Curent cannot be zero when finding resistance, try again")
    else:
        print ("Your resistance is",div(v,i))
        return div(v,i)
def ohvol(i,r):
    """This function finds voltage using ohms law"""
    mult = lambda x,y: x*y
    print ("Your voltage is",mult(i,r))
    return mult(i,r)
def batch_ohm(x1list,x2list,func):
    """This function allows the use of lists from the previos functions and out puts a list of awnsers"""
    return [func(x1,x2) for x1,x2 in zip(x1list,x2list)]