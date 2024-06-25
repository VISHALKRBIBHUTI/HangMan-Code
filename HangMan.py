import random

# ASCII art for the game title
print('''
____    __    ____  _______  __        ______   ______   .___  ___.  _______ 
\   \  /  \  /   / |   ____||  |      /      | /  __  \  |   \/   | |   ____|
 \   \/    \/   /  |  |__   |  |     |  ,----'|  |  |  | |  \  /  | |  |__   
  \            /   |   __|  |  |     |  |     |  |  |  | |  |\/|  | |   __|  
   \    /\    /    |  |____ |  `----.|  `----.|  `--'  | |  |  |  | |  |____ 
    \__/  \__/     |_______||_______| \______| \______/  |__|  |__| |_______|
                                                                             
.___________.  ______                                                        
|           | /  __  \                                                       
`---|  |----`|  |  |  |                                                      
    |  |     |  |  |  |                                                      
    |  |     |  `--'  |                                                      
    |__|      \______/                                                       
                                                                             
 __    __       ___      .__   __.   _______ .___  ___.      ___             
|  |  |  |     /   \     |  \ |  |  /  _____||   \/   |     /   \            
|  |__|  |    /  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \           
|   __   |   /  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \          
|  |  |  |  /  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \         
|__|  |__| /__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\        
                                                                             
.__   __.      _______      ___      .___  ___.  _______                     
|  \ |  |     /  _____|    /   \     |   \/   | |   ____|                    
|   \|  |    |  |  __     /  ^  \    |  \  /  | |  |__                       
|  . `  |    |  | |_ |   /  /_\  \   |  |\/|  | |   __|                      
|  |\   |    |  |__| |  /  _____  \  |  |  |  | |  |____                     
|__| \__|     \______| /__/     \__\ |__|  |__| |_______|                           
''')

# Hangman stages
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
=========
''', '''
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

# Hints dictionary
hints = {
    'apple': 'A common fruit, often red or green.',
    'banana': 'A long, yellow fruit.',
    'cherry': 'A small, red fruit often found in pairs.',
    'date': 'A sweet fruit from a palm tree.',
    'elderberry': 'A dark purple berry used in jams and syrups.'
}

end_of_game = False
word_list = ["apple", "banana", "cherry", "date", "elderberry"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Retrieve the hint for the chosen word
hint = hints[chosen_word]

# Create a variable called 'lives' to keep track of the number of lives left.
# Setting 'lives' to 6.
lives = 6

# Print the hint instead of the solution
print(f'Hint: {hint}')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    if guess in display:
        print(f"You've already guessed {guess}. Try again.")
        continue

    # Track if the guess was correct
    correct_guess = False

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            correct_guess = True

    # If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    if not correct_guess:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was: {chosen_word}")
            break

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
