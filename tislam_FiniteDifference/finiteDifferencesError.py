from vpython import *
#Web VPython 3.2

def X(t):
    return 0.8*t**4 - 2.2*t**3 + 1.5*t + 1

def V_true(t):
    return 3.2*t**3 - 6.6*t**2 + 1.5

def V_central(t, dt):
    return (X(t + dt) - X(t - dt)) / (2 * dt)

def rmse(lower, upper, dt):
    n = int((upper - lower) / dt)  
    sum_squared_error = 0
    t = lower

    for _ in range(n):
        sum_squared_error += (V_true(t) - V_central(t, dt)) ** 2
        t += dt  

    return (sum_squared_error / n) ** 0.5

gph1 = graph(title="", xtitle="Step Size (∆t)", ytitle="RMSE")

RMSEg = gdots(graph=gph1, color=color.green, label="Central Difference RMSE")

lower = -1
upper = 2.5

dt = 0.001
while dt <= 0.05:
    RMSEg.plot(dt, rmse(lower, upper, dt))
    dt += 0.002
