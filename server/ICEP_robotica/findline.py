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
forward_speed = 70
right_speed = 100
left_speed = 100
back_speed = 100

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(line_pin_right,GPIO.IN)
    GPIO.setup(line_pin_middle,GPIO.IN)
    GPIO.setup(line_pin_left,GPIO.IN)
    #motor.setup()

def run():
    last_side = 'no'
    
    while True:
        "Read sensors"
        status_right = GPIO.input(line_pin_right)
        status_middle = GPIO.input(line_pin_middle)
        status_left = GPIO.input(line_pin_left)
        #print('L%d   M%d   R%d'%(status_left,status_middle,status_right))
    
        "Decide direction"
        if status_middle == 1:
            move.move(forward_speed, 'forward', 'no', 1)
            last_side = 'no'

        elif status_left == 1:
            move.move(left_speed, 'forward', 'right', 0.6)
            last_side = 'left'

        elif status_right == 1:
            move.move(right_speed, 'forward', 'left', 0.6)
            last_side = 'right'

        else:
            move.move(back_speed, 'backward', last_side, 0.6)

    
if __name__ == '__main__':
    try:
        time.sleep(5) # Delay to disconect eth cable
        setup()
        move.setup()
        run()

    except KeyboardInterrupt:
        move.destroy()
