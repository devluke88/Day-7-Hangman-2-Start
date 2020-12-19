#Step 2
from replit import clear
import random
import hangman_art
import hangman_words

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')
print(hangman_art.logo)
#Create blanks
display = []
for i in chosen_word:
    display.append("_")

lives = 6
koniec = False
guessed = []
while koniec is False:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in guessed:
        print(f"You've already guessed {guess}")
        lives -= 1
        print(hangman_art.stages[lives])
    else:
        guessed += guess
      #Check guessed letter
        for j in range(len(chosen_word)):
            if chosen_word[j] == guess:
                display[j] = guess
        
        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            print(hangman_art.stages[lives])

    print(" ".join(display))
    if lives <= 0:
      clear()
      print("You lose.")
      print(hangman_art.stages[lives])
      break;
    if "_" not in display:
      clear()
      print("You win.")
      break;
 
  