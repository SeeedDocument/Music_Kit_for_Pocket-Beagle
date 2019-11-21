#!/usr/bin/env python
import time,sys
import smbus

# this device has two I2C addresses
DISPLAY_RGB_ADDR = 0x62 
DISPLAY_TEXT_ADDR = 0x3e
class GroveRgbLcd():
    def __init__(self,bus_num,rgb_addr = DISPLAY_RGB_ADDR,text_addr = DISPLAY_TEXT_ADDR):
        self.bus = smbus.SMBus(bus_num)
        self.rgb_addr = rgb_addr
        self.text_addr = text_addr
    # set backlight to (R,G,B) (values from 0..255 for each)
    def setRGB(self,r,g,b):
        self.bus.write_byte_data(self.rgb_addr,0,0)
        self.bus.write_byte_data(self.rgb_addr,1,0)
        self.bus.write_byte_data(self.rgb_addr,0x08,0xaa)
        self.bus.write_byte_data(self.rgb_addr,4,r)
        self.bus.write_byte_data(self.rgb_addr,3,g)
        self.bus.write_byte_data(self.rgb_addr,2,b)

    # send command to display (no need for external use)    
    def textCommand(self,cmd):
        self.bus.write_byte_data(self.text_addr,0x80,cmd)

    # set display text \n for second line(or auto wrap)     
    def setText(self,text):
        self.textCommand(0x01) # clear display
        time.sleep(.05)
        self.textCommand(0x08 | 0x04) # display on, no cursor
        self.textCommand(0x28) # 2 lines
        time.sleep(.05)
        count = 0
        row = 0
        for c in text:
            if c == '\n' or count == 16:
                count = 0
                row += 1
                if row == 2:
                    break
                self.textCommand(0xc0)
                if c == '\n':
                    continue
            count += 1
            self.bus.write_byte_data(self.text_addr,0x40,ord(c))

    # Update the display without erasing the display
    def setText_norefresh(self,text):
        self.textCommand(0x02) # return home
        time.sleep(.05)
        self.textCommand(0x08 | 0x04) # display on, no cursor
        self.textCommand(0x28) # 2 lines
        time.sleep(.05)
        count = 0
        row = 0
        while len(text) < 32: #clears the rest of the screen
            text += ' '
        for c in text:
            if c == '\n' or count == 16:
                count = 0
                row += 1
                if row == 2:
                    break
                self.textCommand(0xc0)
                if c == '\n':
                    continue
            count += 1
            self.bus.write_byte_data(self.text_addr,0x40,ord(c))
def main():
    if len(sys.argv) < 2:
        print('Usage:please input I2C1 or I2C2')
        sys.exit(1)
    if sys.argv[1] == 'I2C1':
        rgb_lcd = GroveRgbLcd(1)
    if sys.argv[1] == 'I2C2':
        rgb_lcd = GroveRgbLcd(2)
    rgb_lcd.setText("Hello world!\n")
    time.sleep(2)
    rgb_lcd.setText("Bye bye")
    time.sleep(2)
    rgb_lcd.setText(" ")
# example code
if __name__=="__main__":
    main()