# This program will function as a claculator for everything

from math import *

print ('Welcome to Calculator')
print ('Select a Function')
print ('1)Physics')
print ('2)Chemistry')
print ('3)Math')

 # options_start = ["physics", "chemistry", "math"]

choice_user = input("Select one of the Above ")


if choice_user == "physics":
    info_user = input("What do you want ") 
    if  info_user == "xf":
        num1 = input("Enter a Velocity ")
        num2 = input("Enter a Time ")
        num3 = input("Intial Distance ")
        result = float(num1) * float(num2) + int(num3)
        print(result)
    elif info_user == "v":
        num4 = input("Give me a Final Distance ")
        num5 = input("Give a time ")
        num6 = input("Give me an Intial Distance ")
        result2 = float(num4) / float(num5) + int(num6)
        print(result2)
    elif info_user == "t":
        num7 = input("Give me a Velocity ")
        num8 = input("Give me a Final Distance ")
        num9 = input("Give me an Intial Distance ")
        result3 = float(num8) / float(num7) + int(num9)
        print(result3)
    elif info_user == "a":
        num16 = input("Give me a Velocity Final ")
        num17 = input("Give me a Velocity Intial ")
        num18 = input("Give me a Time ")
        result8 = float(num16) - float(num17) / float(num18)
        print(result8)
    elif info_user == "vf":
        num19 = input("Give me a Acceleration ")
        num20 = input("Give me a Time ")
        num21 = input("Give me a Intial Velocity ")
        result9 = float(num19) * float(num20) + int(num21)
        print(result9)

if choice_user == "math":
    print("select a function")
    print("Add or +")
    print("Subtract or -")
    print("Divide or /")
    print("Multiply or *")
    add_user = input("Choose One")
    if add_user == "add":
        num10 = input("First Number")
        num11 = input("Second Number")
        result4 = float(num10) + float(num11)
        print(result4)
    elif add_user == "subtract":
        num10 = input("First Number")
        num11 = input("Second Number")
        result5 = float(num10) - float(num11)
        print(result5)
    elif add_user == "divide":
        num12 = input("First Number")
        num13 = input("Second Number")
        result6 = float(num12) / float(num13)
        print(result6)
    elif add_user == "multiply":
        num14 = input("First Number")
        num15 = input("Second Number")
        result7 = float(num14) * float(num15)
        print(result7)




    
    
    


