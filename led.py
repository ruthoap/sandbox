#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup((29,33), GPIO.OUT)

try:
    while True:
        GPIO.output(29, GPIO.HIGH)
        GPIO.output(33, GPIO.LOW)
	sleep(0.5)
        GPIO.output(29, GPIO.LOW)
        GPIO.output(33, GPIO.HIGH)
	sleep(0.5)

except KeyboardInterrupt:
    pass

GPIO.cleanup()

