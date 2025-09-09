from vpython import *
#Web VPython 3.2
#####    SET UP OBJECTS   ############

scene.userzoom = False
wall = box(pos=vector(-3, 0, 0), height=3, length=0.1, texture=textures.wood)
ball = sphere(pos=vector(-0.5, 0, 0), radius=0.3, color=color.yellow)
spring = helix(pos=wall.pos, axis=ball.pos - wall.pos, coils=19, radius=0.15, thickness = .02)

######  SET UP GRAPH  ######
graphPeriod = graph(title="Mass vs Period", xtitle="Mass (kg)", ytitle="Period (s)",
                    xmin=0, ymin=0, ymax=2)  # set the axes
periodCurve = gdots(graph=graphPeriod, color=color.blue)


#####    NON-NATIVE ATTRIBUTES   ######
ball.vel = vector(0, 0, 0)
ball.acc = vector(0, 0, 0)
ball.mass = 10
spring.k = 200

#####    TIME & STATE VARIABLES   ######
running = False
dt = 0.01
count = 0
cycles = 0
starter = False
periodPlotted = False
goingRight = True  
time = 0

##### BUTTON & SLIDER ######
def toggle_button():
    global running, count, cycles, starter, periodPlotted, goingRight

    running = not running

    if running:
        count = 0
        cycles = 0
        starter = False
        periodPlotted = False
        goingRight = True
        Changer.disabled = True
        countdownText.text = "Cycles till plot: 10"
    else:
        Changer.disabled = False

button(text="Start/Stop", bind=toggle_button)

wtext(text="Mass (kg): ")

dist = wtext(text = ball.mass)

def myaction(slider):
    global periodPlotted
    ball.mass = slider.value
    ball.radius = 0.2 + 0.0005 * ball.mass
    periodPlotted = False
    ball.pos.x = 2.00
    ball.vel = vector(0, 0, 0)

Changer = slider(bind=myaction, min=1, max=50, value=10)

#Countdown cause I'm impatient
countdownText = wtext(text=" Cycles till plot: 10")

#####   MAIN LOOP   ######
while True:
    rate(100)
    
    dist.text = ball.mass
    spring.axis = ball.pos - wall.pos
    if running:
        time +=dt
        ball.acc.x = (-spring.k / ball.mass) * ball.pos.x
        ball.vel.x += ball.acc.x * dt
        ball.pos.x += ball.vel.x * dt
  

        if starter:
            count += dt

        # Detect Peak
        if goingRight and ball.vel.x < 0:
            cycles += 1
            goingRight = False
            if not starter:
                starter = True

            # Countdown updater
            if cycles <= 10:
                countdownText.text = f"  Cycles till plot: {10 - cycles}"
               

        elif not goingRight and ball.vel.x > 0:
            goingRight = True

        # After 10 oscillations, plot period & update text
        if cycles == 10 and not periodPlotted:
            periodCurve.plot(ball.mass, count / 10)
            periodPlotted = True
            countdownText.text = "  Plotted!"
