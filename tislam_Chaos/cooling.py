from vpython import *
#Web VPython 3.2

# Define a function called cooling that takes temperature T as an argument
def cooling(T):
    return .2 * (20 - T)
# Return the rate of temperature change


# make a list of starting temperatures from -100 C to + 100 C in steps of 10 C
starting_temps = []
for x in range (-100,101, 10):
    starting_temps.append(x)

# define a time step deltat
dt = 3
# define a run time for the simulation tMax
tMax = 10
# make a graphing canvas to plot temperature vs time
canvy = graph(title = "Temp vs Time", xtitle = "temperature", ytitle = "time")
tempt = gcurve( graph = canvy, color = color.black)
# iterate through every item in your list

for x in starting_temps:
    tempt.plot(0, x)
    for t in range(dt,tMax, dt):
        x += cooling(x) * dt
        tempt.plot(t, x)
     # make a gcurve and plot the starting temperature
     # iterate from time deltat to tMax in steps of deltat
         # assign the temp to temp + cooling(temp) * deltat
         # plot the new temperature


# things to try playing with:
# increase and decrease deltat
# Change the cooling parameter from 0.2 to something higher or lower.
# Change the environmental temperature to something other than 20
# Do any of these change the end behavior? The short term behavior?



