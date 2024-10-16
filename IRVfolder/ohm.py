import numpy as np
def ohmscur(r, v):
    div = lambda x, y: x/y
    if int(r)==0:
        raise ZeroDivisionError("Your resistance cannot be zero when finding current, try again")
    else:
        print ("Your current is",div(v,r))
        return div(v,r)
def ohmsres(i, v):
    div = lambda x, y: x/y
    if int(i)==0:
        raise ZeroDivisionError("Curent cannot be zero when finding resistance, try again")
    else:
        print ("Your resistance is",div(v,i))
        return div(v,i)
def ohmsvol(i, r):
    mult = lambda x, y: x*y
    print ("Your voltage is",mult(i,r))
    return mult(i,r)

def batch_ohmscur(x1List,x2List,func):
    return [IRV(x1,x2) for x1,x2 in zip(x1List,x2List)]
