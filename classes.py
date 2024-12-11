import string # Imports string functions
import random # Imports function used for random output
import numpy as np # Imports ability to read docstrings

# Class containing characteristic attributes to create a
# character
class MakeCharacter():
    ''' Main class to store data given by chatbot inputs 
    
    Attributes
    - - - - - - -
    name : str
        name of character 
    age : int
        age of character 
    weapon : str
        weapon of character 
    health : int
        default 100, health of character
    attack : int
        randomized, attack of character
     weapon : str
         weapon of character'''
    
    # List providing a limit response for weapons and attacks
    valid_weapons = ['Sword', 'Bow', 'Wand']
    valid_attack = [10, 15, 20]

    # Instance Attributes that make up characteristic of character
    def __init__(self, name=None, age=None, weapon=None,):
        self.health = 100
        self.name = name if name else 'Unknown'
        self.age = age
        self.attack = None
        
        # Default to 'Fists' if invalid input
        self.weapon = weapon if weapon in self.valid_weapons else 'Fists'
        
    # Function tied to self.attack
    def attack_power(self):
        ''' Assigns random int to self.attack attribute
        
        Returns
        - - - - - - -
        self.attack : int
            instance attribute of character
        '''
        # Randomly picks from 'choices' to assigned int to
        # self.attack
        choices = [10, 15, 20]  
        self.attack = random.choice(choices)  
        
        return self.attack
        
    # Function to return information
    def __str__(self):
        ''' Prints information regarding character created 

        Print
        - - - - - - -
            string representation of character
            '''
        # Provides a string representation of the character
        return (
            f"Character(name={self.name}, "
            f"age={self.age}, "
            f"weapon={self.weapon}, "
            f"health={self.health}, "
            f"attack={self.attack})"
        )