from vpython import *
#Web VPython 3.2


scene.camera.pos = vector(0, 6, 20)
scene.camera.axis = vector(0, -3, -15)

# T
cone(pos=vector(-8, 5, 0), axis=vector(0, -2, 0), radius=.5, length = 3, color=color.red)
cone(pos=vector(-9, 5, 0), axis=vector(2, 0, 0), radius=1,length = 3, color=color.red)

# A
cylinder(pos=vector(-5.3, 3, 0), axis=vector(0.5, 2.5, 0), radius=0.2, color=color.green)
cylinder(pos=vector(-4.7, 3, 0), axis=vector(-0.5, 2.5, 0), radius=0.2, color=color.green)
box(pos=vector(-5, 3.8, 0), size=vector(1.2, 0.2, 1.2), color=color.white)

# S
ring(pos=vector(-2, 5, 0), axis=vector(0, 0, 1), radius=1, thickness=0.3, color=color.blue)
sphere(pos=vector(-2.5, 5.3, 0), radius=0.4, color=color.black)
sphere(pos=vector(-1.5, 4.7, 0), radius=0.4, color=color.black)
ring(pos=vector(-2, 3.5, 0), axis=vector(0, 0, 1), radius=1, thickness=0.3, color=color.blue)
sphere(pos=vector(-2.5, 3.8, 0), radius=0.4, color=color.black)
sphere(pos=vector(-1.5, 3.2, 0), radius=0.4, color=color.black)

# N
cylinder(pos=vector(1, 3, 0), axis=vector(0, 3, 0), radius=0.4, color=color.magenta)
cylinder(pos=vector(2, 3, 0), axis=vector(0, 3, 0), radius=0.4, color=color.magenta)
cylinder(pos=vector(1, 3, 0), axis=vector(1, 3, 0), radius=0.3, color=color.orange)

# I
cone(pos=vector(4, 3, 0), axis=vector(0, 2, 0), radius=0.5, color=color.yellow)
sphere(pos=vector(4, 5, 0), radius=0.3, color=color.white)

# M
helix(pos=vector(6.5, 3, 0), axis=vector(0, 3, 0), radius=0.5, coils=6, thickness = .2, color=color.cyan)
helix(pos=vector(8.5, 3, 0), axis=vector(0, 3, 0), radius=0.5, coils=6, thickness = .2, color=color.cyan)
cylinder(pos=vector(6.5, 6, 0), axis=vector(1, -1.5, 0), radius=0.3, color=color.magenta)
cylinder(pos=vector(8.5, 6, 0), axis=vector(-1, -1.5, 0), radius=0.3, color=color.magenta)

