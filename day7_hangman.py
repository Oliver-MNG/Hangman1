import random
from words import words

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
end_of_the_game = False
display = []
lives = 6
chosen_word = random.choice(words).lower()
word_length = len(chosen_word)
guessed = []


#Todo 1: add the same amount of "_" to the variable display as letters in word_length

                                       # Hint:    print(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)

#Todo 2:

# Main part: while not end of the game do the following steps over and over again


while not end_of_the_game:

    #input the letter you guessed
    guess = input("Guess a letter: ").lower()
    
    if guess in guessed:
        print("You have already tried this letter! ")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    #Print the statement when player guessed wrong
    if guess not in chosen_word and guess not in guessed:
        lives -= 1
        print(f"You have {lives} lives left.")
        print(stages[lives])
        if lives == 0:
            print("You are out of life.")
            print("You loose")
            print(f"The word was {chosen_word}")
            end_of_the_game = True
    #If all the blank spaces in display are filled all the letter are guessed right so game is over player won   
    elif "_" not in display:
        end_of_the_game = True
        print("You won! This is the end of the game!")
    guessed += guess
    



#Todo 3

"""
for letter in chosen_word:
    if letter == guess:
        print("right")
    else:
        print("wrong")
"""