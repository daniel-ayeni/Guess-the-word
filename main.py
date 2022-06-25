# import python random module to use choice
import random
# variable to hold the number of lives or trial available which is 3
lives = 3
# a list to hold the words that will be guessed by the user
words = ['pizza', 'fairy', 'teeth', 'shirt', 'otter', 'plane']
# the random word chosen will be stored in this variable called secret_word
secret_word = random.choice(words)

clue = list('?????')
heart_symbol = u'\u2764'

guessed_word_correctly = False


def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index += 1


while lives > 0:
    check = "".join(clue)
    print(clue)
    print('Lives left: ' + heart_symbol * lives)
    guess = input('Guess a letter or the whole word: >_').lower()

    if guess == secret_word or check == secret_word:
        guessed_word_correctly = True
        break

    if guess in secret_word:
        update_clue(guess, secret_word, clue)

    else:
        print('Incorrect. You lose a life')
        lives -= 1

if guessed_word_correctly:
    print('You won! The secret word was ' + secret_word)
else:
    print('You lost! The secret word was ' + secret_word)
