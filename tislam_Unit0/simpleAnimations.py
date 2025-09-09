from vpython import *
#Web VPython 3.2

#Create a simple animation of this ball moving to the right
scene.camera.pos = vector(25,0,60) 
ball = sphere( color = color.red)

#define velocity and time increment

ball.vel = vector(3,0,0)

dt = .01

while (ball.pos.x < 50):
    rate(400)
    ball.pos = ball.pos + ball.vel*dt

    
