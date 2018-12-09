# This is for the master(server) RPi

import cv2
import time
import os
import numpy as np
import RPi.GPIO as GPIO
from undistort_image import undistort_img
from picamera import PiCamera

button = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def main():
    if GPIO.input(button):
        os.system("python server_test2.py")
        

if __name__=='__main__':
    main()
