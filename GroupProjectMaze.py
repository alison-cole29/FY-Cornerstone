"""
Group 6 Pico Portion of Term Long Project
Ali, Elizabeth, Glori, Sohum (cornerstone clashers)
November 13th, 2025

"""

from machine import Pin
import time
import random

''' ===== Define Variables ========================================================================================================================= '''

# Set up button pins as an input
button1Pin = 15 # right
button1 = Pin(button1Pin, Pin.IN, Pin.PULL_UP)
button2Pin = 14 # left
button2 = Pin(button2Pin, Pin.IN, Pin.PULL_UP)

# Set up lights as output
left_led_pin = 13 # yellow left light
left_led = Pin(left_led_pin, Pin.OUT)
right_led_pin = 16 # red right light
right_led = Pin(right_led_pin, Pin.OUT)

# Turn lights off (if they were set on from before)
right_led.off()
left_led.off()

# Define colors as variables
# (in case we switch these later, now I don't need to go fix the code)
left_color = "YELLOW"
right_color = "RED"

# Define a "try number" for the turn taking
try_number = 1

# Create blank array for successful turns
directions = ["", "", "", "", ""]


''' ===== Define Functions ======================================================================================================================= '''

''' ----- Turning animations --------------------------------------------------- '''

# Slide 1 and slide 5 (if correct turn)
def print_far_turn():
    print("\n\n\n\n\n\n\n\n\n\n\n\n")
    print(" '-.                          .-'")
    print("    '-.                    .-'")
    print("       '-.              .-'")
    print("         |#|---------|#|")
    print("         |#| <-   -> |#|")
    print("         |#|_________|#|")
    print("       .-'_____________'-. ")
    print("    .-'____________________'-.")
    print(" .-'__________________________ '-.")
    
# Slide 2
def print_getting_closer():
    print("\n\n\n\n\n\n\n\n\n\n\n\n")
    print("     |                      |")
    print("     |-_                  _-|")
    print("     |##|----------------|##|")
    print("     |##|                |##|")
    print("     |##|  /__      __\  |##|")
    print("     |##|  \``      ``/  |##|")
    print("     |-_| ______________ |_-|")
    print("   .-' ____________________ '-.")
    print(".-'  ________________________  '-.")
    
# Slide 3 (left version)
def print_turn_left():
    print("\n\n\n\n\n\n\n\n\n\n\n\n")
    print("     |#########///")
    print("     |########")
    print("     |##//'")
    print("     |#/''         /__    ")
    print("     |'-.          \```     ")
    print("     |-   '-.         ")
    print("     |        '-.")
    print("   .-'            '-.")
    print(".-'                   '-.")
    
# Slide 4 (right version)
def print_turn_right():
    print("\n\n\n\n\n\n\n\n\n\n\n\n")
    print("              #########| ")
    print("                   '\\##|")
    print("       __\         ''\#|")
    print("      ```/          .-'|")
    print("                .-'   -|")
    print("            .-'        |")
    print("        .-'            '-.")
    print("    .-'                   '-.")
    print(".-'                          '-.")

# Slide 5 (if wrong turn)
def print_wrong_turn():
    print("\n\n\n\n\n\n\n\n\n\n\n\n")
    print("  `-.                       .-`")
    print("    |---------------------|")
    print("    |  #               #  |")
    print("    |  #   Dead end    #  |")
    print("    |  #  turn around! #  |")
    print("    |  _________________  |")
    print("  -` _____________________ `-")
    print("-` __________________________ `-")

# Play animation
def turning_animation(direction, correct):
    print_far_turn()
    time.sleep(.4)
    print_getting_closer()
    time.sleep(.4)
    if direction == "Right":
        print_turn_right() # print right version if taking right turn
    elif direction == "Left":
        print_turn_left() # print left version if taking left turn
    time.sleep(.4)
    if correct == True:
        print_far_turn() # print if they turned the right way
    elif correct == False:
        print_wrong_turn() # print if they turned the wrong way
    time.sleep(.75) # wait on this one longer
        
    print("\n\n\n\n\n\n\n\n\n\n\n\n")
    # reset screen

def print_computer(eye, mouth, line1, line2, line3, line4, line5, line6):
    print(f"         _________________")
    print(f"        | _______________ |")
    print(f"        | |             | |          {line1}")
    print(f"        | |  o       o  | |          {line2}")
    print(f"        | |      _      | |          {line3}")
    print(f"        | |             | |          {line4}")
    print(f"        | |_____________| |          {line5}")
    print(f"        |_________________|          {line6}")
    print(f"            _[_______]_")
    print(f"        ___[___________]___")
    print(f"       |         [_____] []|__")
    print(f"       |         [_____] []|  \__")
    print(f"       L___________________J     \\")
    print(f"        ___________________      /\\")
    print(f"       /###################\    (__)")

''' ----- Define functions for running --------------------------------------------------- '''

# Button checking
def check_buttons():
    # Left button pressed, right button not
    if button1.value() == 0 and button2.value() == 1:
        return "Left"
    
    # Right button pressed, left button not
    if button2.value() == 0 and button1.value() == 1:
        return "Right"
    
    # Accounts for no buttons pressed and 2 buttons pressed
    else:
        return "Error"
    
