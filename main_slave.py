# This is for the master(server) RPi

import time
import os
import RPi.GPIO as GPIO

button = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def main():
    while True:
        if GPIO.input(button):
	    time.sleep(1)
            os.system("/usr/bin/python client_test3.py")
            break
        time.sleep(0.01)

if __name__=='__main__':
    main()
