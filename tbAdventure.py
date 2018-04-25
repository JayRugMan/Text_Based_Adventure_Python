#!/bin/python
# Version 1.0 - baseline

import os
import random

directions = ['north', 'east', 'south', 'west']
facing_which_direction = 0
in_which_room = 0

def random_password():
    password_list = ['sandman', 'Lockhead', 'Babling brooK', 'Santa Claus', 'Peanut', 'fury flurry', 'clinician', 'random PassWord']
    p_word_picker = random.randint(0,(len(password_list) - 1))
    pw = password_list[p_word_picker]
    return pw

password = random_password()


room_0 = {'north' : 'a locked door', 'east' : 'a map', 'south' : 'the exit', 'west' : 'an open door'}
room_1 = {'north' : 'an open door', 'east' : 'an open door', 'south' : 'a wall', 'west' : 'a wall'}
room_2 = {'north' : 'an open door', 'east' : password, 'south' : 'a wall', 'west' : 'a wall'}
room_3 = {'north' : 'a wall', 'east' : 'an open door', 'south' : 'an open door', 'west' : 'a wall'}
room_4 = {'north' : 'a map', 'east' : 'a wall', 'south' : 'an open door', 'west' : 'an open door'}
room_5 = {'north' : 'a wall', 'east' : 'a wall', 'south' : 'an open door', 'west' : 'a wall'}
house = [room_0, room_1, room_2, room_3, room_4, room_5]
room_names = ['foyer', 'parlor', 'study', 'master bedroom', 'kitchen', 'bathroom']

what_you_see = house[in_which_room][directions[facing_which_direction]]
feedback = "Welcome to my old house."

user_input = ''

won = False


def main_display():
    print(
'''=== The House ===

current room: %s
direction you are facing: %s

straight ahead is %s

== Options ==
l = turn left
r = turn right
f = move forward
q = quit

"%s"
"What would you like to do?"
''' % (room_names[in_which_room], directions[facing_which_direction], what_you_see, feedback))


def turning_left(old_direction, dir_list):
    end_of_list = len(dir_list) - 1
    if old_direction == 0:
        new_direction = end_of_list
    else:
        new_direction = old_direction - 1
    return new_direction


def turning_right(old_direction, dir_list):
    end_of_list = len(dir_list) - 1
    if old_direction < end_of_list:
        new_direction = old_direction + 1
        return new_direction
    else:
        new_direction = 0
        return new_direction


def change_rooms(old_room, direction):
    # if you were in the foyer
    if old_room == 0:
        if direction == 0: # and if you are facing north
            new_room = 5 # you will enter the bathroom
        elif direction == 3: # and if you are facing west
            new_room = 1 # you will enter the parlor
    # if you are in the parlor
    elif old_room == 1:
        if direction == 1: # and if you are facing east
            new_room = 0 # you will enter the foyer
        elif direction == 0: # and if you are facing north
            new_room = 4 # you will enter the kitchen
    # if you are in the study
    elif old_room == 2:
        new_room = 3 # you will enter the master bedroom
    # if you are in the master bedroom
    elif old_room == 3:
        if direction == 1: # and if you are facing east
            new_room = 4 # you will enter the kitchen
        elif direction == 2: # and if you are facing south 
            new_room = 2 # you will enter the study
    # if you are in the kitchen
    elif old_room == 4:
        if direction == 2: # and if you are facing south
            new_room = 1 # you will enter the parlor
        elif direction == 3: # and if you are facing west
            new_room = 3 # you will enter the master bedroom
    # if you are in the bathroom
    elif old_room == 5:
        new_room = 0 # you will enter the foyer
    return new_room
    

def password_challenge(pw):
    os.system('cls' if os.name == 'nt' else 'clear')
    user_guess = raw_input('\nWhat is the password? ')
    if user_guess == pw:
        return True
    else:
        return False


def display_map():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(
'''                 === MAP of my house ===

                         -NORTH-  
                         
  +----------------+--------M-------+-----------------+ 
| |                |                |                 | |
E | master bedroom D     kitchen    |    bathroom     | W
A |                |                |                 | E
S +--------D-------+--------D-------+--------D--------+ S
T |                |                |                 | T
| |     study      |     parlor     D      foyer      M |
  |                |                |                 | 
  +----------------+----------------+--------E--------+ 
  
                        -SOUTH-
''')
    raw_input("\t      hit ENTER once you're done")


while(user_input != 'q'):
    os.system('cls' if os.name == 'nt' else 'clear')
    main_display()
    user_input = raw_input(': ')
    user_input = user_input.lower()
    # the fucntion to turn left is called if you choose to turn left
    if user_input == 'l':
        facing_which_direction = turning_left(facing_which_direction, directions)
    # the function to turn right is called if you choose to turn left
    elif user_input == 'r':
        facing_which_direction = turning_right(facing_which_direction, directions)
    # if you choose to go forward, a door must be open to change rooms
    elif user_input == 'f':
        # if the door is open, you change rooms
        if what_you_see == 'an open door':
            in_which_room = change_rooms(in_which_room, facing_which_direction)
            # if you make it into room 5 (bathroom), you win and can only go into room 1 and exit
            # your direction also changes to south
            if in_which_room == 5:
                feedback = "You get the treasure, now leave in peace."
                won = True
                facing_which_direction = 2
                room_0['west'] = 'a closed door'
            # if not in room five, feedback is given that you are in a new room
            else:
                feedback = "You're in a new room"
        # if the door is locked and you move forward, you are challenged for a password
        elif what_you_see == 'a locked door':
            # if you get the password right, the locked door becomes an open door
            if password_challenge(password):
                feedback = "You guessed right"
                room_0['north'] = 'an open door'
            # otherwise, the door stays locked and the password changes
            else:
                feedback = "You guessed wrong. It is written anew."
                password = random_password()
                room_2['east'] = password
        # if you see a wall, you're scolded, but given hope
        elif what_you_see == 'a wall':
            feedback = "You can't walk through walls yet"
        # if you see an exit, you leave the game by going forward
        elif what_you_see == 'the exit':
            user_input = 'q'
        # the door to the parlor - rest of the house - closed once you enter the bathroom
        elif what_you_see == 'a closed door':
            feedback = 'You have your treasure, please leave.'
        # if you see a map, you get to find where you are
        elif what_you_see == 'a map':
            display_map()
            feedback = "don't get lost now"
    what_you_see = house[in_which_room][directions[facing_which_direction]]


os.system('cls' if os.name == 'nt' else 'clear')
if won:
    print("\n\tCongradulations!!\n\tSpend it on charity, will ya?!\n")
else:
    print('\n\tSmell you later!\n')
  
    
    
    
    
    
    
    
    
