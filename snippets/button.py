#!/usr/bin/env /home/pi/.virtualenvs/pincho/bin/python
import RPi.GPIO as gpio
from time import sleep
from button.models import ChairState

BUTTON = 17
DELTA = 0.5  # seconds between reads
MIN_CHANGE = 5  # seconds to accept value

gpio.setmode(gpio.BCM)
gpio.setup(BUTTON, gpio.IN)


def send_value(sit, acc):
    if sit:
        print ('User is on the chair for {}s.'.format(acc))
    else:
        print ('User left the chair for {}s'.format(acc))
    ChairState.objects.create(in_use=sit, acc=acc)

try:

    value = True
    old_value = value
    change_acc = 0
    acc = 0

    while True:
        input_value = gpio.input(BUTTON)

        # Store an acc when detecting the same input
        if input_value == value:
            change_acc += DELTA
        else:
            change_acc = 0
            value = input_value

        # do not use values that are not persistent from more than MIN_CHANGE
        if change_acc >= MIN_CHANGE and not (change_acc % MIN_CHANGE):
            # accumulate the time on the same state
            if value != old_value:
                acc = 0
            acc += MIN_CHANGE
            # Notify value with accumulated time
            send_value(not value, acc)
            old_value = value

        sleep(DELTA)

except KeyboardInterrupt:
    print('Close program and clean GPIO')
    gpio.cleanup()
