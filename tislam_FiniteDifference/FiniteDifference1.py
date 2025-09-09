from vpython import *
#Web VPython 3.2
'''
Make canvas 1
Make canvas 2

define upper and lower
upper - lower = delta t
creae gcurves
for range from lower to upper by interval delta t:
    plot x(t) on gcurves on canvas 1
    plot x(t) - x(t- deltat) on gdots canvas 2
    

'''

def X(t):
    return 0.8*t**4-2.2*t**3+1.5*t+1

def Y(t):
    return 

gph1 = graph(title = "Position vs Time", ytitle="Position(m)", xtitle= "Time(s)", fast = False)
gph2 = graph(title = "Velocity vs Time", ytitle="Velocity(m/s)", xtitle= "Time(s)", fast = False)

upper = 2.5
lower = -1
timeStep= 8
deltaT = (2.5 + 1)/timeStep



distCurve = gcurve(graph = gph1, color = color.blue, label = "Position Curve")
veldots = gdots(graph=gph2, color = color.blue, label = "Velocity Curve", color= color.red)

part2_1 = gdots( graph=gph2,  color = color.black,  label = "Real difference")
part2_2 = gdots(graph= gph2, color = color.green, label = "backwards")
part2_3 = gdots(graph = gph2, color = color.blue, label = "midpoint") 



for t in range(lower, upper, deltaT):
    distCurve.plot(t, (.8*t**4-2.2*t**3 + 1.5*t+1))
    veldots.plot(t, (.8*t**4-2.2*t**3 + 1.5*t+1) - (.8*(t - deltaT)**4-2.2*(t - deltaT)**3 + 1.5*(t- deltaT)+1))
    part2_1.plot(t, (3.2*t**3-6.6*t**2+1.5))
    part2_2.plot(t, ((X(t) - X(t-deltaT))/ deltaT))
    part2_3.plot(t, ((X(t+ deltaT)-X(t-deltaT))/(deltaT*2)))