# Button to move forward
def wait_for_button():
    while True:
        confirm = check_buttons()
        if confirm == "Right" or confirm == "Left":
            break
        else:
            time.sleep(.1)
    time.sleep(.5)

# Tutorial Running
def tutorial():
    print(f"Pressing the {left_color} button takes a left turn.")
    print("Go on! Let's see if it still works!")

    while True:
        turn = check_buttons()
        if turn == "Left":
            turning_animation("Left", True)
            print("Looks like that button still works!")
            break
        elif turn == "Right":
            print("Oops; try the other one!")
            time.sleep(.5)

    time.sleep(.5)
    print(f"What about the {right_color} button? I think it takes us right!")

    while True:
        turn = check_buttons()
        if turn == "Right":
            turning_animation("Right", True)
            print("We're turning right! That's the spirit! Nice button pressing.")
            break
        elif turn == "Left":
            turning_animation("Left", True)
            print(f"Oh no, the {left_color} button turns left, remember?")
            time.sleep(.5)
    
    time.sleep(.5)

# Propogate new random directions into list
def new_directions():
    for i in range(len(directions)):
        turn = random.randint(0,1)
        if turn == 1:
            directions[i] = "Right"
        else:
            directions[i] = "Left"
            
''' ===== Main Game Loop ======================================================================================================================= '''

# Screen that stays open while waiting for users to start
print_far_turn()
print("\n\n        PASSENGER FLOORS")
print("Press either button to get started!")
wait_for_button()
print("\n\n\n\n\n\n\n\n\n\n\n\n")

# Start narrative for part
print("The ships emergency lighting went down!")
print("But, you still need to find your way off of the ship.")
print("\n\nEscape the ship by taking left and right turns")

print("\n(press button)")
wait_for_button()
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

# Play tutorial to teach users how to use buttons
tutorial()

print("\n\n\n\n\n\n\n\nLet's use our buttons to take turns to get off the ship.")
print("Press either to get started!")
wait_for_button()
print("\n\n\n\n\n\n\n\n\n")
picked_wrong = False

while True:
    new_directions()
    for i in range(5):
        correct_direction = directions[i]
        print("Do you want to go left? Or right?")
        print(f"Remember: {left_color} = left, {right_color} = right")
        print(f"(Turn {i+1}/5)")
        
        # Wait for answer
        while True:
            user_turn = check_buttons()
            
            if user_turn == correct_direction:
                turning_animation(user_turn, True)
                print("Good turn!")
                time.sleep(1)
                picked_wrong = False
                break
            elif user_turn == "Right" or user_turn == "Left":
                turning_animation(user_turn, False)
                print("Wrong turn :(")
                try_number = try_number + 1
                picked_wrong = True
                break
            else:
                time.sleep(0.1)
        if picked_wrong == True:
            break
    if picked_wrong == False:
        print("Woah!! You found your way off! That was scary, I didn't know where to go!")
        time.sleep(.5)
        break
    elif try_number > 2:
        print("Looks like that's two tries...")
        break
    
    print(f"Agh. Let's try again!")
    print("I'm all turned around. I think the turns are going to be different this time.")
    print(f"You're on try number {try_number}")
    time.sleep(.5)
    
time.sleep(1)
print("Woahhahaha!")
print("This thing is coming to life!")

time.sleep(1)
print("Look at those lights!")

for i in range(10):
    right_led.on()
    time.sleep(.05)
    left_led.on()
    time.sleep(.05)

    right_led.off()
    time.sleep(.05)
    left_led.off()
    time.sleep(.05)

print("It says here that they're emergency navigation systems...")

time.sleep(1)
print(f"Reading the instructions... seems like they light up {left_color} for a left turn and {right_color} for a right turn!")

print("Let's find our way off this boat again, this time with the working systems!")

try_number = 1
while True:
    new_directions()
    for i in range(5):
        correct_direction = directions[i]
        print("Do you want to go left? Or right?")
        print(f"Remember: {left_color} = left, {right_color} = right")
        print(f"(Turn {i+1}/5)")
        
        if correct_direction == "Right":
            right_led.on()
        else:
            left_led.on()
        # Wait for answer
        while True:
            user_turn = check_buttons()
            if user_turn == correct_direction:
                turning_animation(user_turn, True)
                print("Good turn!")
                time.sleep(1)
                picked_wrong = False
                break
            elif user_turn == "Right" or user_turn == "Left":
                turning_animation(user_turn, False)
                print("Wrong turn :(")
                try_number = try_number + 1
                picked_wrong = True
                break
            else:
                time.sleep(0.1)
                
        right_led.off()
        left_led.off()
        
        if picked_wrong == True:
            break
    if picked_wrong == False:
        print("We did it!!")
        time.sleep(.5)
        break
    elif try_number > 3:
        print("Looks like that's three tries...")
        break
    
    print(f"Agh. Let's try again!")
    print("I'm all turned around. I think the turns are going to be different this time.")
    print(f"You're on try number {try_number}")
    time.sleep(.5)
    
print("And... we've made it out of the passenger deck!")

time.sleep(.5)

print("Up on the hull... Look there!")

time.sleep(.5)

print("There's the word! 'LIFEBOATS' ")
