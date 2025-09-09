from vpython import *
#Web VPython 3.2

# titles
scene.title = "Wind Your Own Clock\nClick to wind the minute hand manually to set the time and click to let go :)"
scene.append_to_title("\nEach full revolution moves the hour hand")

# global states
wound = False
dragging = False

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
prev_angle = 0
full_rotations = 0  # Tracks full turns

# 
def change_minutes(new_minutes):
    global current_minutes, current_hours, full_rotations

    previous_minutes = current_minutes
    current_minutes = new_minutes % 60  

    if previous_minutes > 50 and current_minutes < 10:  
        current_hours = (current_hours + 1) % 12
        full_rotations += 1
    elif previous_minutes < 10 and current_minutes > 50:  
        current_hours = (current_hours - 1) % 12
        full_rotations -= 1

    # 
    minute_angle = -current_minutes * (pi / 30) + pi / 2
    minute_hand.axis = vec(little_rad * cos(minute_angle), little_rad * sin(minute_angle), 0.1)

    # 
    hour_angle = -((current_hours % 12) * (pi / 6) + (current_minutes / 60) * (pi / 6)) + pi / 2
    hour_hand.axis = vec(little_rad * cos(hour_angle), little_rad * sin(hour_angle), -0.1)

# 
def drag():
    global dragging, prev_angle
    dragging = not dragging
    if dragging:
        mouse_pos = scene.mouse.pos
        prev_angle = atan2(-mouse_pos.y, -mouse_pos.x) #calculate point to angle (did a reflection and translated to follow mouse)
scene.bind('click', drag)

# 
def update_minute_hand():
    global prev_angle, current_minutes

    if dragging:
        mouse_pos = scene.mouse.pos
        angle = atan2(-mouse_pos.x, -mouse_pos.y) 

        # Convert angle to minutes (each 6° = 1 min)
        new_minutes = round((180 + degrees(angle)) / 6) % 60

        # Update hand dynamically
        change_minutes(new_minutes)

        prev_angle = angle

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
dt = 0.025

# 
while True:
    rate(60)  
    
    update_minute_hand()  

    if wound:
        t += dt
        current_minutes += dt

        if current_minutes >= 60:
            current_minutes = 0
            current_hours = (current_hours + 1) % 12

        # minute pos set
        minute_angle = -current_minutes * (pi / 30) + pi / 2
        minute_hand.axis = vec(little_rad * cos(minute_angle), little_rad * sin(minute_angle), 0.1)

        # hour pos set
        hour_angle = -((current_hours % 12) * (pi / 6) + (current_minutes / 60) * (pi / 6)) + pi / 2
        hour_hand.axis = vec(little_rad * cos(hour_angle), little_rad * sin(hour_angle), -0.1)

