#imports

import random
import time
from db import cardImages
from db2 import cards



print("""
 /$$$$$$$           /$$                          
| $$__  $$         | $$                          
| $$  \ $$ /$$$$$$ | $$   /$$  /$$$$$$   /$$$$$$ 
| $$$$$$$//$$__  $$| $$  /$$/ /$$__  $$ /$$__  $$
| $$____/| $$  \ $$| $$$$$$/ | $$$$$$$$| $$  \__/
| $$     | $$  | $$| $$_  $$ | $$_____/| $$      
| $$     |  $$$$$$/| $$ \  $$|  $$$$$$$| $$      
|__/      \______/ |__/  \__/ \_______/|__/
""")


#Main code

#Lists
deck = ["spaAce","spa2","spa3","spa4","spa5","spa6","spa7","spa8","spa9","spa10","spaJ","spaQ","spaK","clubAce","club2","club3","club4","club5","club6","club7","club8","club9","club10","clubJ","clubK","clubQ","heaAce","hea2","hea3","hea4","hea5","hea6","hea7","hea8","hea9","hea10","heaJ","heaQ","heaK","diaAce","dia2","dia3","dia4","dia5","dia6","dia7","dia8","dia9","dia10","diaJ","diaQ","diaK"]


usersHand = []

computersHand = []

pool = []

#Functions

def textWrite(text):
	for a in text:
		print(a, end="")
		time.sleep(0.1)

def printCards(cardsList):
  for card in cardsList:
    print(cardImages.get(card), end="  ")

def removeCards(amount, deckToAdd):
  for i in range(0,amount):
    randomCard = random.randint(0, len(deck) - 1)
    deckToAdd.append(deck[randomCard])
    del deck[randomCard]
    
#Tutorial

textWrite("""
Do you know how to play poker?
Type "y" for yes and "n" for no
""")

choice = input("")
choice = choice.lower()
loopTutorial = True
while loopTutorial == True:
  if choice == "n":
    textWrite()
    loopTutorial = False
  elif choice == "y":
    textWrite("Let's begin.")
    
    loopTutorial = False
  else:
    textWrite("Invalid Input")

#Tutorial

textWrite("""
Do you know how to play poker?
Type "y" for yes and "n" for no
""")

choice = input("")
choice = choice.lower()
loopTutorial = True
while loopTutorial == True:
  if choice == "n":
    textWrite()
    loopTutorial = False
  elif choice == "y":
    textWrite("Let's begin.")
    loopTutorial = False
  else:
    textWrite("Invalid Input")


#Game
removeCards(2, computersHand)
removeCards(2, usersHand)

gameActive = True
while gameActive == True:
  printCards(usersHand) 
  gameActive = False

textWrite("Yo it's Mr Worldwide.") 

#( ͡° ͜ʖ ͡°)textwre