print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("Which direction are you heading?\nR or L.\n")
direction = direction.lower()
if direction == "l":
  decision = input("You've chosen the left direction, what do you wanna do now?\nSwim or Wait.\n")
  decision = decision.lower()
  if decision == "wait":
    door = input("You chose to wait.\nThree coloured doors have appeared\nPick your desired colour\nRed - Yellow - Blue.\n")
    door = door.lower()
    if door == "red":
      print("You got burned by fire like Satan\nBetter luck next time buddy.")
    elif door == "yellow":
      print("OMG YOU DID IT!\nYOU FOUND THE TREASURE")
    elif door == "blue":
      print("You think you did it, but you end up being a good looking snack for the beasts.")
    else:
      print("You lost the game for being too stupid, I told you to pick a colour, good luck escaping the implosion like ocean gate.")
  else:
    print("You got attacked by a Trout\nThat's depressing not gonna lie.")
    
else:
  print("You fell into a hole.\nWell that's it I guess, hm?.")
    