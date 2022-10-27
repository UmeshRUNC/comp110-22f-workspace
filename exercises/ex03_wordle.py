"""EX03 - Structured Wordle - Wordle."""

__author__ = "730469023"


def contains_char(string: str, character: str) -> bool:
    """Searches for the character in string."""
    assert len(character) == 1
    for i in range(len(string)):
        if character == string[i]:
            return True
    return False


def emojified(string: str, guess: str) -> str:
    """Returns a string of emojis that resembles wordle."""
    assert len(string) == len(guess)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    wordle_box_string: str = ""

    while i < len(string):
        if guess[i] == string[i]:
            wordle_box_string += GREEN_BOX
            i += 1
        else:
            if contains_char(string, guess[i]) is True:
                wordle_box_string += YELLOW_BOX
                i += 1
            else:
                if contains_char(string, guess[i]) is False:
                    wordle_box_string += WHITE_BOX
                    i += 1
    return (wordle_box_string)


def input_guess(expected_length: int) -> str:
    """A function to check if user's guess has the right number of characters as the string."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loops."""
    string: str = "codes"
    guess: str = ""
    turn_number: int = 1
    result: bool = False
    while turn_number <= 6 and result is False:
        print(f"=== Turn {turn_number}/6 ===")
        guess = input_guess(len(string))
        print(emojified(string, guess))
        if string == guess:
            print(f"You won in {turn_number}/6 turns!")
            result = True
        else:
            turn_number += 1
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()