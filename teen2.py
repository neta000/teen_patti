# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 00:25:02 2020

@author: nitesh
"""
import random

class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color
    def display_value(self):
        return self.value
    def display_color(self):
        return self.color
    def fun(self):
        return Card
    
    
colors =['heart','diamonds','spades','clubs']

deck = [Card(value, color) for value in range(2,15) for color in colors]

for i in range(0,52):
    print(" {} {}   ".format(deck[i].display_value(),deck[i].display_color()))
random.shuffle(deck)


class Player:
    def __init__(self):
        self.cards = [deck.pop(),deck.pop(),deck.pop()]
    def display_cards(self):
        return self.cards

play = [Player(),Player(),Player(),Player(),Player(),Player()]
print("--------------------------------------")
for player in play:
    cards = player.display_cards()
    for card in cards:
        print(" {}  {} ".format(card.display_color(),card.display_value()))
        
    print("--------------------------------------")
    
    
# function for sequence
def sequence_checker(c1,c2,c3):
    seq = [c1,c2,c3]
    seq.sort()
    print(seq)
    if(seq[0]==12 and seq[1]==13 and seq[2]==14):
        return 15
    elif(seq[0]==2 and seq[1]==3 and seq[2]==14):
        return 14
    elif(seq[2]-seq[1] == 1 and seq[1]-seq[0] == 1):
        return seq[2]
    else:
        return 0
        
    
    
# function for same color    
def same_color(cc1,cc2,cc3):
    if(cc1==cc2==cc3):
        return True
    else:
        return False
    
# function for two same card
def two_same(c1,c2,c3):
    if c1==c2:
        return c1
    elif c2==c3:
        return c2
    elif c1==c3:
        return c1
    else:
        return 0
    
# function to return highest card
def highest_card(c1,c2,c3):
    if(c1>c2 and c1>c3):
        return c1
    elif(c2>c3):
        return c2
    else:
        return c3

# function to find winner
def win(play):
    player_score = []
    for player in play:
        cards = player.display_cards()
        c1 = cards[0].display_value()
        c2 = cards[1].display_value()
        c3 = cards[2].display_value()
        cc1 = cards[0].display_color()
        cc2 = cards[1].display_color()
        cc3 = cards[2].display_color()

        sequence = sequence_checker(c1,c2,c3)
        print("               {}---sequence".format(sequence))
        number = two_same(c1,c2,c3)
        print("               {}---two card same".format(number))
        similar = same_color(cc1, cc2, cc3)
        print("               {}---same color".format(similar))
# three same card
        if(c1==c2==c3):
            player_score.append(1000000 + c1) 
# same color with sequence
        elif similar:
            if sequence >0:
                player_score.append(100000+sequence)
            elif (number >0):
                player_score.append(1100+number)
            else:
                player_score.append(highest_card(c1, c2, c3)+1000)
# with sequence
        elif sequence > 0:
            player_score.append(10000+sequence)


# two same card
        elif (number >0):
            player_score.append(100+ number)

# highest card
        else:
            player_score.append(highest_card(c1, c2, c3))    
    return player_score

win = win(play)
print(win)


        
    
     
     
     
     
  
     
     
     
     
  

