from vpython import *
#Web VPython 3.2

def logistic(X, r):
    return r * X * (1 - X)

seed1 = float(input(prompt="First starting x: "))
seed2 = float(input(prompt="Second starting x: "))
r = float(input(prompt="Growth rate: "))
N = int(input(prompt="Amount of iterations: "))

X1 = [seed1]
X2 = [seed2]
D = [abs(seed1 - seed2)]

popit = graph(title="SDIC: Population fraction vs iterate #", xtitle="iterate", ytitle="population fraction", fast=False)

Curve1 = gcurve(graph=popit, color=color.blue)
Dots1 = gdots(graph=popit, color=color.cyan)

Curve2 = gcurve(graph=popit, color=color.red)
Dots2 = gdots(graph=popit, color=color.orange)

Curve1.plot(0, X1[0])
Dots1.plot(0, X1[0])

Curve2.plot(0, X2[0])
Dots2.plot(0, X2[0])

for i in range(1, N + 1):
    X1.append(logistic(X1[i - 1], r))
    X2.append(logistic(X2[i - 1], r))
    D.append(abs(X1[i] - X2[i]))
    Curve1.plot(i, X1[i])
    Dots1.plot(i, X1[i])
    Curve2.plot(i, X2[i])
    Dots2.plot(i, X2[i])

diffGraph = graph(title="Separation vs Iterate #", xtitle="iterate", ytitle="separation", fast=False)
DiffCurve = gcurve(graph=diffGraph, color=color.green)
DiffDots = gdots(graph=diffGraph, color=color.yellow)

for i in range(0, N + 1):
    DiffCurve.plot(i, D[i])
    DiffDots.plot(i, D[i])
