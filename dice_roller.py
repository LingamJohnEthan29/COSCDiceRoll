import random
import time 
def dice_roll():
    roll = random.randint(1,6)
    print("Rolling")
    t = 3
    while t > 0:
        print( "... "+str(t))
        t -=1
        time.sleep(1)
    print("Number gotten, ",roll)
input("Press enter to roll")
dice_roll()
