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
timeButtonState = False
print('starting to check Button pressed and print time in millseconds')
startTimeMilliSeconds = int(round(time.time() * 1000))
print('Start time = ',startTimeMilliSeconds)

# Infinete Loop
while True:
    # reset Button check
    print('checking if Time button is pushed')
    while timeButtonState == False:
        timeButtonState = GPIO.input(timeButton)
        #print(resetButtonState)
        if timeButtonState == True:
            print('Time Button Pressed')
            # Ask or the current time in Milliseconds
            currentMilliSeconds = int(round(time.time() * 1000))
            print('Button Pusshed at ',currentMilliSeconds)
            timeDifference = currentMilliSeconds - startTimeMilliSeconds
            print('Start to Button Pusshed difference = ',timeDifference)

            if timeDifference > 10000 :
                print('----------------- Times up ---------------')
                print('starting to check Button pressed and print time in millseconds')
                startTimeMilliSeconds = int(round(time.time() * 1000))
                print('Start time = ',startTimeMilliSeconds)

    sleep(.05)


    timeButtonState = False
