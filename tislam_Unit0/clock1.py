from vpython import *
#Web VPython 3.2

# 
scene.title = "This is your trusty dusty clocknThis is just a text input\n"
scene.append_to_title("Type whatever you need in the labeled text inputs")

# 
wound = False

# 
big_rad = 3.1
little_rad = 2.6
micro_rad = 2.8

# 
minute_hand = arrow(pos=vec(0, 0, 0.1), axis=vec(0, little_rad-0.2, 0.1), color=color.blue)
hour_hand = arrow(pos=vec(0, 0, -0.1), axis=vec(0, little_rad-0.5, -0.1), color=color.green)

# time var storage
current_hours = 0
current_minutes = 0

# minute setter
def change_minutes(tim):
    global current_minutes, current_hours
    current_minutes = tim.number % 60

    # 
    minute_angle = -current_minutes * (pi / 30) + pi / 2
    minute_hand.axis = vec(little_rad * cos(minute_angle), little_rad * sin(minute_angle), 0.1)

    # 
    hour_angle = -((current_hours % 12) * (pi / 6) + current_minutes * (pi / 360)) + pi / 2
    hour_hand.axis = vec(little_rad * cos(hour_angle), little_rad * sin(hour_angle), -0.1)

# hour setter
def change_hours(hrs):
    global current_hours
    current_hours = hrs.number % 12

    # hour setter for func
    hour_angle = -current_hours * (pi / 6) + pi / 2
    hour_hand.axis = vec(little_rad * cos(hour_angle), little_rad * sin(hour_angle), -0.1)

# 
scene.append_to_caption('Input your desired hours and then your desired minutes\n<span style="color:green">Hours</span>    ')
hours = winput(bind=change_hours, type='numeric')
scene.append_to_caption('            (Numbers out of range will wrap around)\n<span style="color:blue">Minutes</span> ')
minutes = winput(bind=change_minutes, type='numeric')
scene.append_to_caption('\n')

# 
for i in range(12):
    outer_x = big_rad * cos(pi * i / 6)
    outer_y = big_rad * sin(pi * i / 6)
    if i % 3 == 0:
        inner_x = little_rad * cos(pi * i / 6)
        inner_y = little_rad * sin(pi * i / 6)
    else:
        inner_x = micro_rad * cos(pi * i / 6)
        inner_y = micro_rad * sin(pi * i / 6)
    curve(pos=[vec(outer_x, outer_y, 0), vec(inner_x, inner_y, 0)], radius=0.05, color=color.yellow)

# 
def setRun(b):
    global wound
    wound = not wound
    if wound:
        b.text = "Click to pause."
    else:
        b.text = "Click to run."

# 
button(bind=setRun, text="Click to wind the clock.")

# 
t = 0
dt = 0.05

# 
while True:
    rate(10)
    if wound:
        t += dt
        current_minutes += dt

        # time var track
        if current_minutes >= 60:
            current_minutes = 0
            current_hours = (current_hours + 1) % 12

        # minute pos set
        minute_angle = -current_minutes * (pi / 30) + pi / 2
        minute_hand.axis = vec(little_rad * cos(minute_angle), little_rad * sin(minute_angle), 0.1)

        # hour pos set
        hour_angle = -((current_hours % 12) * (pi / 6) + current_minutes * (pi / 360)) + pi / 2
        hour_hand.axis = vec(little_rad * cos(hour_angle), little_rad * sin(hour_angle), -0.1)
