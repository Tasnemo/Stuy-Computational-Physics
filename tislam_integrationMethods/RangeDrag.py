from vpython import *
#Web VPython 3.2

m= 1
raddydaddy = 35
vellypelly =40
init_pos4 = vector(2,-3,0)

g = vector(0,-9.81,0)

platform = box(pos = vector(40,-4.5,0), size = vec(1,1,10))


bmvdist= graph(title="b/m vs Optimal Angle", xtitle="b/m", ytitle="Optimal Angle")

proppy  = gdots(graph = bmvdist, color = color.blue)

dt = .1

for b in range(0,1,.01):
    furthydurthy = 0

    for angybangy in range(0,90,.1):
        dt = .1
        init_vel = vector(vellypelly * cos(radians(angybangy)), vellypelly*sin(radians(angybangy)),0)
        ball4 = sphere(pos =init_pos4,color = color.yellow,make_trail=True)
        ball4.vel = init_vel
        t = 0
        while ball4.pos.y >= -3:
            if(ball4.pos.y < (vellypelly * dt) & ball4.vel.y < 0):
                dt = .001
         #   rate(1/dt)
            platform.size.x = furthydurthy + 10
            platform.pos.x = furthydurthy/2

            aN = (( m* g) - (ball4.vel * b) )/m
            dV = aN * dt
            vNhalf = ball4.vel + dV* .5
            aNhalf = (( m* g) - (vNhalf * b) )/m
            
            ball4.vel += aNhalf * dt
            ball4.pos += vNhalf * dt
            
            if(ball4.pos.x > furthydurthy):
                furthydurthy = ball4.pos.x
                optangle = angybangy
    
            t += dt
    proppy.plot(b,optangle)