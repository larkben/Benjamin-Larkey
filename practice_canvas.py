from Tkinter import *

root = Tk()

#Drop Down Menu
OptionList = [
    10,
    20,
    30,
    40,
    50,
]
#Variables
x = 100
b = 5
z = 0
y = 0

#Functions
'''
def Attack():
    print "The Monster Roars"
    new_health = x - b
    set(new_health)   
'''
#Need WORK!!!!!
def OpenImage():
    x = open("slime_monster_py", mode)

#Frames
topFrame = Frame(root)
bottomFrame = Frame(root)
leftFrame = Frame(root)
rightFrame = Frame(root)

#Establishing Variables
button1 = Button(leftFrame, text = 'Attack', command = Attack)
button2 = Button(leftFrame, text = 'Defend')

text_health = Label(bottomFrame, text = 'Health:')

health_meter = Scale(bottomFrame,orient = HORIZONTAL, from_=0, to=100, bg = "red")
health_meter.set(x)

#Mouse Recognition
screen = Frame(root, width = 300, height = 300)
def MouseLeft(event):
    print ("Left Click")

def MouseMiddle(event):
    print ("Middle Click")

def MouseRight(event):
    print ("Right Click")

screen.bind("<Button-1>", MouseLeft)
screen.bind("<Button-2>", MouseMiddle)
screen.bind("<Button-3>", MouseRight)

#Image Junk
'''
image = "slime_monster_py.png"
load = open("slime.jpg")
render = PhotoImage(load)
'''
#Widget Packing
button1.pack()
button2.pack()
text_health.pack()
health_meter.pack()

#Frame Packing
topFrame.pack()
bottomFrame.pack(side = BOTTOM)
leftFrame.pack(side = LEFT)
rightFrame.pack(side = RIGHT)
screen.pack()



root.mainloop()