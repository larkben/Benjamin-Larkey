# Welcome to a Risk of Rain 2 Tracker

from Tkinter import *
import math
import time

main_screen = Tk()

#Functions
def PrintStats():
    print "Hello"

Screen = Frame(main_screen, width = 500, height = 500)
Top_Screen = Frame(Screen)
Bottom_Screen = Frame(Screen)
Left_Screen = Frame(Screen)
Right_Screen = Frame(Screen)

Title = Label(Top_Screen, text = "Welcome to Risk of Rain 2 Tracker", fg = "BLUE")

# Heroes
Commando_Button = Button(Left_Screen, text = "Commando", fg = "RED", )
Huntress_Button = Button(Left_Screen, text = "Huntress", fg = "RED", )
MulT_Button = Button(Left_Screen, text = "Mul-T", fg = "RED" )
Engineer_Button = Button(Left_Screen, text = "Engineer", fg = "RED", )
Artificer_Button = Button(Left_Screen, text = "Artificer", fg = "RED", )
Mercenary_Button = Button(Left_Screen, text = "Mercenary", fg = "RED", )
REX = Button(Left_Screen, text = "REX", fg = "RED", )
Loader_Button = Button(Left_Screen, text = "Loader", fg = "RED", )
Acrid_Button = Button(Left_Screen, text = "Acrid", fg = "RED", )

# Hero Text
Health = Label(Right_Screen, text = "Health: " , fg = "GREEN")
Attack = Label(Right_Screen, text = "Attack: " , fg = "GREEN")
SP_Attack = Label(Right_Screen, text = "SP. Attack: " , fg = "GREEN")
SP_Defense = Label(Right_Screen, text = "SP. Deffense: " , fg = "GREEN")
Speed = Label(Right_Screen, text = "Speed: " , fg = "GREEN")

# Widgets
Title.pack()
Commando_Button.pack()
Huntress_Button.pack()
MulT_Button.pack()
Engineer_Button.pack()
Artificer_Button.pack()
Mercenary_Button.pack()
REX.pack()
Loader_Button.pack()
Acrid_Button.pack()
Health.pack()
Attack.pack()
SP_Attack.pack()
SP_Defense.pack()
Speed.pack()

# Screens
Screen.pack()
Top_Screen.pack(side = TOP)
Bottom_Screen.pack(side = BOTTOM)
Left_Screen.pack(side = LEFT)
Right_Screen.pack(side = RIGHT)

main_screen.mainloop()
