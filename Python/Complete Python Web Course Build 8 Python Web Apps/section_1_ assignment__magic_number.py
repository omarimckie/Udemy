#Create a variable that holds a "magic nmber" between 0 and 10
#Tell the user to pick a number between 0 and 10
#If the user pickes the "magic number", tell them they've won
#Else , tell them to run the program again

import random

magic_number = random.randint(0,10)

user_pick = input("Please enter a number between 0 and 10: ")
int_user_pick = int(user_pick)

if magic_number == int_user_pick:
    print("You have won!")
else:
    print("You didnt get it...the magic number was {}, please run the program again"
          .format(magic_number))