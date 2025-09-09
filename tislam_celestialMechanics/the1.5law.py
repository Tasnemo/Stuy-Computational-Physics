from vpython import *
#Web VPython 3.2

scene = canvas(width=600, height=600)

G = 6.67e-11
planets =[]
sun = sphere(pos = vector(0, 0, 0), radius = 12e9, texture = "https://i.imgur.com/XdRTvzj.jpeg", shininess = 0, emissive=True, make_trail = True);
earth = sphere(name = "Earth",pos = vector(149.6e9, 0, 0), init_pos = vector(1.5e11, 0, 0), radius = 6.37e9, prev_pos = vector(0,0,0), texture=textures.earth, make_trail = True, retain = 30, angle = 0, orbitF = False, smaF = False, sma = 0, orbit = 0, period = 0);
venus = sphere(name = "Venus",pos = vector(108.2e9,0,0), init_pos = vector(.723 * earth.pos.x,0,0), prev_pos = vector(0,0,0),radius = earth.radius * 0.9499293674, texture = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Solarsystemscope_texture_8k_venus_surface.jpg/2560px-Solarsystemscope_texture_8k_venus_surface.jpg", make_trail = True, retain = 30, angle = 0, orbitF = False, smaF = False, orbit = 0, sma = 0, period = 0 )
mars = sphere(name = "Mars", pos = vector(228.0e9,0,0), init_pos = vector(1.5 * earth.pos.x,0,0),radius = earth.radius * .8, texture = "https://upload.wikimedia.org/wikipedia/commons/7/70/Solarsystemscope_texture_8k_mars.jpg", make_trail = True, retain = 30, angle = 0, orbitF = False, smaF = False, orbit = 0, sma = 0, period = 0);


# Please note that I made the radii of the earth and the Sun much too large, just so they're more visible. 
# All other quantities are realistic.

sun.mass = 1.9891e30
earth.mass = 5.97e24
mars.mass = earth.mass * .107
venus.mass = earth.mass * .815

sun.velocity = vector(0,0,0)
earth.velocity = vector(0,29.8e3,0)
mars.velocity = vector(0,24.1e3,0)
venus.velocity = vector(0,35e3,0)

sun.acc = vector(0,0,0)
earth.acc = vector(0,0,0)
mars.acc = vector(0,0,0)
venus.acc = vector(0,0,0)

planets.append(earth)
planets.append(mars)
planets.append(venus)


def gravity(star, satellite):
    dist = star.pos - satellite.pos
    
    F = G * star.mass * satellite.mass / mag(dist) ** 2
    return F * hat(dist)

def angGrab(planet):
    delta_theta = diff_angle(planet.pos - sun.pos, planet.prev_pos - sun.pos)
    planet.angle += delta_theta
    


def grav(satty):
    global sun
    
    sun.acc = gravity(satty,sun)/sun.mass
    satty.acc = gravity(sun,satty)/satty.mass
    
    satty.velocity = satty.velocity + satty.acc * dt
    sun.velocity = sun.velocity + sun.acc *dt
    
    satty.prev_pos = satty.pos
    satty.pos = satty.pos + satty.velocity *dt
    sun.pos = sun.pos + sun.velocity*dt
    



        
t=0; dt=3600
    
while(!mars.orbitF):
    rate(1000)
  
    
    for plan in planets:
        grav(plan)
        angGrab(plan)
   
        if(not plan.orbitF and plan.angle >= 2 * pi):
            print(plan.name + " period: " + str(t/3600/24))
            plan.periodo = t/3600/24
            plan.orbitF = True

        if( not plan.smaF and plan.angle >= pi):
            print(plan.name + " Semi Major Axis: " )
            print(mag(plan.pos - sun.pos) + mag(plan.init_pos - sun.pos))
            plan.smaF = True
            plan.sma = mag(plan.pos - sun.pos) + mag(plan.init_pos - sun.pos)
            
        
    t = t+dt

comparison = graph( title = "a^3 va t^2", xtitle = "semi major axis(km)", ytitle = "orbital period(days)")

planetsP = gdots(graph = comparison, color = color.red)
    

Xvals = []
Yvals = []

for planny in planets:
    planetsP.plot(planny.sma ** 3, planny.periodo ** 2)
    Xvals.append(planny.sma ** 3)
    Yvals.append(planny.periodo ** 2)


fitty = gcurve(graph = comparison, color = color.black)
numerator = 0
denominator = 0
for i in range(len(Xvals)):
    numerator += Xvals[i] * Yvals[i]
    denominator += Xvals[i] ** 2

m = numerator / denominator
print("Best-fit slope (T^2 / a^3): " + str(m))



for p in range(0, max(Xvals) * 1.1, max(Xvals)/20):
    fitty.plot(p,p*m)

for _ in planets:
    print(_.name)
    print("   Semi Major Axis:" + str(_.sma) + "(km)")
    print("   Period of Orbit:" + str(_.periodo) + "(days)")