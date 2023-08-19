print('Welcome to treasure Island.\n')
print("Your Today mission is to find the hidden treasure.\n")
direction = input('You are at cross road. Where do you want to go? Type "left" and "right"\n')
if direction == "right":
    print("Entered into Crocodile Den. Life Over means Game over.\n")
else:
    path = input("You are taken to the lake. There is a island in the middle of the lake.\nType 'boat' to wait for the"
                 "boat.\nType 'swim' to swim to island.\n")
    if path == "swim":
        print("There are blue sharks here. Life....oohh....Game Over!!!!!!!\n")
    else:
        color = input("You are at the island. Enter 'red', 'blue' or 'yellow' for the password.\n")
        if color == 'red':
            print("Sorry! Bomb Alert. Had fun playing with you :)\n")
        elif color == 'blue':
            print("Aaaaaaaaaah. You! You! You are truly a winner. But password is incorrect. Bye:)\n")
        else:
            print(":(You won\n")
