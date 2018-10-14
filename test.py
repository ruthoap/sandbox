#!/usr/bin/env python

import serial
from time import sleep

ser = serial.Serial('/dev/ttyAMA0',9600)

ser.write("aaaaa") 

ser.close()

