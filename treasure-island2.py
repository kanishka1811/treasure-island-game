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
print("Welcome to the Treasure Island!")
print("Your mission is to find the treasure")

choice1 = input('You\'re at a crossroad, where do you want to go? Type left" or "right."\n').lower()
if choice1 == "left":
    print('You\'ve come to a lake. There is an island in the middle of the lake.')
    choice2 = input(
        'Type "boat" to go by boat, type "swim" to swim across, type "helicopter" to wait for a helicopter\n').lower()
    if choice2 == "boat":
        print("Congratulations, you've arrived to the island unharmed!")
        print('There\'s a castle right infront of you. It has 3 gates.')
        choice3 = input(
            'Type "chocolate" to open the chocolate gate, "mango" to open the mango gate, "strawberry" to open the strawberry gate\n').lower()
        if choice3 == "chocolate":
            print("You find a room, but a river is flowing!")
            choice4 = input('How would you like to go? By "bridge" , "boat" or just "swim" ?\n')
            if choice4 == "boat":
                choice5 = input(
                    'You\'ve crossed this room unharmed! There are 2 gates, type "11" to open the 11 no gate and "14" to open the 14 no. gate\n').lower()
                if choice5 == "11":
                    choice6 = input(
                        'There\'s a pit, the key to the treasure box is inside. Type "shovel" to use a shovel to dig or "spade" to use a "spade".\n').lower()
                    if choice6 == "spade":
                        print("You've got the key no. 18, Remember the key!!")
                    else:
                        print("You've got the key no. 15, Remember the key!!")
                    print(
                        "You are at the last stage! You enter a room where you can see the treasure box. Select your moves carefully!")
                    print(
                        "The way towards the treasure box has stepping stones. Half of them will drown, and half will lead you the the treasure box")
                    choice7 = input(
                        'Press "even" to step on the even numbered stones and "odd" to step on the odd numbered stones\n').lower()
                    if choice7 == "odd":
                        choice8 = input(
                            'Congratulations, you\'ve got the treasure box! Now use the key you have, type the key number.\n').lower()
                        if choice8 == "18":
                            print("CONGRATULATIONS! YOU'VE FOUND THE TREASURE. YOU WIN")
                        elif choice8 == "15":
                            print("THIS IS THE WRONG KEY. YOU CAN'T OPEN THE TREASURE BOX. YOU'VE LOST!!")
                        else:
                            print("you have wrong key")
                    elif choice7 == "even":
                        print("The stepping stones are drowning! Game over!.")
                    else:
                        print("Wrong choice entered. Game over!.")

                else:
                    print("You fall into a pit. Game over!")


            elif choice4 == "swim":
                print("You've been attacked by crocodiles! Game Over.")

            elif choice4 == "bridge":
                print("The bridge is broken. You fall! Game over.")
            else:
                print("You've entered wrongly. Game over.")

        else:
            print("Wrong gate chosen. Game over.")

    elif choice2 == "helicopter":
        print("It is running out of fuel! It is about to crash. Game Over.")
    elif choice2 == "swim":
        print("You got attacked by an angry trout. Game over.")
    else:
        print("Wrong choice entered. Game over")

else:
    print("You fall into a pit. Game over!")
