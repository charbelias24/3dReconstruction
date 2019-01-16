import RPi.GPIO as GPIO
import time

class Led():
    """ Controlling an LED using a Raspberry Pi.

    The master/server will use this class to control the behavior
    of the Led based on the state of the program"""
    def __init__(self, led_pin):
        self.led_pin = led_pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.led_pin, GPIO.OUT)

    def __del__(self):
        GPIO.output(self.led_pin, False)

    def blink(self, delay, num_of_times):
        for state in (True, False) * int(num_of_times):
            GPIO.output(self.led_pin, state)
            time.sleep(delay)

    def turn_on(self):
        GPIO.output(self.led_pin, True)

    def turn_off(self):
        GPIO.output(self.led_pin, False)
