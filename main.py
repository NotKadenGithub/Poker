#imports

import random
from db import cardImages

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





#Tutorial

print("""
Do you know how to play poker?
Type "y" for yes and "n" for no
""")

choice = input("")
choice = choice.lower()
loopTutorial = True
while loopTutorial == True:
  if choice == "n":
    print()
    loopTutorial = False
  elif choice == "y":
    print()
    loopTutorial = False
  else:
    print("Invalid Input")


#Main code

deck = ["spaAce","spa2","spa3","spa4","spa5","spa6","spa7","spa8","spa9","spa10","spaJ","spaQ","spaK","clubAce","club2","club3","club4","club5","club6","club7","club8","club9","club10","clubJ","clubK","clubQ","heaAce","hea2","hea3","hea4","hea5","hea6","hea7","hea8","hea9","hea10","heaJ","heaQ","heaK","diaAce","dia2","dia3","dia4","dia5","dia6","dia7","dia8","dia9","dia10","diaJ","diaQ","diaK"]

usersHand = []

pool = []


def removeCards(amount, deckToAdd):
  for i in range(0,amount):
    randomCard = random.randint(0, len(deck) - 1)
    deckToAdd.append(deck[randomCard])
    del deck[randomCard]

