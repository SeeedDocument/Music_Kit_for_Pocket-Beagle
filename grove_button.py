#!/usr/bin/env python
import time,sys
import Adafruit_BBIO.GPIO as GPIO

class GroveButton:
    def __init__(self, pin):
        self.__pin = pin
        GPIO.setup(self.__pin, GPIO.IN)
    def read_buttun(self):
        return GPIO.input(self.__pin)
def main():
    if len(sys.argv) < 2:
        print('Usage:please input A0,A2 or PWM')
        sys.exit(1)
    if sys.argv[1] == 'A2':
        PIN = "P2_24"
    if sys.argv[1] == 'A0':
        PIN = "P1_31"
    if sys.argv[1] == 'PWM':
        PIN = "P2_1"
    button = GroveButton(PIN)
    while True:
        time.sleep(1)
        if button.read_buttun():
            print('Button is pressed')
        else :
            print('Button is released')        
if __name__ == "__main__":
    main()