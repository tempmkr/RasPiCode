import RPi.GPIO as GPIO
import time

'''
Importing Modules or classe, if you wish to import more do so in the same manner
'''

from .Move import Move
from .Sense import Sense

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

'''
Setup the pins by calling the class and call methods on classes to execute something
'''
M = Move(pwm_l, pwm_r, dir_l1, dir_l2, dir_r1, dir_r2)
S = Sense(echo_l, echo_m, echo_r, trig_l, trig_m, trig_)

'''
Your Script comes here
'''
M.straight(100)
S.distance()

