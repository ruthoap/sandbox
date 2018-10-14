#!/usr/bin/env python

import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.wait_for_edge(40, GPIO.FALLING)

def cb(pin):
    print(time.time(), pin)

GPIO.add_event_detect(40,GPIO.FALLING, callback=cb, bouncetime=100)

try:
    while True:
        time.sleep(0.05)
except KeyboardInterrupt:
    pass

GPIO.cleanup()

