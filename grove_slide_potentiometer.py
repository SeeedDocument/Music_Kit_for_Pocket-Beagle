#!/usr/bin/env python
import time
import sys
import Adafruit_BBIO.ADC as ADC
class GroveSlidePotentioMeter:
    def __init__(self,pin):
        self.__pin = pin
        ADC.setup()
    def get_data(self):
        return ADC.read_raw(self.__pin)
def main():
    if len(sys.argv) < 2:
        print('Usage:please input A0 A2 or A5(3.3V)')
        sys.exit(1)
    if sys.argv[1] == 'A2':
        PIN = "AIN2"
    if sys.argv[1] == 'A0':
        PIN = "AIN0"
    if sys.argv[1] == 'A5':  
        PIN = "AIN5"
    slidepotentiometer = GroveSlidePotentioMeter(PIN)
    while True:
        print('SlidePotentioMeter Value: {}'.format(slidepotentiometer.get_data()))
        time.sleep(.2)

if __name__ == '__main__':
    main()