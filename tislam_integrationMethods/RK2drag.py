from vpython import *
#Web VPython 3.2

m= 4
b = float(input("Enter b:"))
raddydaddy = 35
vellypelly =40

init_pos = vector(-4,-3,0)
init_pos2 = vector(4,-3,-0)
init_pos3 = vector(-2,-3,0)
init_pos4 = vector(2,-3,0)
init_vel = vector(vellypelly * cos(radians(raddydaddy)), vellypelly*sin(radians(raddydaddy)),0)
g = vector(0,-9.81,0)

platform = box(pos = vector(40,-4.5,0), size = vec(100,1,10))

ball4 = sphere(pos = init_pos4,color = color.yellow, make_trail= True)
ball4.vel = init_vel

vvt = graph(title="v vs Time", xtitle="Time", ytitle="Height", fast = False)

rk2  = gcurve(graph = vvt, color = color.blue)
rk2x =  gcurve(graph = vvt, color = color.red)

dt = .1
t = 0

while ball4.pos.y >= -3:
    rate(1/dt)
    
    rk2.plot(t,ball4.vel.y)
    rk2x.plot(t,ball4.vel.x)
    aN = (( m* g) - (ball4.vel * b) )/m
    dV = aN * dt
    vNhalf = ball4.vel + dV* .5
    aNhalf = (( m* g) - (vNhalf * b) )/m
    
    ball4.vel += aNhalf * dt
    ball4.pos += vNhalf * dt
    
    t += dt