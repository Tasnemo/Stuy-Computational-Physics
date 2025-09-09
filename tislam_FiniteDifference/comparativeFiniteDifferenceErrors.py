from vpython import *
#Web VPython 3.2
def X(t):
    return 0.8*t**4 - 2.2*t**3 + 1.5*t + 1

def V_true(t):
    return 3.2*t**3 - 6.6*t**2 + 1.5

def V_central(t, dt):
    return (X(t + dt) - X(t - dt)) / (2 * dt)

def V_forward(t, dt):
    return (X(t + dt) - X(t)) / dt

def rmse(method, lower, upper, dt):
    rangeF = int((upper - lower) / dt)

    sum_squared_error = 0
    t = lower

    for _ in range(rangeF):
        if method == "central":
            approx = V_central(t, dt)
        elif method == "forward":
            approx = V_forward(t, dt)

        sum_squared_error += (V_true(t) - approx) ** 2
        t += dt  

    return (sum_squared_error / rangeF) ** 0.5  # Corrected denominator

gph1 = graph(title="RMSE: Central vs Forward Difference", xtitle="Step Size (∆t)", ytitle="RMSE")

RMSEg_central = gdots(graph=gph1, color=color.green, label="Central Difference RMSE")
RMSEg_forward = gdots(graph=gph1, color=color.red, label="Forward Difference RMSE")

lower = -1
upper = 2.5

dt = 0.001
while dt <= 0.05:
    error_central = rmse("central", lower, upper, dt)
    error_forward = rmse("forward", lower, upper, dt)

    RMSEg_central.plot(dt, error_central)
    RMSEg_forward.plot(dt, error_forward)

    dt += 0.002
