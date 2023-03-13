# File name: avoid.py
# Description: Detect obstacles and avoid collisions
# Author: Irving (irvi3nggasimov@gmail.com)
# Date: 2023/02/07

import time, ultra_ICEP, move
"Set speed"
speed_set_forward = 60
speed_set_turn = 100
dist = 20
delay = 1.05

"Setup function"
def setuplibs():
    ultra_ICEP.setup()
    move.setup()

"Create function to avoid obstacles"
def avoid():
    while True:
        distance = ultra_ICEP.checkdist()*100 # Measure distance
        time.sleep(0.05)

        if distance > dist:   # Move forward as long as distance > 25cm
            move.move(speed_set_forward, 'forward', 'no', 0.8)

        elif distance > 0 and distance <= dist: # Stop when distance <= 25cm
            move.motorStop()
            time.sleep(0.1)
            move.move(speed_set_turn, 'no', 'right', 0.8) # Move robot to the left 90deg
            time.sleep(delay)
            move.motorStop()
            distance = ultra_ICEP.checkdist()*100 # Measure distance
            time.sleep(0.05)

            "If distance on the left is < 25cm, check distance on the right side"
            if distance > 0 and distance <= dist:
                move.move(speed_set_turn, 'no', 'left', 0.8)
                time.sleep(delay*2) # Rotate 180deg
                move.motorStop()
                distance = ultra_ICEP.checkdist()*100
                time.sleep(0.05)
                
                if distance > 0 and distance <= dist : # There is a closed area, come back
                    move.move(speed_set_turn, 'no', 'left', 0.8)
                    time.sleep(delay)
                    move.motorStop()
                    time.sleep(0.05)


if __name__ == '__main__':
    try:
        setuplibs()
        time.sleep(5) # Delay time to disconect eth cable
        avoid()
        move.destroy()
    except KeyboardInterrupt:
        move.destroy()
