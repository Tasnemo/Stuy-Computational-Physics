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

    

t=0; dt=3600
    
while((earth.pos-sun.pos).mag>(earth.radius+sun.radius)):
    rate(1000)
  
    earth.acc = gravity(sun,earth)/earth.mass
    sun.acc = gravity(earth,sun)/sun.mass
    
    earth.velocity = earth.velocity + earth.acc*dt
    sun.velocity = sun.velocity + sun.acc*dt
    
    earth.pos = earth.pos + earth.velocity*dt
    sun.pos = sun.pos + sun.velocity*dt
     
    
    t = t+dt

