from vpython import *
#Web VPython 3.2


x = box(pos = vec(.5,0,0), size = vec(1,.1,.1), color = color.red)
y = box(pos = vec(0,.5,0), size = vec(.1,1,.1), color = color.blue)
z = box(pos = vec(0,0,.5), size = vec(.1,.1,1), color = color.green)

xpyr = pyramid(pos = vec(1,0,0), size = vec(.2,.2,.2), color = color.red)
ypyr = pyramid(pos = vec(0,1,0), size = vec(.2,.2,.2), color = color.blue)
ypyr.rotate(axis=vec(0, 0, 1), angle=pi / 2, origin=vec(0,1, 0))
zpyr = pyramid(pos = vec(0,0,1), size = vec(.2,.2,.2), color = color.green)
zpyr.rotate(axis=vec(0, 1, 0), angle=(3 *pi) / 2, origin=vec(0,0, 1))


axes = compound([xpyr, ypyr, zpyr,x,y,z])

axes.size.x = 1