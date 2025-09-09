from vpython import *
#Web VPython 3.2

def logistic(X,r):
    return r*X*(1-X)

seed = float(input(prompt= "starting x:"))
r = float(input(prompt= "growth rate:"))
N = int(input(prompt= "Amount of interations:"))

X = []
X[0] = seed

popit = graph(title= "pop fraction vs iterate number", xtitle = "iterate", ytitle = "population fraction", fast = False)

Curvy = gcurve(graph = popit)
Dotty = gdots(graph = popit)

Curvy.plot(0,X[0])
Dotty.plot(0,X[0])

for i in range(1, N +1):
    X[i] = logistic(X[i-1], r)
    Curvy.plot(i,X[i])
    Dotty.plot(i,X[i])