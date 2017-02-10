#!/usr/bin/env python

"""
My first python script for RaspberryPi!
"""

import time
from datetime import datetime
import sys
import scrollphat

scrollphat.clear()
scrollphat.set_brightness(20)

WIDTH = 11
HEIGHT = 5

COORDS = {
    0:[{'x': 5, 'y': 1}, {'x': 5, 'y': 0}],
    1:[{'x': 6, 'y': 1}, {'x': 7, 'y': 1}, {'x': 8, 'y': 0}],
    2:[{'x': 6, 'y': 2}, {'x': 7, 'y': 1}, {'x': 8, 'y': 1}, {'x': 9, 'y': 1}, {'x': 10, 'y': 0}],
    3:[{'x': 6, 'y': 2}, {'x': 7, 'y': 2}, {'x': 8, 'y': 2}, {'x': 9, 'y': 2}, {'x': 10, 'y': 2}],
    4:[{'x': 6, 'y': 2}, {'x': 7, 'y': 3}, {'x': 8, 'y': 3}, {'x': 9, 'y': 3}, {'x': 10, 'y': 4}],
    5:[{'x': 6, 'y': 3}, {'x': 7, 'y': 3}, {'x': 8, 'y': 4}],
}

def round_down(num, divisor):
    """ Rounds a number down to the nearest divisor """
    return num - (num % divisor)

def mirror(coord):
    """ Flips the coordinates along the 12/6 axis """
    return {'x': (WIDTH - 1) - coord['x'], 'y': (HEIGHT - 1) - coord['y']}

SIX_TO_ELEVEN = {}

for c in COORDS:
    SIX_TO_ELEVEN[c + 6] = map(mirror, COORDS[c])

COORDS.update(SIX_TO_ELEVEN)

MIDDLE = True

while True:
    try:
        HOUR = COORDS[datetime.now().hour - 12 if datetime.now().hour > 12 else datetime.now().hour]
        MINUTE = COORDS[round_down(datetime.now().minute, 5) / 5]
        SECOND = COORDS[round_down(datetime.now().second, 5) / 5]
        scrollphat.clear()
        for h in HOUR:
            if h != HOUR[-1]:
                scrollphat.set_pixel(h['x'], h['y'], True)
        for m in MINUTE:
            scrollphat.set_pixel(m['x'], m['y'], True)
        scrollphat.set_pixel(SECOND[-1]['x'], SECOND[-1]['y'], True)
        scrollphat.set_pixel(5, 2, MIDDLE)
        MIDDLE = not MIDDLE
        scrollphat.update()
        time.sleep(1)
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)

