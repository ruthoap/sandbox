#!/usr/bin/env python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(40, GPIO.OUT)

try:
    while True:
        GPIO.output(40, GPIO.HIGH)
        GPIO.output(40, GPIO.LOW)
except KeyboardInterrupt:
    pass

GPIO.cleanup()

