wordToGuess = 'python'
# word = iter(word_to_guess)
# print(word)
wordBoard = ['_']*len(wordToGuess)
guessed = []
active = True
prompt = 'Guess a Letter: '

def checkGuess(letter, wordToGuess, wordBoard):
    index = -2
    while index != -1:
        if letter in wordToGuess:
            index = wordToGuess.find(letter)
            removed_character='*'
            wordToGuess = wordToGuess[:index] + removed_character + wordToGuess[index+1:]
            wordBoard[index] = letter
        else:
            index = -1
    return (wordToGuess, wordBoard)

def win_check():
    for i in range(0,len(wordBoard)):
        if wordBoard[i] == '_':
            return -1
    return 1 

num_turns = 5
for i in range(0, num_turns):
    letter = input(prompt)
    if letter in wordToGuess:
        wordToGuess, wordBoard = checkGuess(letter, wordToGuess, wordBoard)
    else:
        print('Sorry that letter is not in the word.')
       
    #check if the player guess the word
    if win_check() == 1:
        print('Congratulations you won')
        break
       
    print('you have'+ str(num_turns - i)+' turns left.')
    print()   
        

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






    