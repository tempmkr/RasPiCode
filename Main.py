import RPi.GPIO as GPIO
import time

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
M = Move(25, 8, 24, 23, 27, 22)
S = Sense(26, 19, 13, 21, 20, 16)


'''
Your Script comes here
'''

print(S.distance_us())
M.straight(100)

time.sleep(3)
