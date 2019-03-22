import RPi.GPIO as GPIO


#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

class Move:

    def __init__(self, pwm_l, pwm_r, dir_l1, dir_l2, dir_r1, dir_r2,f = 1000):

        '''
        engine gpio pins are set and initialized.
        Pass in the pins:
        pwm_l(ENA), pwm_r(ENB), dir_l1(IN1), dir_l2(IN2), dir_r1(IN3), dir_r2(IN4), pwm frequency default = 1000Hz

        '''

        self.pwm_l = pwm_l
        self.pwm_r = pwm_r

        self.dir_l1 = dir_l1
        self.dir_l2 = dir_l2
        self.dir_r1 = dir_r1
        self.dir_l1 = dir_r2

        self.f = f

        GPIO.setup(pwm_l, GPIO.OUT)
        GPIO.setup(pwm_r, GPIO.OUT)

        GPIO.setup(dir_l1, GPIO.OUT)
        GPIO.setup(dir_l2, GPIO.OUT)

        GPIO.setup(dir_r1, GPIO.OUT)
        GPIO.setup(dir_r2, GPIO.OUT)

        p_r = GPIO.PWM(pwm_l, f)
        p_l = GPIO.PWM(pwm_r, f)


    def straight(self,speed, forward = True):

        '''

        :param speed: Speed in percent
        :param forward: default = forward, enter False for backwards

        '''

        GPIO.output(self.dir_l1, not forward)
        GPIO.output(self.dir_l2, forward)

        GPIO.output(dir_b1, not forward)
        GPIO.output(dir_b2, forward)

        self.pwm_l.start(self.speed)
        self.pwm_r.start(self.speed)

    def rotate(self, speed, right = True):
        '''

        :param speed: Speed in percent
        :param right: default = right, enter False for left
        '''

        GPIO.output(self.dir_l1, right)
        GPIO.output(self.dir_l2, not right)

        GPIO.output(self.dir_b1, not right)
        GPIO.output(self.dir_b2, right)

        self.pwm_l.start(self.speed)
        self.pwm_r.start(self.speed)


    def turn(self, speed_diff):

        '''

        :param speed__diff: Speed difference between left and right

        '''

        pass



    def stop(self):
        self.p_r.stop()
        self.p_l.stop()
