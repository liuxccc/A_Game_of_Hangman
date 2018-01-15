#A game of Hangman
def setUp():
    """shows instructions, reads file,and returns a list of words from the english dictionary"""
    print(60*'*' +'''\n\t\tWelcome to Hangman!\n\t
    I have selected a word from an english dictionary. \n\t
    I will first show you the length of the secret word\n\t
    as a series of dashes.\n\t
    Your task is to guess the secret word one letter at a time.\n\t
    If you guess a correct letter I will show you the guessed\n\t
    letter(s) in the correct position.\n
    You can only make 8 wrong guesses before you are hanged\n
    \t\tGood luck\n''' + 60*'*')
    infile=open('dictionary.txt')
    l=infile.readlines()# list of words from which to choose
    infile.close()
    return(l)

def playRound(wr,g):
    """ It allows user to guess one letter. If right,places letter in correct positions in current guess string g, and shows current guess to user
    if not, increments w, number of wrongs. Returns current number of wrongs and current guess string"""
    print('You have ' + str(8 - wr) + ' possible wrong guesses left.\n')
    newLetter = input('Please guess a letter of the secret word:\n')
    glist = list(g)#need to make changes to current guess string so need a mutable version of it
    if newLetter in secretWord:
        for j in range (0,len(secretWord)):
            if secretWord[j]==newLetter:
               glist[j] = newLetter
        g = ''.join(glist)#reassemble the guess as a string
        print('Your letter is indeed present in the secret word: ' +  ' '.join(g)+'\n')
    else:
        wr += 1
        print('Sorry, there are no ' + newLetter + ' in the secret word. Try again.\n')
    return(wr,g)

def endRound(wr, w,l):
    """determines whether user guessed secret word, in which case updates s[0], or failed after w=8 attempts, in s\which case it updates s[1]"""
    if wr == 8:
            l += 1
            print('Sorry, you have lost this game.\n\nThe secret word was '+secretWord +'\n')#minor violation of encapsulation
    else:
        w +=1
        print(15*'*' + 'You got it!' + 15*'*')
    return(w,l)

def askIfMore():
    """ask user if s/he wants to play another round of the game"""
    while True:
        more = input('Would you like to play another round?(y/n)')
        if more[0].upper() == 'Y' or more[0].upper()=='N':
            return more[0].upper()
        else:
            continue
        
def printStats(w,l):
    """prints final statistics"""
    wGames='games'
    lGames = 'games'
    if w == 1:
        wGames = 'game'
    if l ==1:
        lGames = 'game'
    print('''Thank you for playing with us!\nYou have won {} {} and lost {} {}.\nGoodbye.'''.format(w,wGames,l,lGames))
          
import random
words=setUp()#list of words from which to choose
won, lost = 0,0 #accumulators for games won, and lost
while True:
    wrongs=0 # accumulator for wrong guesses
    secretWord = random.choice(words)[:-1]#eliminates '\n' at the end of each line
    print(secretWord) #for testing purposes
    guess= len(secretWord)*'_'
    print('Secret Word:' + ' '.join(guess))
    while wrongs < 8 and guess != secretWord:
        wrongs, guess = playRound(wrongs, guess)
    won, lost = endRound(wrongs,won,lost)
    if askIfMore()== 'N':
        break
printStats(won, lost)
    
