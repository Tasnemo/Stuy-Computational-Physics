from vpython import *
#Web VPython 3.2


#####    SET UP OBJECTS   ############

scene.userzoom = False
wall = box(pos=vector(-3, 0, 0), height = 3, length=0.1, texture=textures.wood)
ball = sphere(pos=vector(0,0,0), radius=0.3, color=color.yellow)
spring = helix(pos=wall.pos, axis=(ball.pos-wall.pos), coils=19, radius=0.2)

ballawalla = graph(title= 'Time by Position', xtitle = 'time', ytitle= 'position', align = 'right')
balla = gcurve(graph= ballawalla, color = color.red)
walla = gcurve(graph = ballawalla)

#####     ADDING NON-NATIVE ATTRIBUTES TO THE BALL AND SPRING   #######

ball.vel = vector(0,0,0)
ball.acc = vector(0,0,0)
ball.mass = 60      # I chose this at random

spring.k = 240             # I chose this at random

phase_space = graph(title='Position vs Velocity', xtitle='position', ytitle='velocity', align = 'right')

ps_curve = gcurve(graph=phase_space)

#####    SETTING UP A TIME FRAMEWORK  #########

dt = (1/100)
b = 240 * .7
spin_factor = 2 * .4
direction = None

t_i = 0
t_f = 0

total_time = 0

while True:
    global direction
    rate(1/dt)        
    total_time += dt
    # This runs the loop in pseudo-real time.
    # Find the current acceleration here
    # Update the velocity here
    wall.pos.x = cos(total_time*spin_factor) -3
    
    ball.acc = (-spring.k * (ball.pos - wall.pos) - ball.vel * b)/ ball.mass
    ball.vel = ball.vel + ball.acc * dt
    ball.pos = ball.pos + ball.vel * dt
    walla.plot(total_time, wall.pos.x)
    balla.plot(total_time, ball.pos.x)
    
   
    spring.pos = wall.pos
    spring.axis = ball.pos-wall.pos

    ps_curve.plot(ball.pos.x, ball.vel.x)

    recent_direction = direction
    direction = sign(ball.vel.x)
   
    if(recent_direction and recent_direction > direction):  
        t_i = total_time
