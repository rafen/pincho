#!/usr/bin/env python
from time import sleep
from RPi import GPIO

BUTTON = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN)

def down(channel):
    print ('down')

def up(channel):
    print ('Up')

GPIO.add_event_detect(BUTTON, GPIO.RISING, callback=up, bouncetime=1000)
GPIO.add_event_detect(BUTTON, GPIO.FALLING, callback=down, bouncetime=1000)

try:
    while True:
       sleep(1)
except Exception:
    print ('Exit')
finally:
    GPIO.remove_event_detect(BUTTON)
