import string # Imports string functions
import random # Imports function used for random output

#https://docs.python.org/3/library/json.html
import json # Imports Javascript Object Notation

import os # Imports ability to interact with Operating System
import numpy as np # Imports ability to read docstrings
from my_modules.classes import MakeCharacter

# Help from Assignment #3
# Prepares user input to work alongside additional functions
def prepare_text(input_string): 
    ''' Taking input string and divides into list

    Parameters
    - - - - - - -
    input_string : str
        string to be split into list

    Returns
    - - - - - - -
    out_list : list
        list of string
        '''
    # Takes string input, using functions to set all characters
    # lowercase and splitting into strings
    if type(input_string) == str:
        temp_string = input_string.lower() 
        out_list = temp_string.split() 

        return out_list 

# Help from Assignment #3
# Determines if elements from two variables match
def in_list(list_one, list_two):
    ''' If elements of first input is in second input

    Parameters
    - - - - - - -
    list_one : list
        elements to check
    list_two : list
        conditions elements need to match

    Returns
    - - - - - - - 
    boolean : boolean
        True or False 
        '''
    # For first provided elements, if present in second will return True
    # Otherwise, False
    for element in list_one:
        if element in list_two:
            return True
            
    return False

# Help from Assignment #3
# Based off elements provide and check, will return a response
def take_response(input_list, check_list, return_list):
    ''' If first input is present in second input, returning third

    Parameters
    - - - - - - -
    input_list : list
        element to check
    check_list : list 
        conditions elements need to match
    return_list : list
        based off match, specific list return

    Returns
    - - - - - - - 
    output : str
        specific list return
        '''
    # Output initially assigned to nothing
    output = None

    # If element present in first variable is also present in second
    # varible, will return assigned third variable
    for string in input_list: 
        if string in check_list: 
            output = return_list[0] 
            break 
       
    return output 

# Function to determine self.weapon attribute
def get_valid_weapon():
    ''' Weapon input for MakeCharacter class

    Return
    - - - - - - - 
    weapon : str
        input by user
        '''
    # Based of user input, if valid response will be stored
    # otherwise default is 'Fist'
    while True:
        weapon = input("Choose a weapon (Sword, Bow, Wand): ").capitalize()
        if weapon in MakeCharacter.valid_weapons:
            return weapon
        # Else, break out of loop and assign default
        else:
            break

# Takes input collected by chatbot to store within JSON file
def save_character_to_file(character_data, filename='character_data.json'):
    '''Save the character data to a file in JSON format

    Parameters
    - - - - - - - 
    character_data : dictionary
        data collected by inputs by user
    filename : str, default = 'character_data.json'
        name of file to be created
        
        '''
    # Using imported OS, determines if file exist. Inputs data within file
    # in a structured manner.
    if os.path.exists(filename):
        with open(filename, 'r+') as file:
            existing_data = json.load(file)
            existing_data.append(character_data)
            file.seek(0)
            json.dump(existing_data, file, indent=4)

    else:
        # Otherwise, new file is created and data is stored in a structured
        # manner
        with open(filename, 'w') as file:
            json.dump([character_data], file, indent=4)

# Takes previously made JSON data and is inputted into MakeCharacter()
def create_character_from_input():
    '''Interact with user and creates a character based on their input

    Return
    - - - - - - -
    character : object
        object created based off user input
        '''
    # Triggers reponse to allow user to input 'name'
    name = input('What\'s your character\'s name? ').strip()

    # While chatbot is triggered, allows input from user to assign int to age
    # if invald, a specific response is triggered
    while True:
        try:
            age = int(input('How old is your character? '))
            if age < 0:
                print('Age cannot be negative. Please try again.')
            else:
                break
        except:
            age = int(input(('Invalid input. Please enter a valid age.')))

    # Triggers get_valid_weapon() function
    weapon = get_valid_weapon()

   # Input reponses are within a dictionary to mimic JSON
    character_data = {
        'name': name,
        'age': age,
        'weapon': weapon
    }

    # Save character to file
    save_character_to_file(character_data)
    # Create the character object
    character = MakeCharacter(**character_data)
    
    # MakeCharacter() method is trigger to assign self.attack attribute
    character.attack_power()
    
    return character

# Help from Assignment #3
# Function to allow user to end chat
def end_chat(input_list):

    # If 'quit' is present as an string,
    # True is returned to return False
    if 'quit' in input_list:
        return True
        
    return False

# Help from Assignment #3
# Main function to run the chat
def have_a_chat():
    ''' Function to allow Chat to be ran

    Parameters
    - - - - - - - 
    msg : user input
        input send to chat

    Returns
    - - - - - - 
    out_msg : bot output
        output determines by input
        '''
    # When True, Chat is activated and character1 object is assigned
    # to MakeCharacter(). Beginning string is printed
    chat = True 
    character1 = MakeCharacter() 
    print('Type a greeting!')

    # in_intro set as false, allowing for introductions to begin first
    # and while chat is True, user is directed to input with no out_msg assigned yet
    in_intro = False
    while chat: 
        msg = input('INPUT :\t') 
        out_msg = None 

        # Input given goes through prepare_text function, returning 
        # appropriate format
        msg = prepare_text(msg)

        # If end_chat is True, Chat is False and is discontinued
        if end_chat(msg): 
            out_msg = 'Goodbye' 
            chat = False 

        # Responding to user input, therefore no out_msg
        if not out_msg:  
            introduction_in = ['hello', 'hi', 'hey', 'hola', 'greetings']
            introduction_out = ['Welcome to Character Creation! Questions will be prompted,' 
            'type anything to continue.' 
            ]

            # If msg is True through in_list function, out_msg function is triggered
            # and out_msg is given
            if in_list(msg, introduction_in):
                out_msg = take_response(msg, introduction_in, introduction_out) 
                in_intro = True

            # If in_intro is True but msg is not present in_list,
            # crated_character_from_input() is triggered and 
            # assigned to character1 object, ending the chat.
            elif in_intro and not in_list(msg, introduction_in):
                character1 = create_character_from_input()
                print('Thank you! Here is your character. Prompt the chat again to create another.')
                print(f"Character Created: {character1}")
                out_msg = f"Character Created: {character1}"
                break  # End the chat after character creation

        # If no appropriate input provided, out_msg string is triggered
        if not out_msg:
            out_msg = 'I\'m sorry, I didn\'t understand that.'

        # Printed chatbot response based off introduction interaction
        print('OUTPUT:', out_msg)