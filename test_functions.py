# https://docs.python.org/3/library/unittest.mock.html
# https://docs.python.org/3/library/unittest.html#module-unittest
import unittest # Import testing framework
from unittest.mock import patch # Import function decorator 
from unittest.mock import MagicMock # Import testing object


import os # Imports ability to interact with Operating System
from classes import MakeCharacter # Import MakeCharacter class

from functions import get_valid_weapon # Import function
from functions import save_character_to_file # Import function
from functions import create_character_from_input # Import function


@patch('random.choice', return_value=15)
def test_attack_power(mock_random_choice):
    '''Test the get_valid_weapon function '''
    
    character = MakeCharacter(name="Test", age=25, weapon="Sword")
    attack_value = character.attack_power()

    assert attack_value == 15, f"Expected attack power to be 15, but got {attack_value}"
    assert character.attack == 15, f"Expected attack to be 15, but got {character.attack}"


def test_save_character_to_file():
    '''Test the save_character_to_file function.'''

    character_data = {
        "name": "Alice",
        "age": 25,
        "weapon": "Sword"
    }
    character = MakeCharacter(**character_data)
    character.attack_power()
    assert os.path.exists('test_character_data.json') == False


def test_create_character_negative_age():
    ''' Test the create_character_from_input function'''
    
    inputs = [
        'TestCharacter',  
        '-5',  
        '25', 
        'Bow'  
    ]

    with patch('builtins.input', side_effect=inputs):
        character = create_character_from_input()
    
    assert character.age == 25