from vpython import *
#Web VPython 3.2

scene = canvas(width=600, height=600)

G = 6.67e-11

sun = sphere(pos = vector(0, 0, 0), radius = 12e9, texture = "https://i.imgur.com/XdRTvzj.jpeg", shininess = 0, emissive=True, make_trail = True);
earth = sphere(pos = vector(1.5e11, 0, 0), radius = 6.37e9, texture=textures.earth, make_trail = True, retain = 30);

# Please note that I made the radii of the earth and the Sun much too large, just so they're more visible. 
# All other quantities are realistic.

sun.mass = 1.9891e30
earth.mass = 5.97e24

sun.velocity = vector(0,0,0)
earth.velocity = vector(0,21000,0)

sun.acc = vector(0,0,0)
earth.acc = vector(0,0,0)

def gravity(star, satellite):
    dist = star.pos - satellite.pos
    
    F = G * star.mass * satellite.mass / mag(dist) ** 2
    return F * hat(dist)

def days(t):
    return t/86400
rad = curve()


def dA(satellite, star):
    rad = (satellite.pos - star.pos)
    return mag(cross(rad,satellite.velocity*dt)/2)
    #return .5 * rad * mag(sattelite.velocity * dt)

are1 = 0
are2 = 0
t=0; dt=3600

dadt = graph( title = "da vs dt", xtitle = "time", ytitle = "Da/Dt", xmin = 0, ymin = 0)
plotto = gcurve(graph = dadt, color = color.cyan)
while(days(t) < 200):
    rate(1000)
    
    if( days(t) < 20 and days(t) > 0):
        rad = curve(pos = [sun.pos,earth.pos], color = color.cyan)
        are1 += dA(earth,sun)
        
        
        
    elif(days(t) < 110 and days(t) > 90):
        rad = curve(pos = [sun.pos, earth.pos], color = color.orange)
        are2 += dA(earth,sun)
    else:
        rad.clear()
    earth.acc = gravity(sun,earth)/earth.mass
    sun.acc = gravity(earth,sun)/sun.mass
    
    earth.velocity = earth.velocity + earth.acc*dt
    sun.velocity = sun.velocity + sun.acc*dt
    
    earth.pos = earth.pos + earth.velocity*dt
    sun.pos = sun.pos + sun.velocity*dt
    plotto.plot(t, dA(earth,sun))
    
    
    
     
    t = t+dt


print(are1)
print(are2)