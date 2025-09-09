from vpython import *
#Web VPython 3.2
N =100
lengtho = 4
maxT = 50
minT = 20
cylItems = []
dx = lengtho / N


def coloring(item):
    item.color = vec((item.t -minT)/(maxT -minT),0,1- (item.t -20)/(50 -20))
    
def newTemp(itemI):
    global cylItems
    
    
    
    
for i in range(N):
    cylitem = cylinder(t = 20, pos = vec(-2 + dx * i,0,0), length = dx, radius = .2 )
    coloring(cylitem)
    cylItems.append(cylitem)

dtim = 500
while True:
    rate(1/dtim)
    
    for step in range(0,N):
        
        coloring(cyl)