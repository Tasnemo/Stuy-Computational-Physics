from vpython import *
#Web VPython 3.2

'''
LISTS, FOR LOOPS, AND LOGIC

Things to know about lists:
    - A list is a type of data structure that allows you to store multiple items
    - How to create a list
    - How to append items to a list
    - How to perform list comprehensions

Things to know about for() loops:
    - When to use for() and when to use while()
    - How to use the range(start,stop,step) function
    
'''
'''
myList = []

for i in range(1,101,2):
    myList.append(i)

print(myList)


# make newList that is only multiples of 3 contained in myList
newList = []

for i in range(1,101,2):
    if i % 3 == 0:
        newList.append(i)
        
print(newList)
'''

objList = []
for i in range (0,10):
    item = sphere(pos=vector(-5 + i,0,0), radius = .5)
    item.color = vector(i/10, 1- i/10,i/10)
    objList.append(item)

#jiggle

t = 0
dt = 0.4

while True:
    rate(100)
    t += dt
    for i in range(objList.length):
        objList[i].pos.y = sin(t+i)

