from Deck import *
from Card import *
import time

class TriPeaks(object):

    #Smidur
    def __init__(self):
        #Stokkur leiksins
        self.deck = Deck(52)
        self.deck.setCards()
        self.deck.shuffleCards()
        
        #Spil sem eru i bordi
        self.board = Deck(0)
        #Spil sem eru i hrugu
        self.heap = Deck(0)
    
        #Breyta sem heldur utanum stig
        self.score = 0
    
        #Breyta sem byrjar ad taka tima
        self.start_time = time.time()
    
    #Segir hvort adgerd er logleg, skilar true ef satt annars false
    def isLegal(self, card):
        return self.heap.getNextCard(len(self.heap)) == card
    
    #Skrifar ut stodu spila a bordi
    def boardShow(self):
        raise Exception("Fall ekki tilbuid")

    #Tekur inn user input fra notenda
    def userInput(self):
        raise Exception("Fall ekki tilbuid")

    #Faerir spil ur bordi i hrugu
    def toHeap(self):
        self.heap.append(self.deck.pop())

    #Dregur spil ur stokk
    def drawCard(self):
        self.deck.pop()

    #Heldur utanum stig leiksins
    def score(self, points):
        self.score += points

    #Tekur tima leiksins
    def measureTime(self):
        return time.time() - self.start_time

    #Athugar hvort leikur se buinn, t.e.a.s. er buid ad vinna
    def hasWon(self):
        return (self.deck != 0 and self.board == 0)

def main():
    newGame = TriPeaks()

if __name__ == "__main__":
    sys.exit(main())