import Adafruit_BBIO.PWM as PWM 
import time,sys
BassTab = [1911,1702,1516,1431,1275,1136,1012]
class GroveSpeaker():
    def __init__(self,channel):
        self.channel = channel
    def Speaker_sound(self,note_index):
        PWM.set_frequency(self.channel, 2*note_index)
        PWM.set_duty_cycle(self.channel, 50) 
    def Speaker_enable(self,status = True):
        if status:
            PWM.start(self.channel,0)
        else:
            PWM.set_duty_cycle(self.channel, 0)
            PWM.stop(self.channel)
            PWM.cleanup()
def main():
    if len(sys.argv) < 2:
        print('Usage:please input PWM')
        sys.exit(1)
    if sys.argv[1] == 'PWM':
        speaker = GroveSpeaker("P2_1")
    speaker.Speaker_enable()
    for index in range(len(BassTab)):
        speaker.Speaker_sound(BassTab[index])
        time.sleep(1)
    speaker.Speaker_enable(False)  
if __name__=="__main__":
    main()