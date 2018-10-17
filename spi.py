#!/usr/bin/env python

import spidev
import time

spi = spidev.SpiDev()
spi.open(0,0)

try:
    while True:
        res = spi.xfer2([0x00])
        print(res[0])
        time.sleep(1)

except KeyboardInterrupt:
    pass

