
# Create a new file called "guess.py" 
# Create a variable and assign it the value of a word to be guessed by the user. This should be a single word with at least 6 characters


guessed = []


def showBoard():
    word_to_guess = 'python'
    wordBoard = ['_']*len(word_to_guess)
    
    def get_letter_position(guess, word, spaces):
        index = -2
        while index != -1:
            if guess in word:
                index = word.find(guess)
                removed_character ='*'
                word = word[:index]+removed_character+word[index+1:]
                wordBoard[index] = guess
            else:
                index = -1
     
        return (word, spaces)


    def win_check():
        for i in range(0, len(spaces)):
            if spaces[i] == '_':
                return -1
     
        return 1

    num_turns = len(word)
    for i in range(-1, num_turns):
        guess = input('Guess a character:')
 
        if guess in word:
            word, spaces = get_letter_position(guess, word, spaces)
            print(spaces)
        else:
            print('Sorry that letter is not in the word.')
     
        if win_check() == 1:
            print('Congratulations you won')
            break
     
        print('you have '+str(num_turns - i)+' turns left.')
        print()
#     turns = 5
#     # failed = 0
#     while turns > 0:
#         print(f'Welcome to the Guessing Game!!\n Below is the word board.\n GOOD LUCK!!\n------------------')
#         print(wordBoard)
#         user_guess = input('What Letter would you like to guess?')
#         check_guess(user_guess)    

# def check_guess(letter):
#     if letter in word_to_guess:
#         if letter in guessed:
#             print(f'You have already guessed {letter}.. Please try again...')

#         else: 
#             print(f'{letter} is correct!!')
#             guessed.append(letter)
#             print(wordBoard.append(letter))
#             return True
#     else:
#         if letter in guessed:
#             print(f'You have already tried that word. Guess again')
#             return True
#         else:
#             print(f'{letter} is incorrect..')
#             guessed.append(letter)
#             print(guessed)
#             return True
showBoard()
    # if letter in word_to_guess:
    #     if letter in guessed:
    #         print(f'You have already guessed {letter}.. Please try again...')
            
    #     else:
    #         print(f'{letter} is correct!!')
    #         guessed.append(letter)
           

            # print('_', end=' ')
            # failed += 1

# def add():
#     for i in range(len(word_to_guess)):
#         if (word_to_guess[i] == guessed):
#             wordBoard.append(i)
#             return True
# print(wordBoard)





# Create a function called “checkGuess”. 
# This function requires one parameter, the user’s guessed letter.
# This function should check if the guessed letter is in the secret word.
# If it is, then update “wordBoard” by placing the correctly guessed letter in the correct position.
# Remember that a word may have more than one instance of the guessed letter.
# This function should return a Boolean value of True if the letter was found, otherwise False.
# Display the board to the user
# Prompt the user to guess a letter
# If the user already guessed that letter, let the user know that
# If the letter is in the secret word, display the updated board with the letters in the correct place
# If the letter is not in the secret word, keep track of the number of wrong guesses.  When the user has five wrong guesses and the word hasn’t yet been guessed, then the game ends.
# If the user has guessed all of the letters, the game ends.  Display the fully solved board to the user.
# Continue prompting the user till they run out of chances or solve the puzzle.
# Hint: You will find it easier if the word and all of the user guesses are uppercase.