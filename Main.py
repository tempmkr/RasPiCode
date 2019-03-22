import RPi.GPIO as GPIO
import time
from Tkinter import *


'''
Importing Modules or classe, if you wish to import more do so in the same manner
'''

from Move import Move
from Sense import Sense

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

'''
Setup the pins by calling the class and call methods on classes to execute something
'''
M = Move(8, 25, 24, 23, 27, 22)
S = Sense(26, 19, 13, 21, 20, 16)


'''
Your Script comes here
'''

root = Tk()
frame = Frame(root, width = 300, height = 250)

def key_input(event):
    key_press = event.keysym.lower()
    print(key_press)

    if key_press == "w":
        M.straight()

    elif key_press == "s":
        M.straight(60, False)

    elif key_press == "d":
        M.turn()

    elif key_press == "a":
        M.turn(60, False)

    elif key_press == "q":
        M.rotate(60, False)


    elif key_press == "e":
        M.rotate(60)

    elif key_press == "y":

        dist = S.distance_us()
        print("Distance L: ", dist[0])
        print("Distance M: ", dist[1])
        print("Distance R: ", dist[2])

    elif key_press == "space":
        M.stop()

    else:
        pass

root.bind_all("<Key>",key_input)
frame.pack()
root.mainloop()



GPIO.cleanup()



#print(S.distance_us())
#M.straight(100)

#time.sleep(3)
