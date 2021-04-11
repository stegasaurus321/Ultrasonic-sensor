import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
Trigger = 17
Echo = 18
GPIO.setup(Trigger, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)
try:
    GPIO.output(Trigger, 0)
    time.sleep(0.3)

    def pulse():
        GPIO.output(Trigger, 0)
        time.sleep(0.5)
        GPIO.output(Trigger, 1)
        time.sleep(0.00001)
        GPIO.output(Trigger, 0)

    def get_distance():
        start_time = time.time()
        while GPIO.input(Echo) == 0:
            start_time = time.time()
        while GPIO.input(Echo) == 1:
            stop_time = time.time()


        elapsed_time = stop_time - start_time
        distance = elapsed_time * 34326 / 2
        return distance

    while True:
        pulse()
        get_distance()
        print(str(get_distance()) + 'cm')
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    exit(0)
