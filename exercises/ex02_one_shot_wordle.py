"""EXO2 - One Shot Wordle Program."""

__author__ = "730469023"

secret_word: str = input("What would you like your secret word on Wordle to be?: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def yellow_box():
    j: int = 0
    while j < len(secret_word):
        if word_guess[i] == secret_word[j]:
            return True
        else:
            j += 1
    else: 
        return False


word_guess: str = input("What is your {}-letter guess? " .format(len(secret_word)))


if len(word_guess) != len(secret_word):
    while len(word_guess) != len(secret_word):
        word_guess: str = input("That was not {} letters! Try again: " .format(len(secret_word)))

i: int = 0

wordle_box_string: str = ""

while i < len(secret_word):
    if word_guess[i] == secret_word[i]:
        wordle_box_string += GREEN_BOX + " "
        i += 1
    else:
        if yellow_box() is True:
            wordle_box_string += YELLOW_BOX + " "
            i += 1
        else:
            wordle_box_string += WHITE_BOX + " "
            i += 1

print(wordle_box_string)

if word_guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")