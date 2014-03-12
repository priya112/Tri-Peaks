'''
Created on 28.1.2014

@author: Gudrun
'''
import random
from Card import *

# Class for a deck of cards
class Deck(object):
    
    # Creates a new deck with 'noCards' number of cards
    def __init__(self, noCards):
        self.cards = []
        self.numCards = noCards
        self.setCards()

    # Called when a Deck object is printed
    def __repr__(self):
        return str(self.cards)
        
    # Initializes the cards in the deck
    def setCards(self):
        self.cards = []
        for i in range(1,(self.numCards/4 + 1)):
            self.cards.append(Card('H',i))
            self.cards.append(Card('S',i))
            self.cards.append(Card('T',i))
            self.cards.append(Card('L',i))
            
    # Shuffles the order of the cards in the deck
    def shuffleCards(self):
        random.shuffle(self.cards)
        
    # Returns card number 'i' in the deck 
    def getNextCard(self, i):
        return self.cards[i]
    
    # Adds the card 'card' to the deck
    def addCard(self, card):
        self.cards.append(card)
        
    # Removes the card 'card' from the deck
    def removeCard(self, card):
        self.cards.remove(card)
        
    # Removes two cards between card number 'prevCardNo' and 'prevCardNo+3' if they have the same sort
    def removeBetween(self, prevCardNo):
        if (len(self.cards) < prevCardNo+3 or len(self.cards) < 4):
            print 'Card index out of range'
            return
        prevCardSort = self.cards[prevCardNo].sort
        laterCardSort = self.cards[prevCardNo+3].sort
        if (prevCardSort != laterCardSort):
            print 'The cards are not the same sort!'
            return
        self.removeCard(self.cards[prevCardNo+1])
        self.removeCard(self.cards[prevCardNo+1])
        
    # Removes four cards from card number 'prevCardNo' to 'prevCardNo+3' if they have the same value
    def removeFour(self, firstCardNo):
        if (len(self.cards) < firstCardNo+3):
            print 'Card index out of range'
            return
        firstCardVal = self.cards[firstCardNo].value
        fourthCardVal = self.cards[firstCardNo+3].value
        if (firstCardVal != fourthCardVal):
            print 'The cards do not have the same value'
            return
        for _ in range(4):
            self.removeCard(self.cards[firstCardNo])

    
        
