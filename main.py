# Buisness Tycoon Simulator (Text Edition)
import time
import math

#Establishing Variables
end_time = time.time()
start_time = time.time()
time_lapsed = end_time - start_time
cash = 0
p = 5
money = False
time_months = 0
months_left = 0
total_cash = 0

# Random Story Events
story1 = ("The FBI has shown up on your doorstep and demands $500 cash, you run and go radio silent")
story2 = ("Your Buinesses have been shamed by politicians; you may notice higher tax rates")
story3 = ("Your family comes home and you weren't able to get any work done")

#Functions
def Game():
      if p == 7:
        print ("To start your next month press SpaceBar")
        print ("Upgrades:")
        print ("(1). Next Buisness - $1000")
        print ("(2). Reduce Taxes - 1.2%")
        print ("(3). Restart Game")
        ()

def Transition():
    months_left = months - 1
    cash = 0
    total_cash = cash + 500
    print(total_cash)

  
#def Month_Timing():
  #months = int(input("Please Enter how long youd like to play for (In Months)"))
  #()

Game_Running = True

#Intro Stuffs / Gameplay   
while Game_Running == True:
  while p == 5:
    print ("Welcome to Buiness Tycoon Text Edition")
    print ("To play the game press (Spacebar then Enter)")
    prompt1 = input()
    if prompt1 == " ":
      p = 6
  while p == 6:
    print (" You will start with $0. Since you just purchsed your first buisness")
    print (" To start your first buisness press (Spacebar then Enter)")
    prompt2 = input()
    if prompt2 == " ":
      p = 7
      print ("Before you begin. Please select how long youd like to play for (1 Month is equal 10 or less seconds ")
      months = int(input("Please select your amount of months "))
    if months_left > 0:
        months2 = months
  while Game_Running == True:
        Game()
        input()
        start_time = time.time()
        Transition()
        input()
        end_time = time.time()
        time_lapsed = end_time - start_time











    






      

