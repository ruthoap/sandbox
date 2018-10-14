#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)

pwm = GPIO.PWM(40, 1000) #1KHz

pwm.start(50) #50%

try:
    while True:
        sleep(0.1)

except KeyboardInterrupt:
    pass

pwm.stop()

GPIO.cleanup()

#pwm.ChangeFrequency()
#pwm.ChangeDutyCycle()
