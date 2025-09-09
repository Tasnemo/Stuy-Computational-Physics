from vpython import *
#Web VPython 3.2

'''
This is a program that simulates an analog clock.
We will modify this program to allow user input to:
 -- start and stop the clock
 -- set the initial time of the clock

Your first job is to read through the code and add a comment
after each hashtag saying what the next block or line of code does.
'''

# title printer
scene.title = "This is a clock.\nThis is a new line.\n"
scene.append_to_title("This is yet a third line of text.")

# Is the Clock going to run
wound = False

# length of the clock ticks
big_rad = 3.1
little_rad = 2.6
micro_rad = 2.8

# clock face setup
for i in range(12):
    outer_x = big_rad*cos(pi*i/6)
    outer_y = big_rad*sin(pi*i/6)
    if i%3 == 0:
        inner_x = little_rad*cos(pi*i/6)
        inner_y = little_rad*sin(pi*i/6)
    else:
        inner_x = micro_rad*cos(pi*i/6)
        inner_y = micro_rad*sin(pi*i/6)
    curve(pos=[vec(outer_x, outer_y, 0), vec(inner_x, inner_y, 0)], radius = 0.05, color=color.yellow)

# clock hand setup
minute_hand = arrow(pos=vec(0, 0, 0.1), axis=vec(0, little_rad-0.2, 0.1), color=color.blue)
hour_hand = arrow(pos=vec(0, 0, -0.1), axis=vec(0, little_rad-0.5, -0.1), color=color.green)

# time passed
t = 0
# speed of rotation
dt = 0.05 


button(bind=setRun, text = "click to wind")

def setRun(b):
    global wound
    wound = not wound
    b.text
    if wound:
        b.text = "click to unwind"
    else:
        b.text = "click to wind"

# spinloop for all cases
while True:
    rate(10)
    # hand shift mechanism
    if wound:
        # moves the hands
        minute_hand.rotate(axis=vec(0, 0, -1), angle=dt, origin=vec(0, 0, 0))
        hour_hand.rotate(axis=vec(0, 0, -1), angle=dt/12, origin=vec(0, 0, 0))
        # elapses time
        t += dt
    

        
       