import time,sys
import Adafruit_BBIO.GPIO as GPIO

usleep = lambda x: time.sleep(x / 1000000.0)

_TIMEOUT1 = 1000
_TIMEOUT2 = 10000

class GroveUltrasonicRanger():
    def __init__(self, pin):
        self.__pin = pin

    def _get_distance(self):
        GPIO.cleanup()
        GPIO.setup(self.__pin, GPIO.OUT)
        GPIO.output(self.__pin,GPIO.LOW)
        usleep(2)
        GPIO.output(self.__pin,GPIO.HIGH)
        usleep(5)
        # time.sleep(20 / 1000000.0)
        # GPIO.output(self.__pin,GPIO.LOW)
        # print("configured succse!!!")
        GPIO.setup(self.__pin, GPIO.IN)
        t0 = time.time()
        count = 0
        while count < _TIMEOUT1:
            if GPIO.input(self.__pin):
                # print("when breaked the count is")
                # print(count)
                break
            count += 1
        else : 
            print("time out")
            return None
        t1 = time.time()
        count = 0
        while count < _TIMEOUT2:
            if not GPIO.input(self.__pin):
                break
            count += 1
        if count >= _TIMEOUT2:
            return None

        t2 = time.time()

        dt = int((t1 - t0) * 1000000)
        if dt > 530:
            return None

        distance = ((t2 - t1) * 1000000 / 29 / 2)    # cm

        return distance

    def get_distance(self):
        while True:
            dist = self._get_distance()
            if dist:
                return dist


Grove = GroveUltrasonicRanger


def main():
    if len(sys.argv) < 2:
        print('Usage:please input A0 A2 or PWM')
        sys.exit(1)
    if sys.argv[1] == 'A2':
        sonar = GroveUltrasonicRanger("P2_24")
    if sys.argv[1] == 'A0':
        sonar = GroveUltrasonicRanger("P1_31")
    if sys.argv[1] == 'PWM':
        sonar = GroveUltrasonicRanger("P2_1")
    print('Detecting distance...')
    while True:
        print('{} cm'.format(sonar.get_distance()))
        time.sleep(1)

if __name__ == '__main__':
    main()
