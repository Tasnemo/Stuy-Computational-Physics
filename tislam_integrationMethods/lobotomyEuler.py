from vpython import *
#Web VPython 3.2

init_pos = vector(-4,-3,0)
init_pos2 = vector(4,-3,-0)
init_pos3 = vector(0,-3,0)
init_vel = vector(0,30,0)
g = vector(0,-9.81,0)

platform = box(pos = vector(0,-4.5,0), size = vec(15,1,10))


ball = sphere(pos = init_pos, color= color.cyan, make_trail=True)
ball.vel = init_vel

ball2= sphere(pos = init_pos2, color= color.orange, make_trail=True)
ball2.vel = init_vel

ball3= sphere(pos = init_pos3,color = color.red, make_trail= True)
ball3.vel = init_vel

hvt = graph(title="Height vs Time", xtitle="Time", ytitle="Heigth")
regents = gcurve(graph = hvt, color = color.orange)
euler = gcurve(graph = hvt, color = color.cyan)
reverse_E =gcurve(graph = hvt, color = color.red)

dt = .04
t = 0
while t < 6:
    rate(1/dt)
    euler.plot(t, ball.pos.y)
    ball.vel += g * dt
    ball.pos += ball.vel * dt
    
    
   
    ball2.pos = init_vel * t + .5 * g * (t **2) + init_pos2
    regents.plot(t,ball2.pos.y)
    
    reverse_E.plot(t, ball.pos.y)
    ball3.pos += ball3.vel * dt
    ball3.vel += g * dt
    
    
    t += dt