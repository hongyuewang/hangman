# https://www.asciiart.eu/miscellaneous/noose
# https://ascii.co.uk/art/hangman

import random
from words import word_list

def get_random_word():
    word = random.choice(word_list)
    return word.upper()

def return_drawing(tries):
    stages = [
        """
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
              |
              |
              |
        =========
        """,
        """
          +---+
          |   |
              |
              |
              |
              |
        =========
        """
    ]
    return stages[tries]

def print_missing_letters(word):
    print("_ " * (len(word) - 1)),
    print("_")


def play(word):
    is_correct = False
    tries_left = 6
    guessed_letters = []

    print(
        """
         _                                             
        | |                                            
        | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
        | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
        | | | | (_| | | | | (_| | | | | | | (_| | | | |
        |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                            __/ |                      
                           |___/                       
        """
    )
    
    print_missing_letters(word)


play(get_random_word())

