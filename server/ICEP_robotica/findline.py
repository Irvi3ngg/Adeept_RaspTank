#!/usr/bin/python3
# File name   : findline.py
# Description : line tracking 
# Website     : www.gewbot.com
# Author      : William
# Date        : 2019/08/28
import RPi.GPIO as GPIO
import time
import move

line_pin_right = 20
line_pin_middle = 16
line_pin_left = 19

"Speed cts"
forward_speed = 50
right_speed = 100
left_speed = 100
back_speed = 90

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(line_pin_right,GPIO.IN)
    GPIO.setup(line_pin_middle,GPIO.IN)
    GPIO.setup(line_pin_left,GPIO.IN)
    #motor.setup()

def run():
    "Read sensors"
    status_right = GPIO.input(line_pin_right)
    status_middle = GPIO.input(line_pin_middle)
    status_left = GPIO.input(line_pin_left)
    #print('R%d   M%d   L%d'%(status_right,status_middle,status_left))
    "Decide direction"
    if status_middle == 1:
        move.move(forward_speed, 'forward', 'no', 1)

    elif status_left == 1:
        move.move(left_speed, 'forward', 'right', 0.6)
        last_side = 'left'

    elif status_right == 1:
        move.move(right_speed, 'forward', 'left', 0.6)
        last_side = 'right'

    elif last_side == 'right' and status_middle == 0 and status_left == 0 and status_right == 0:
        move.move(back_speed, 'backward', 'right', 0.6)

    elif last_side == 'left' and status_middle == 0 and status_left == 0 and status_right == 0:
        move.move(back_speed, 'backward', 'left', 0.6)

if __name__ == '__main__':
    try:
        time.sleep(10) # Delay to disconect eth cable
        setup()
        move.setup()
        while 1:
            run()
        pass
    except KeyboardInterrupt:
        move.destroy()
