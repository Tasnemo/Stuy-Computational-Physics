from vpython import *
#Web VPython 3.2


Posgraph = graph(title="Position vs Time", xtitle="Time", ytitle="Position", 
xmax=2.5, width=600, ymax=1, ymin = -1.5, height=300, align='left')

Accelgraph = graph(title="Acceleration vs Time", xtitle="Time", ytitle="Acceleration", 
xmax=2.5, width=600, ymax=1, ymin = -1.5, height=300, align='left')

acceleration = gcurve(graph=Posgraph, color=color.black)
position = gcurce(graph = Accelgraph, color= color.blue)

upper = 25
lower = 0
dt = 25/1000

def X(t):
    return 3 + cos(t)
def XAccel(t):
    return (X(t+dt)-2*X(t)+X(t-dt))/(dt**2)

while True:
    