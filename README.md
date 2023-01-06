# Guess-the-word
This code is a simple word guessing game. 
The game generates a random word from a list of words and prompts the user to guess the word or individual letters in the word. 
The user has three lives, and they lose a life each time they guess incorrectly. 
If the user guesses the word correctly or correctly guesses all the letters in the word, they win the game. 
If they run out of lives before guessing the word correctly, they lose the game.
The code begins by importing the random module and defining the number of lives and the list of words that can be guessed. 
It then generates a random word from the list and stores it in the secret_word variable. 
The clue variable is initialized as a list of question marks that is the same length as the secret word, to provide a clue to the user about how many letters are in the word. 
The heart_symbol variable is a Unicode character for a heart, which is used to represent the user's remaining lives. 
The guessed_word_correctly variable is a flag that is set to True if the user guesses the word correctly and to False otherwise.
The update_clue function takes in three arguments: a guessed letter, the secret word, and the current clue. 
It iterates through the secret word and updates the clue by replacing any question marks with the guessed letter if the letter is present in the secret word.
The game is then played in a loop that continues until the user runs out of lives or guesses the word correctly. 
Inside the loop, the code prints the current clue and the user's remaining lives, prompts the user to enter a guess, and checks whether the guess is correct. 
If the user guesses the word or all the letters in the word correctly, the guessed_word_correctly flag is set to True and the loop is exited. 
If the user's guess is incorrect, their remaining lives are decreased by one.
After the loop ends, the code checks the value of the guessed_word_correctly flag and prints a message indicating whether the user won or lost the game.