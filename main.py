import string
import random
from prefixtree import PrefixTree

#----------------------------------------
# Dictionary initalization
#----------------------------------------
print('Loading dictionary...')

# Opening text file that contains the dictionary
with open('words.txt') as wordFile:
    wordList = wordFile.read().split()

# Inserting dictionary into a prefix tree
prefix_tree = PrefixTree(wordList)


#----------------------------------------
# Character bank initialization
#----------------------------------------
bank_length = random.randrange(1, 5)
bank = ''
vowels = 'AEIOU'

for i in range(bank_length):
    character = random.choice(string.ascii_uppercase)

    if character not in bank:
        bank += character

# Ensuring that the bank has at least one vowel
if not any(x in bank for x in vowels):
    bank += random.choice(vowels)


#----------------------------------------
# Game
#----------------------------------------
print(f"List as many words as you can that contain the following characters (you can use each character more than once): {bank}")

cont = True
used_words = []
score = 0

while cont:
    word = input('Enter a word: ')

    for i in bank:
        if i.lower() not in word:
            print('You must use each character in the bank at least once! Try again.')
            cont = False
            break

    if not cont:
        cont = True
    elif prefix_tree.contains(word):
        if word not in used_words:
            used_words.append(word)
            score += 1
            print(f'Correct! You have {score} correct word(s).')
        else:
            print('You already used that word.')       
    else:
        print('Not a valid word.')

    choice = input('Would you like to continue? (y/n): ')

    if choice == 'n':
        cont = False

print(f"Game Ended. You got {score} correct word(s).")