

word = 'python'
guessed = []
wordBoard = ['_']*len(word)
turns = 5
prompt = 'Guess a letter: '

def showBoard():
    print(" ".join(wordBoard))
    # for ch in wordBoard:
    #     print(ch, end=" ")
    # print()
def checkGuess(guess):
    i = -1
    for x in range(word.count(guess)):
    # if guess in word:
        i = word.find(guess,i+1)
        wordBoard[i]=guess
    return guess in word

def isBoardSolved():
    for i in range(0, len(wordBoard)):
        if wordBoard[i] == '_':
            return False
    return True

while turns > 0:
    showBoard()
    guess = input(prompt)
    if guess in guessed:
        print(f'--Incorrect!--\nYou have already guessed "{guess.capitalize()}"..\nTry again...')
    elif checkGuess(guess):
        guessed.append(guess)
        print(f"You're Correct! Adding the letter {guess} to the puzzle..")    
    else:
        turns = turns - 1
        print(f'{guess.capitalize()} is not Incorrect! you have {turns} left.')
    if isBoardSolved() == True:
        print(f'\n***Congratulations you won!!***')
        break
    if turns == 0:
        print(f'\n____GAMEOVER!!____')
        break  
    
