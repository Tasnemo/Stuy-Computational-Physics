from vpython import *
#Web VPython 3.2

cubes = []
    
for x in range(2):
    for y in range(2):
        for z in range(2):
          cubes.append(box( pos = vector(x,y,z), size = vector(.3,.3,.3)))
          
for i in cubes:
    i.color = i.pos
    
    
t = 0
while True:
    rate(20)
    # time dependent instead of recursive
    t += 0.1
    i = 0  
    for cube in cubes:
        cube.color = vector(abs(sin(t + i)), abs(cos(t + i)), abs(sin(t - i))) 
        i += 1