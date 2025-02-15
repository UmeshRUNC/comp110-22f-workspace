"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730469023"

instance_count: int = 0
word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
character: str = input("Enter a single character: ")
if len(character) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for {} in {}".format(character, word))
for i in range(len(word)):
    if character == word[i]:
        instance_count += 1
        print("{} found at index {}" .format(character, i))
if instance_count == 0:
    print("No instances of {} found in {}." .format(character, word))
if instance_count > 1:
    print("{} instances of {} found in {}" .format(instance_count, character, word))
if instance_count == 1:
    print("{} instance of {} found in {}" .format(instance_count, character, word))