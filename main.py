#imports

import random

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


#Cards
cards = {
  "spaAce": """   _____
                 |A .  |
                 | /.\ |
                 |(_._)|
                 |  |  |
                 |____V|""",
  "diaAce": ""
}





print("""
Do you know how to play poker?
Type "y" for yes and "n" for no
""")

choice = input("")
choice = choice.lower()
if choice == "n":
  print()

