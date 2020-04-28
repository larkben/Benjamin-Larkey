#Boolean Project
import math
from random import *, randrange

print("Hello humanoid subject!")
name = input("Please enter your name")
print ("Welcome " + name)
print("Now it's great to meet you although I'd like one more thing.")
age = int(input("Please enter your age please"))

if age > 10:
    print ("You are a teenager")
else:
    print ("You are very young yet")

print ("How about we play a game " + name)

def user_roll_game():
    game_running = True
    while game_running == True:
        user1 = randrange(1,7,1)
        computer1 = randrange(1,7,1)
        print("You rolled a" , user1 , "I rolled a" , computer1)
        game_continue = input("Whould you like to play again")
        if game_continue == "no":
            game_running = False
        else:
            game_running = True
        
user_roll_game()

print("Thanks for playing!")

    
            







    
