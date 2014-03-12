from Deck import *
from Card import *

class TriPeaks(object):

    #Smidur
    def __init__(self):
        deck = Deck()
        board = Deck()
        heap = Deck()
    
    #Segir hvort adgerd er logleg
    def isLegal(self):
        raise Exception("Fall ekki tilbuid")

    #Skrifar ut stodu spila a bordi
    def boardShow(self):
        raise Exception("Fall ekki tilbuid")

    #Tekur inn user input fra notenda
    def userInput(self):
        raise Exception("Fall ekki tilbuid")

    #Faerir spil ur bordi i hrugu
    def toHeap(self):
        raise Exception("Fall ekki tilbuid")

    #Dregur spil ur stokk
    def drawCard(self):
        raise Exception("Fall ekki tilbuid")

    #Heldur utanum stig leiksins
    def score(self):
        raise Exception("Fall ekki tilbuid")

    #Tekur tima leiksins
    def measureTime(self):
        raise Exception("Fall ekki tilbuid")

    #Athugar hvort leikur se buinn, t.e.a.s. er buid ad vinna eda tapa
    def hasWon(self):
        raise Exception("Fall ekki tilbuid")