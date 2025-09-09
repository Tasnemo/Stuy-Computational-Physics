from vpython import *
#Web VPython 3.2

gph1 = graph(title = "position vs time", ytitle="Position(m)", xtitle= "Time(s)")

loCurve = gcurve(graph = gph1, color = color.red, label = "Position Curve")
velCurve = gcurve(graph=gph1, color = color.blue, label = "Velocity Curve")

for t in range(1, 10, .5):
    loCurve.plot(t, 3*(t*t*t) - 2*(t*t))
    velCurve.plot(t, 9*(t*t) - 4*(t))