from vpython import *
#Web VPython 3.2

scene = canvas(width=600, height=600)

G = 6.67e-11

distys = []
possys= []

sun = sphere(pos = vector(0, 0, 0), radius = 12e9, texture = "https://i.imgur.com/XdRTvzj.jpeg", shininess = 0, emissive=True, make_trail = True);
earth = sphere(pos = vector(1.5e11, 0, 0), radius = 6.37e9, texture=textures.earth, make_trail = True);


start_pos = earth.pos
total_angle = 0
last_angle = 0



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

dunzo = True

t=0; dt=3600
maxy = 0
maxx = 0
while((earth.pos-sun.pos).mag>(earth.radius+sun.radius) and (dunzo)):
    rate(1000)
  
    earth.acc = gravity(sun,earth)/earth.mass
    sun.acc = gravity(earth,sun)/sun.mass
    
    earth.velocity = earth.velocity + earth.acc*dt
    sun.velocity = sun.velocity + sun.acc*dt
    yback = earth.pos.y
    xback = earth.pos.x
    earth.pos = earth.pos + earth.velocity*dt
    sun.pos = sun.pos + sun.velocity*dt
    

    r_now = earth.pos - sun.pos
    r_prev = vector(xback, yback, 0) - sun.pos

    delta_theta = diff_angle(r_now, r_prev)
    total_angle += delta_theta

    if total_angle >= 2 * pi:
        dunzo = False

    
    distys.append( abs(mag(earth.pos - sun.pos)))
    possys.append(earth.pos - sun.pos)
    
    
    
    t = t+dt
    
print(distys)

# Find perihelion and aphelion positions
min_dist = min(distys)
max_dist = max(distys)
peri_index = distys.index(min_dist)
aphe_index = distys.index(max_dist)
peri_pos = possys[peri_index]
aphe_pos = possys[aphe_index]

# Create perihelion vector (red)
peri_vec = peri_pos - sun.pos
arrow(pos=sun.pos, axis=0.5 * peri_vec, color=color.red, shaftwidth=5e9)
label(pos=sun.pos + 0.5 * peri_vec, text="Perihelion", height=2e9, box=False, color=color.red)

# Create aphelion vector (blue)
aphe_vec = aphe_pos - sun.pos
arrow(pos=sun.pos, axis=0.5 * aphe_vec, color=color.blue, shaftwidth=5e9)
label(pos=sun.pos + 0.5 * aphe_vec, text="Aphelion", height=2e9, box=False, color=color.blue)

# Calculate second focus (Focus) position
a = (min_dist + max_dist) / 2  # semi-major axis
c = abs(max_dist - min_dist) / 2  # focal distance
focus_pos = sun.pos - norm(peri_pos - aphe_pos) * c

# Add yellow sphere for second focus
sphere(pos=focus_pos, radius=5e9, color=color.yellow)
label(pos=focus_pos, text="Focus", height=2e9, box=False, color=color.yellow)

# Debug printouts
print("Perihelion:", min_dist, "at t =", peri_index*dt, "s")
print("Aphelion:", max_dist, "at t =", aphe_index*dt, "s")
print("Focus located at:", focus_pos)
