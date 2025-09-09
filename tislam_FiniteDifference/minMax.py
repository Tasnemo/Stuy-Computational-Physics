from vpython import *
#Web VPython 3.2

#####    SET UP A CANVAS AND OBJECTS   ############

c1 = canvas(width=600, height=300, align='left')
wall = box(pos=vector(-2, 0, 0), height = 3, length=0.1, texture=textures.wood)
base = box(pos=vector(0,-0.35,0), length=4, height=0.1)

ball = sphere(pos=vector(0,0,0), radius=0.3, color=color.yellow)
spring = helix(pos=wall.pos, axis=(ball.pos-wall.pos), coils=17, radius=0.2)
    
scene.userzoom = False

######  MAKE A POSITION FUNCTION     #########

def damping(t):
    return cos((7*t)-0.2)*exp(-t/2) - 0.2
            
            
#####    DEFINE A RUN TIME AND A TIME STEP #######            
            
Tmin = 0
Tmax = 2.5

numSteps = 1000
t = 0
dT = (Tmax - Tmin)/numSteps

#####  SET UP A GRAPHING CANVAS AND A GRAPHING OBJECT  ##########

Posgraph = graph(title="Position vs Time", xtitle="Time", ytitle="Position", 
xmax=2.5, width=600, ymax=1, ymin = -1.5, height=300, align='left')


gpos = gcurve(graph=Posgraph, color=color.magenta)
bottom = gdots(graph = Posgraph, color= color.blue)
top = gdots(graph = Posgraph, color = color.red)

def poop(x):
    sphere(pos=vec(x, -.35, 0), color = color.red, radius = .1)
#####  RUN THE ANIMATION AND THE GRAPH SIMULTANEOUSLY  ###########

while t<Tmax:
    rate(100)
    
    if (sign((damping(t+ dT)-damping(t-dT))/(dT*2)) > sign((damping(t)-damping(t-2*dT))/(dT*2))):
        bottom.plot(t,damping(t))
        poop(damping(t))
    if (sign((damping(t+ dT)-damping(t-dT))/(dT*2)) < sign((damping(t)-damping(t-2*dT))/(dT*2))):
        top.plot(t,damping(t))
        poop(damping(t))
    ball.pos.x = damping(t)
    spring.axis=ball.pos-wall.pos
    gpos.plot(t, damping(t))
    t += dT