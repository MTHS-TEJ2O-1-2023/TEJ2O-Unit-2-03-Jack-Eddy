"""
Created by: Jack
Created on: Sep 2023
This module is a Micro:bit MicroPython program
"""

from microbit import *


display.clear()
sleep(1)

display.scroll("A rectangle has dimensions 5 cm & 3 cm")

display.scroll("Perimeter would be :" + str(5 * 2 + 3 * 2))

display.scroll("cm")

display.scroll("Area would be :" + str(5 * 3))

display.scroll("cm")
