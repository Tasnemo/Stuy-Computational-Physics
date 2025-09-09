from vpython import *
#Web VPython 3.2
N =100
lengtho = 4
maxT = 50
minT = 5
cylItems = []
dx = lengtho / N

dt = dx ** 2 /4
def coloring(item):
    item.color = vec((item.T -minT)/(maxT -minT),0,1- (item.T -20)/(50 -20))
    
def newTemp(itemI):
    global cylItems
    if itemI != 0 and itemI != N - 1:
        d2T = (cylItems[itemI+1].T + cylItems[itemI-1].T - 2 * cylItems[itemI].T) / dx**2
        cylItems[itemI].T += dt * d2T

    
    
    
for i in range(N):
    cylitem = cylinder(T = 20, pos = vec(-2 + dx * i,0,0), length = dx, radius = .2 )
    coloring(cylitem)
    cylItems.append(cylitem)

label1 = label(pos = cylItems[int(N/3)].pos, text = cylItems[int(N/3)].T, yoffset= 40, xoffset = -20)
label2 = label(pos = cylItems[int(2*N/3)].pos, text = cylItems[int(2 *N/3)].T, yoffset= 40, xoffset = 20)
while True:
    rate(1000)
    cylItems[0].T = 50
    cylItems[N-1].T = 5
    for step in range(0,N):
        newTemp(step)
        coloring(cylItems[step])
        label1.text = round(cylItems[int(N/3)].T,1)
        label2.text = round(cylItems[int(2 * N/3)].T,1)
        
        