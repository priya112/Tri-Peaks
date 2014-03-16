from Deck import *
from Card import *
import time

class TriPeaks(object):

    #Smidur
    def __init__(self):

        self.boardRows = 4
        self.boardCols = 10
        
        #Stokkur leiksins
        self.deck = Deck(52)
        self.deck.shuffleCards()
        
        #2D array of cards in the board, initialized as None
        self.board = [[None for _ in range(self.boardCols)] for _ in range(self.boardRows)]
        self.dealToBoard()
        
        #Cards in the heap
        self.heap = [self.deck.cards.pop()]
    
        #Breyta sem heldur utan um stig
        self.score = 0
    
        #Breyta sem byrjar ad taka tima
        self.start_time = time.time()

    # Pre:  self.deck contains a deck of cards
    # Post: 28 cards from the deck have been dealt to the board
    # Run:  TriPeaks.dealToBoard()
    def dealToBoard(self):
        ''' Deals cards from the deck to the board '''
        for i in range(0,self.boardCols-1,3):
            self.board[0][i] = self.deck.cards.pop()
        for i in [i for i in range(self.boardCols-2) if i%3 is not 2]:
            self.board[1][i] = self.deck.cards.pop()
        for i in range(self.boardCols-1):
            self.board[2][i] = self.deck.cards.pop()  
        for i in range(self.boardCols):
            self.board[3][i] = self.deck.cards.pop()
            

    # Pre:  row and col are integers
    # Post: returns true if the card at self.board[row][col] is movable
    # Run:  TriPeaks.isMovable(row,col)
    def isMovable(self, row, col):
        ''' Checks if a card in the board is movable '''
        return (row == self.boardRows-1) or (self.board[row+1][col] is None and self.board[row+1][col+1] is None)
    
    # Pre:  card is a Card object
    # Post: returns True if card has a value one higher or lower than the
    #       top card on the heap
    # Run:  TriPeaks.isLegal(card)
    def isLegal(self, card):
        ''' Checks if a card move is legal '''
        return abs(self.heap.getNextCard().value - card.value) == 1        
    
    # Post: the board has been printed to the console
    # Run:  TriPeaks.printBoard()
    def printBoard(self):
        ''' Prints the board to the console '''
        print "Cards in board: \n"
        for i in range(self.boardRows):
            for j in range(self.boardCols):
                if (self.board[i][j] is None):
                    print " "*(3-i),
                elif (self.isMovable(i,j)):
                    print " #  ",
                else:
                    print " "*(3-i), self.board[i][j],
            print ''

        print '\nCard in heap: '
        print self.heap[-1]

    # Pre:
    # Post:
    # Run:
    def getUserInput(self):
        ''' Handles user inputs '''
        raise Exception("Fall ekki tilbuid")

    # Pre:  self.deck contains at least one Card object, self.heap is a
    #       list of Card objects
    # Post: the next card in the deck is moved on top of the heap
    # Run:  TriPeaks.toHeap()
    def toHeap(self):
        ''' Moves the next card from the deck to the heap '''
        self.heap.append(self.deck.pop())

    # Pre:  self.deck contains at least one Card object
    # Post: the next card in the deck has been removed and is returned
    # Run:  TriPeaks.drawCard()
    def drawCard(self):
        ''' Draws a card from the deck '''
        self.deck.pop()

    # Pre:  self.score is an integer
    # Post: self.score has been increased by points
    # Run:  self.addScore(points)
    def addScore(self, points):
        ''' Increases the game score by points '''
        self.score += points

    # Pre:  self.start_time is a time object
    # Post: returns the time elapsed since self.start_time
    # Run:  TriPeaks.elapsedTime
    def elapsedTime(self):
        ''' Measures the time elapsed since the game started '''
        return time.time() - self.start_time

    # Post: returns true if the game is won, false otherwise
    # Run:  TriPeaks.hasWon()
    def hasWon(self):
        ''' Checks if the game is won '''
        return all(b is None for b in self.board)

    # Post: returns true if there are no more moves possible, false otherwise
    # Run:  TriPeaks.hasLost()
    def hasLost(self):
        ''' Checks if the game is lost '''
        return len(self.deck) == 0

    # Post: the game rules have been printed to the terminal
    # Run:  TriPeaks.showRules()
    def showRules(self):
        ''' Prints the game rules to the terminal'''
        print """
        TRI-PEAKS RULES:
        ----------------
        The object of Tri-Peaks is to transfer all the cards from the board
        to the heap.

        You can move a card from the board that has a value one lower or
        higher than the top card on the heap if it is not covered by
        another card.

        If you run out of moves you can move a card from the deck to the
        heap and try again to move a card from the board.
        """ 

    # Post: runs the game logic
    # Run:  TriPeaks.playGame()
    def playGame(self):
        ''' Plays the game '''
        print 'Playing game...'
        self.printBoard()
        
if __name__ == "__main__":
    game = TriPeaks()
    game.showRules()
    game.playGame()
