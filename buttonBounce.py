# Button & Time
# 3.3v = 1,17, 5.0v =2,4 GND = 6,9,14,20,25,30,34,39
# I/O = 3,5,7,8,10,11,12,13,15,16,18,19,21,22,23,24,
# More I/O =26,27,28,29,31,32,33,35,36,37,38,40

import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setmode(GPIO.BOARD)
timeButton = 18
gotTimeLED = 5



GPIO.setup(gotTimeLED, GPIO.OUT)

GPIO.setup(timeButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


# Your Code Here

# init states
buttonEvent = False
buttonCount = 0

print('checking hiow many time the button was pushed')
# Infinete Loop
while True:
    for i in range(100):
        buttonCurrentState = GPIO.input(timeButton)
        #buttonLastState = buttonCurrentState
        #buttonCurrentState = GPIO.input(timeButton)
        buttonLastState = GPIO.input(timeButton)
        if buttonCurrentState != buttonLastState :
            buttonCount = buttonCount +1

    if buttonCount :
        print('Button Bounce Count = ',buttonCount)
        buttonCount=0
    


