import os
import random

from hangman_words import word_list
word = random.choice(word_list)
length = len(word)

end_of_game = False
lives = 6

from hangman_art import  logo, stages
print(logo)
print(f'Pssst, the solution is {word}.')

display = []
for i in range(length):
    display += "_"

while not end_of_game:
    user_guess = input("Please Enter A Letter : ").lower()
    #os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" * 100)
    
    if user_guess in display:
        print(f"You already guessed {user_guess}")
    
    for position in range(length):
        letter = word[position]
        #print(f"Current position : {position}\n Current Letter: {letter}\n Guessed letter:{user_guess}")
        if letter == user_guess:
            display[position] = letter
    
    if user_guess not in word:
        lives -= 1
        print(f"You guessed {user_guess}, that's not in the word. You lose a live. You Only Left {lives}")
        if lives == 0:
            end_of_game = True
            print("You Lose")
        
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You Win!!!!")
        
    print(stages[lives])



