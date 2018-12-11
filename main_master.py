# This is for the master(server) RPi

import cv2
import time
import os
import RPi.GPIO as GPIO

button = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def main():
    while True:
        if GPIO.input(button):
            os.system("/usr/bin/python server_test3.py")
            break
        time.sleep(0.01)

if __name__=='__main__':
    main()
