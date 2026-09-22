import RPi.GPIO as GPIO
import time
import threading

# should install  sudo apt-get install python3-rpi.gpio

ON_STATUS = GPIO.HIGH
OFF_STATUS = GPIO.LOW


GPIO_00 = 0
GPIO_01 = 1

GPIO_02 = 2
GPIO_03 = 3

GPIO_04 = 4
GPIO_05 = 5

GPIO_06 = 6
GPIO_07 = 7

GPIO_08 = 8
GPIO_09 = 9

GPIO_10 = 10
GPIO_11 = 11

GPIO_12 = 12
GPIO_13 = 13

GPIO_14 = 14
GPIO_15 = 15

GPIO_16 = 16
GPIO_17 = 17

GPIO_18 = 18
GPIO_19 = 19

GPIO_20 = 20
GPIO_21 = 21

GPIO_22 = 22
GPIO_23 = 23

GPIO_24 = 24
GPIO_25 = 25

GPIO_26 = 26
GPIO_27 = 27

flag = False

def initialize_gpio():
    global flag
    if flag:
        return
    GPIO.setmode(GPIO.BCM)  # Broadcom pin-numbering scheme
 #   GPIO.setup(GPIO_00, GPIO.OUT)
    GPIO.setup(GPIO_01, GPIO.OUT)
    GPIO.setup(GPIO_02, GPIO.OUT)
    GPIO.setup(GPIO_03, GPIO.OUT)
    GPIO.setup(GPIO_04, GPIO.OUT)
    GPIO.setup(GPIO_05, GPIO.OUT)
    GPIO.setup(GPIO_06, GPIO.OUT)
    GPIO.setup(GPIO_07, GPIO.OUT)
    GPIO.setup(GPIO_08, GPIO.OUT)
    GPIO.setup(GPIO_09, GPIO.OUT)
    GPIO.setup(GPIO_10, GPIO.OUT)
    GPIO.setup(GPIO_11, GPIO.OUT)
    GPIO.setup(GPIO_12, GPIO.OUT)
    GPIO.setup(GPIO_13, GPIO.OUT)
    GPIO.setup(GPIO_14, GPIO.OUT)
    GPIO.setup(GPIO_15, GPIO.OUT)
    GPIO.setup(GPIO_16, GPIO.OUT)
    GPIO.setup(GPIO_17, GPIO.OUT)
    GPIO.setup(GPIO_18, GPIO.OUT)
    GPIO.setup(GPIO_19, GPIO.OUT)
    GPIO.setup(GPIO_20, GPIO.OUT)
    GPIO.setup(GPIO_21, GPIO.OUT)
    GPIO.setup(GPIO_22, GPIO.OUT)
    GPIO.setup(GPIO_23, GPIO.OUT)
    GPIO.setup(GPIO_24, GPIO.OUT)
    GPIO.setup(GPIO_25, GPIO.OUT)
    GPIO.setup(GPIO_26, GPIO.OUT)
  # GPIO.setup(GPIO_27, GPIO.OUT)
    flag =True

def reset_status(gpio):
    GPIO.output(gpio, OFF_STATUS)


def set_status(gpio,delay):
    initialize_gpio()
    if gpio > 26 or gpio < 0:
        print("Invalid pin!")
        return

    GPIO.output(gpio, ON_STATUS)
    delay_seconds = delay / 1000
    timer = threading.Timer(delay_seconds, lambda: reset_status(gpio))
    timer.start()


# def test_blink():
#     for i in range(1, 10):
#         set_status(i, 'ON')
# 	    # time.sleep(1)
#         set_status(i,'OFF')
    
#     GPIO.cleanup()


# if __name__ == '__main__':
#     initialize_gpio()
#     test_blink()