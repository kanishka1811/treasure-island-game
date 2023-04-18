print("Welcome to the Treasure Island!")
print(" Your mission is to find the treasure")
print('''
                                  -|             |-
         -|                  [-_-_-_-_-_-_-_-]                  |-
         [-_-_-_-_-]          |             |          [-_-_-_-_-]
          | o   o |           [  0   0   0  ]           | o   o |
           |     |    -|       |           |       |-    |     |
           |     |_-___-___-___-|         |-___-___-___-_|     |
           |  o  ]              [    0    ]              [  o  |
           |     ]   o   o   o  [ _______ ]  o   o   o   [     | ----__________
_____----- |     ]              [ ||||||| ]              [     |
           |     ]              [ ||||||| ]              [     |
       _-_-|_____]--------------[_|||||||_]--------------[_____|-_-_
      ( (__________------------_____________-------------_________) )
''')

choice1 = input('You\'re at a crossroad, where do you want to go? Type left" or "right."').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake.Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game over.")
        elif choice3 == "yellow":
            print("You've found the treasure. You win!")
        elif choice3 == "blue":
            print("It's a room full of rocks. Game over.")
        else:
            print("You chose a door that doesn't exist. Game over.")
    else:
        print("You got attacked an angry trout. Game over")
else:
    print("You fell into a hole. Game over")
