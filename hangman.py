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


def print_letters(word_list):
    for i in word_list:
        print(i, end=' ')


def print_user_interface(word, tries_left, displayed_letters, guessed_letters):
    print("\n\n\n\n\n")
    print(return_drawing(tries_left))
    print_letters(displayed_letters)
    print("\n")
    print_letters(guessed_letters)
    print("\n")


def play(word):
    is_correct = False
    tries_left = 6
    guessed_letters = []
    displayed_letters = []

    for i in range(len(word)):
        displayed_letters.append("_")

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

    while (tries_left > 0):
        if "_" not in displayed_letters:
            is_correct = True
            break

        print_user_interface(
            word, tries_left, displayed_letters, guessed_letters)

        is_in_guessed_list = True

        while is_in_guessed_list:
            guess = input("TAKE A GUESS: ").strip().upper()

            if not guess.isalpha():
                print("YOU MUST ENTER A LETTER.")
            elif guess in guessed_letters:
                print("YOU HAVE ALREADY GUESSED THIS LETTER.")
            else:
                is_in_guessed_list = False
                guessed_letters.append(guess)
                if guess in word:
                    index_list = [i for i, e in enumerate(word) if e == guess]
                    for i in index_list:
                        displayed_letters[i] = word[i]
                else:
                    tries_left -= 1

    print_user_interface(word, tries_left, displayed_letters, guessed_letters)
    print("\n\n")

    if is_correct:
        print("CORRECT.")
    else:
        print("YOU DIED.")
        print("THE WORD WAS: " + word.upper())

    valid_input = False

    while not valid_input:
        choice = input(
            "WOULD YOU LIKE TO START A NEW GAME? (Y/N): ").strip().upper()
        if choice == "Y":
            play(get_random_word())
        elif choice == "N":
            break
        else:
            print("PLEASE ENTER A VALID INPUT (Y/N): ")


play(get_random_word())
