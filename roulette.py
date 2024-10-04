import os
import sys
import time
import random
from playsound import _playsoundWin

def fire(firearm, chamber):
    if (firearm[chamber]):
         print("[BANG!]")
         sys.exit()
    else:
         print("[click]")
    time.sleep(1.5)

def user_pull(ans):
     while (not ans.lower() ==  "*pull*" and not ans.lower() == "pull" and not ans.lower() == "*pull"):
          print("You are scared now?  Just go *pull*, with your finger.")
          ans = str(input())

print("Хотите играть в русском стиле?")
choice = str(input())

if (choice.lower() == "yes" or choice.lower() == "da" or choice == "да"):
    gun = [False,False,False,False,False,True]

    print("Wonderful, my comrade! We play Russian style roulette.")
    time.sleep(4)
    print("Here, you spin so is fair.")
    #_playsoundWin("C:\Real Stuff\VS Coding\dylan.mp3")      # get someone to speak the lines in Russian accent
    choice = str(input())

    while (not choice.lower() == "*spin*" and not choice.lower() == "spin" and not choice.lower() == "*spin"):
         print("No, like this.")
         time.sleep(2.5)
         print("*spin*")
         time.sleep(1)
         print("Now you do so is fair.")
         choice = str(input())
    
    random.shuffle(gun)

    print("Good spin, my comrade!")
    time.sleep(3)
    print("Do you want first go?")
    choice = str(input())

    if (choice.lower() == "yes" or choice.lower() == "da" or choice == "да"):
         print("Ho ho, I like your courage.  Go ahead then, pull the trigger.")
         choice = str(input())

         user_pull(choice)
         fire(gun, 0)
         
         print("Oh boy, now is my turn.")
         time.sleep(4)

         fire(gun, 1)

         print("My my, here you are, my friend.")
         choice = str(input())

         user_pull(choice)
         fire(gun, 2)

         print("Uh oh, me again, ha ha.")
         time.sleep(4)

         fire(gun, 3)

         print("Well, my friend, things get interesting!  Here you are.")
         choice = str(input())

         user_pull(choice)
         fire(gun, 4)

         print("Oh...")
         time.sleep(1.5)
         print("Oh no...")
         time.sleep(1.5)
         print("Well, this is where we part, my friend.  It was good to meet you.")
         time.sleep(7)

         fire(gun, 5)
    else:
         print("My friend!  I guess I asked though.  Okay, I first.")
         time.sleep(5)

         fire(gun, 0)

         print("Ho ho, now is your turn.")
         choice = str(input())

         user_pull(choice)
         fire(gun, 1)

         print("Uh oh, me again, ha ha.")
         time.sleep(4)

         fire(gun, 2)

         print("My my, here you are, my friend.")
         choice = str(input())

         user_pull(choice)
         fire(gun, 3)

         print("Well, my friend, things get interesting!  My go.")
         time.sleep(5)

         fire(gun, 4)

         print("Oh...")
         time.sleep(1.5)
         print("Oh no...")
         time.sleep(1.5)
         print("Well, this is where we part, my friend.  Whenever you are ready.")
         choice = str(input())

         user_pull(choice)
         fire(gun, 5)

else:
    sys.exit("Sorry.  Exhibit still in development.")
    wheel = []
    os.system('cls')

    print("Very well then, let's play roulette.")
    print("Please place your bets.")