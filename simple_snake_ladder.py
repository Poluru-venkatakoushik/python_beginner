from random import *
user_name=input("Enter your name")
user_name2=user_name.capitalize()
position=0
while(position<100):
        x=randint(1,6)
        if((position+x)==5):
            print("Your Dice says {0}".format(x))
            print("Your current position is {0}".format(position))
            position=69
            print("Congo!!You stepped up a ladder")
            print("Your current position is {0}".format(position))
        elif ((position+x)>100):
            continue
        else:
            position+=x
            print("Your Dice says {0}".format(x))
            print("Your current position is {0}".format(position))
print("Yay !! {0} you made it ".format(user_name2))