import numpy as np

def IRV(i, r, v):
    div = lambda x, y: x/y
    mult = lambda x, y: x*y
    if type(i)==str:
        if int(r)==0:
            return print ("Your resistance cannot be zero when finding current, try again")
        else:
            print ("Your current is",div(v,r))
            return div(v,r)
    if type(r)==str:
        if int(i)==0:
            return print ("Curent cannot be zero when finding resistance, try again")
        else:
            print ("Your resistance is",div(v,i))
            return div(v,i)
    else:
        print ("Your voltage is",mult(i,r))
        return mult(i,r)


def testfunk(x, y):
    return x+y
