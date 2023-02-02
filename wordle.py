"""
Wordle
Chris Stankus
"""
import random
import linecache

class Wordle:
    '''
    Starts game of wordle
    Initializes the word to guess and game parameters
    Starts the game
    '''
    def __init__(self):
        self.numGuesses = 0
        self.numGuessAllowed = 6
        self.numCorrect = 0
        self.result = ["_","_","_","_","_"]
        self.word = self.getWord()
        self.play()

    """
    Returns a random word from wordbank.txt
    """
    def getWord(self):
        with open(r"wordbank.txt", 'r') as fp:
            for count, line in enumerate(fp):
                pass
        count += 1
        lineNum = random.randint(1, count)
        #print(lineNum)
        word = linecache.getline(r"wordbank.txt", lineNum)
        print(word)
        return word

    """
    Plays Wordle
    Main function for the program
    """
    def play(self):
        #limit number of rounds to allowed
        prevGuess = []
        for i in range(self.numGuessAllowed):
            #Get User Guess
            guess = self.makeGuess()
            self.numCorrect = 0
            self.result = ["_","_","_","_","_"]
            for i in range(len(guess)):
                if guess[i] == self.word[i]:
                    self.numCorrect += 1
                    self.result[i] = self.word[i]
            
            print("-----------------------------")
            prevGuess.append(self.getGuessResult())
            self.getPrevGuesses(prevGuess)

            #Win Condition
            if self.numCorrect == 5:
                self.endCondition(1)

        #Lose Condition
        self.endCondition(2)

    """
    Prints out a list of previos guesses
    Input: list of values to print
    """
    def getPrevGuesses(self, guessList):
        for i in guessList:
            print(i)

    """
    Condition For end of game
    input = 1 - win, 2 - lose
    displays message, calls play again
    """
    def endCondition(self, condition):
        if condition == 1:
            print("You Won in " + str(self.numGuesses) + " guesses!")
            self.playAgain()
        if condition == 2:
            print("You Lose, ran out of attempts")
            self.playAgain()

    """
    Gets User Input for 5 Letter Word
    Checks if word is in wordbank
    """
    def makeGuess(self):
        userIn = ""
        while True:
            userIn = input("Make a guess:")

            #DEBUG ENTRY - ENDS PROGRAM
            if userIn == "l":
                exit()

            fp = open(r"wordbank.txt", 'r')
            words = fp.read()
            if userIn in words:
                self.numGuesses += 1
                return userIn
            else:
                print("Enter Valid Word")

    """
    Returns a string of self.result[]
    """
    def getGuessResult(self):
        result = ""
        for i in self.result:
            result = result + i
        return result

    """
    Gets user input and either resets the game or ends the game
    """
    def playAgain(self):
        #get user input
        userChoice = "x"
        while True:
            userChoice = input("Would you like to play again? Y | N \n")
            userChoice = userChoice.upper()
            if userChoice == 'Y':
                print("Reseting and playing again")
                self.resetGame()
            if userChoice == 'N':
                print("Thanks for playing!")
                exit()

    """
    Starts the game over
    """
    def resetGame(self):
        self.__init__()
                
game = Wordle()