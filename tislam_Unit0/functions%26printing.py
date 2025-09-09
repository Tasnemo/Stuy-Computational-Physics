from vpython import *
#Web VPython 3.2

x = box( pos = vec(1,1,1), color = color.red)

print("The volume is ", volume(x))


def volume(shape):
    return shape.length*shape.width*shape.height
'''
#Function format#
def functionName(vars):
    plz do stuff
    return eject


Calling the function 
functionName(vars)
'''
