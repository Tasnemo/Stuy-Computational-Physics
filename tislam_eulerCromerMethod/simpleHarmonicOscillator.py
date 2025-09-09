from vpython import *
#Web VPython 3.2

# Scene setup
scene.userzoom = False

# Create objects
wall = box(pos=vector(-3, 0, 0), height=3, length=0.1, texture=textures.wood)
ball = sphere(pos=vector(-1, 0, 0), radius=0.3, color=color.yellow)
spring = helix(pos=wall.pos, axis=ball.pos - wall.pos, coils=15, radius=0.2)

# Graph for Mass vs Period
graphPeriod = graph(title="Mass vs Period", xtitle="Mass (kg)", ytitle="Period (seconds)")
periodPlot = gdots(graph=graphPeriod, color=color.blue)

graph

# Initial properties
spring.k = 4000  # Spring constant (fixed for this version)

# Simulation variables
running = False
dt = 0.01
time = 0
max_positions = []  # To store times at peak positions
periodPlotted = False

# Set initial ball properties
ball.mass = 400
ball.vel = vector(0, 0, 0)
ball.acc = vector(0, 0, 0) 

# GUI Elements
def toggle_run():
    global running, time, max_positions, periodPlotted
    running = not running
    run_button.text = "Stop" if running else "Start"
    mass_slider.disabled = running
    if not running:
        if len(max_positions) >= 2:
            period = (max_positions[-1] - max_positions[-2]) * 2
            periodPlot.plot(ball.mass, period)
        max_positions = []
        periodPlotted = False
        time = 0

def change_mass(slider):
    global periodPlotted
    ball.mass = slider.value
    ball.radius = 0.1 + 0.0007 * ball.mass
    periodPlotted = False

run_button = button(text="Start", bind=toggle_run)

mass_slider = slider(min=100, max=500, value=400, step=10, bind=change_mass)
mass_label = wtext(text=f"Mass: {ball.mass:.1f} kg\n")

change_mass(mass_slider)

# Peak detection variables
last_vel = 0
peak_detected = False

# Main simulation loop
while True:
    rate(1 / dt)

    if running:
        ball.acc.x = (-spring.k / ball.mass) * (ball.pos.x - wall.pos.x)
        ball.vel.x += ball.acc.x * dt
        ball.pos.x += ball.vel.x * dt
        spring.axis = ball.pos - wall.pos

        time += dt

        # Detect peaks - when velocity changes sign (from positive to negative)
        if ball.vel.x * last_vel < 0 and last_vel > 0:
            max_positions.append(time)
            if len(max_positions) > 2:
                max_positions.pop(0)

        last_vel = ball.vel.x

