import time

    
def Intro():
    intro_options = ["Yes", "yes", "No", "no"]
    change = ""
    while change not in intro_options:
        print("You arrive at your friend Jackson's house to pick him up for the party")
        print("He comes out wearing a deep v-neck. You see a tuft of chest hair.")
        time.sleep(3)
        print()
        print("You are tempted to tell him to change because you don't want to be seen")
        print("entering the party with him.")
        change = input("Do you tell Jackson to change? Yes or no? >> ")
        if change == "No" or "no":
            NotChange()
        elif change == "Yes" or "yes":
            Change()
        
def Change():
    print("Jackson looks hurt. He asks you if it really looks that bad. You say yes.")
    time.sleep(3)
    print("He goes back in and changes and the rest of the car ride is spent in silence.")
    Party()
    
def Party():
    print()
    print("You get to the party and you and Jackson walk up to your friend group")
    time.sleep(1)
    print("However you and Jackson don't talk to each other.")
    next = input("What would you like to do next? A: talk and apologize to Jackson, B: stay with your buddies, C: wander off? >> ")
    if next == "A" or "a":
        Apology()
    elif next == "B" or "b":
        Bro()
    else:
        WanderOff()
        
def NotChange():
    print("You get to the party and your buddies taunt Jackson")
    print()
    print("Jackson leaves the group and starts talking to new people.")
    follow = input("Do you A: follow Jackson, B: stay with your buddies, C: wander off? >> ")
    if follow == "A" or "a":
        Apology()
    elif follow == "B" or "b":
        Bro()
    else:
        WanderOff()
        
def WanderOff():
    print()
    print("Wow, you met a girl. You won! But you and Jackson are no longer friends.")
    print("But hey, that's life.")
    print()
    
def Bro():
    print()
    print("You spend the rest of the night getting hammered and tomorrow you are hungover. You lose")
    
def Apology():
    print()
    print("You tell Jackson that you will support his v-neck-wearing journey")
    print("You and Jackson are still friends and you ditch the dudebros. You win.")


Intro()
playAgain = input("Would you like to play again?")
if playAgain == "Yes" or "yes" or "y":
    Intro()
else:
    print("Thanks for playing! Bye bye.")