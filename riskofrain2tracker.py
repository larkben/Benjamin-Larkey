# Welcome to a Risk of Rain 2 Tracker

from tkinter import *
import math
import time

main_screen = Tk()

#Variables
h1 = 0
hr1 = 0
d1 = 0
a1 = 0
var = DoubleVar

#Functions
def Commando():
    h1 = 110 + 32 * Level.get()
    hr1 = 0.6 + 0.12 * Level.get()
    d1 = 12 + 3 * Level.get()
    a1 = 0 + 2 * Level.get()
    Health.config(text = h1)
    Attack.config(text = d1)
    Health_Regen.config( text = hr1)
    Armor.config( text = a1)

    
# Frames
Screen = Frame(main_screen, width = 500, height = 500)
Top_Screen = Frame(Screen)
Bottom_Screen = Frame(Screen)
Left_Screen = Frame(Screen)
Right_Screen = Frame(Screen)
Very_Right = Frame(Right_Screen)

#Title
Title = Label(Top_Screen, text = "Welcome to Risk of Rain 2 Tracker", fg = "BLUE")

# Heroes
Commando = Button(Left_Screen, text = "Commando", fg = "RED", command = Commando)
Huntress = Button(Left_Screen, text = "Huntress", fg = "RED", )
MulT = Button(Left_Screen, text = "Mul-T", fg = "RED" )
Engineer = Button(Left_Screen, text = "Engineer", fg = "RED", )
Artificer = Button(Left_Screen, text = "Artificer", fg = "RED", )
Mercenary = Button(Left_Screen, text = "Mercenary", fg = "RED", )
Rex = Button(Left_Screen, text = "REX", fg = "RED", )
Loader = Button(Left_Screen, text = "Loader", fg = "RED", )
Acrid = Button(Left_Screen, text = "Acrid", fg = "RED", )

#Slider
Level = Scale(Bottom_Screen, fg = "RED", orient = HORIZONTAL, from_=0.0, to = 100, variable = var)


# Hero Variables
Health = Label(Very_Right, text = h1 , fg = "GREEN")
Attack = Label(Very_Right, text =  d1 , fg = "GREEN")
Health_Regen = Label(Very_Right, text = hr1 , fg = "GREEN")
Armor = Label(Very_Right, text = a1 , fg = "GREEN")

#Hero Labels
H = Label(Right_Screen, text = "Health:", fg = "GREEN")
At = Label(Right_Screen, text = "Attack:", fg = "GREEN")
Hr = Label(Right_Screen, text = "Health Regen:", fg = "GREEN")
A = Label(Right_Screen, text = "Armor:", fg = "GREEN")

# Widgets
H.pack()
At.pack()
Hr.pack()
A.pack()
Title.pack()
Commando.pack()
Huntress.pack()
MulT.pack()
Engineer.pack()
Artificer.pack()
Mercenary.pack()
Rex.pack()
Loader.pack()
Acrid.pack()
Health.pack()
Attack.pack()
Health_Regen.pack()
Armor.pack()
Level.pack()


# Screens
Screen.pack()
Top_Screen.pack(side = TOP)
Bottom_Screen.pack(side = BOTTOM)
Left_Screen.pack(side = LEFT)
Right_Screen.pack(side = RIGHT)
Very_Right.pack(side = RIGHT)

main_screen.mainloop()