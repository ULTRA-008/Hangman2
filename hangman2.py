

# --- Imports and wordlist ---
import random
from random_words import easy_wordlist, medium_wordlist, hard_wordlist
import getpass

# --- Hangman stages ---
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''' ]


# --- Difficulty selection ---

# --- Word selection (difficulty or own word) ---
def choose_word():
    while True:
        mode = input("Type 'own' to enter your own word, or choose difficulty (easy, medium, hard): ").strip().lower()
        if mode == 'own':
            while True:
                word = getpass.getpass("Enter your word (letters only, no spaces): ").strip().lower()
                if word.isalpha():
                    print("Word accepted! Let's play.")
                    return list(word)
                else:
                    print("Invalid word. Please use only letters, no spaces or symbols.")
        elif mode == "easy":
            return list(random.choice(easy_wordlist))
        elif mode == "medium":
            return list(random.choice(medium_wordlist))
        elif mode == "hard":
            return list(random.choice(hard_wordlist))
        else:
            print("Invalid choice. Please type 'own', easy, medium, or hard.")

# --- Main game loop ---
def play_game():
    chosen_word = choose_word()
    blank = ""
    for letter in chosen_word:
        blank += "_"
    blank_list = list(blank)
    update_display = 0
    used_letters = set()

    def making_a_guess():
        nonlocal update_display
        correct_guess = False
        used_letters.add(guess.lower())
        for i, letter in enumerate(chosen_word):
            if guess.lower() == letter:
                blank_list[i] = guess.lower()
                correct_guess = True
                print(f"Good guess! {guess} is in the word.")
        if not correct_guess:
            print(f"There is no {guess}, sorry.")
            update_display += 1

    print(HANGMANPICS[update_display])
    print(''.join(blank_list))
    print(f"Used letters: {', '.join(sorted(used_letters))}")
    while update_display < 6:
        while True:
            guess = input("Make a guess: ").strip().lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
            elif guess in used_letters:
                print(f"You already guessed '{guess}'. Try a different letter.")
            else:
                break
        making_a_guess()
        print(HANGMANPICS[update_display])
        print(''.join(blank_list))
        print(f"Used letters: {', '.join(sorted(used_letters))}")
        if blank_list == chosen_word:
            print("YOU WIN!")
            return
    print("GAME OVER.")
    print(f"The word was: {''.join(chosen_word)}")

# --- Play again loop ---
while True:
    play_game()
    again = input("Play again? (y/n): ").strip().lower()
    if again != 'y':
        print("Thanks for playing!")
        break