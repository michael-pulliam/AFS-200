
def showBoard():
    intro = 'Can you Guess the word?'
    prompt = 'Guess a letter: '
    word = 'mom'
    guessed = []
    wordBoard = ['_']*len(word)
    turns = 7
    print(intro)

    def checkGuess(guess,word,wordBoard):
        if guess in word:
            i = word.find(guess)
            removed_character='*'
            word = word[:i]+removed_character+word[i+1:]
            wordBoard[i]=guess
            print(guessed)
            return (word,wordBoard)
     
    def win_check():
        for i in range(0, len(wordBoard)):
            if wordBoard[i] == '_':
                return -1
        return 1 
    
    while turns > 0:
        guess = input(prompt)
        if guess in word:
            word,wordBoard=checkGuess(guess,word,wordBoard)
            guessed.append(guess)
            print(guessed)
            print(f'You guessed "{guess.capitalize()}"')
            print(wordBoard)      
        elif guess not in word:
            if guess in guessed:
                print(f'--Incorrect!--\nYou have already guessed "{guess.capitalize()}"..\nTry again...')
                print(guessed)
            else:
                guessed.append(guess)
                turns = turns - 1
                print(f'The letter {guess} is Incorrect.. You have {turns} turns left')
                if turns == 0: print('GAMEOVER')
                turns == 0
        if win_check() ==1:
            print('Congratulations you won')
            break           
showBoard()
        # elif guess not in guessed:
        #     turn = turns -1
        #     print(f'Sorry that letter is not in the word.\n You have {turn} left')
        #     print(turn)
            
# def checkGuess(letter):
#     if letter in word_to_guess:
#         if letter in guessed:
#             print(f"You've already found the letter {letter} in the word. Please try again..")
#             return True
#         else:
#             guessed.append(letter)
#             print(f"You're Correct! Adding the {letter} to the puzzle..")
#             print(guessed)
#             return True
        
# def showBoard():
#     active = True
#     while active:
#         print(wordBoard)
#         user_guess = input(prompt)
#         checkGuess(user_guess)
#         active = True
# showBoard()