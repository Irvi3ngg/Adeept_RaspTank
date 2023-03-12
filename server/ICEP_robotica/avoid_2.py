'''
File name: avoid_2.py
Description: Detect obstacles according to competition
Author: Irving Juarez
Date: 6/Mar/2023
'''

import time, ultra_ICEP, move

"Set speed"
speed_forward = 60
speed_turn = 100

"Setup function"
def setuplibs():
    ultra_ICEP.setup()
    move.setup()

"Constants"
right = 1
left = 0
dist = 20

"Create function to avoid"
def avoid():
    turns = {0: 'right', 1: 'right', 2: 'left', 3: 'left'}
    cont = 0
    while True:
        distance = ultra_ICEP.checkdist()*100
        time.sleep(0.1)

        if distance > dist:
            move.move(speed_forward, 'forward', 'no', 0.8)
        
        elif distance <= dist:
            move.motorStop()
            direct = turns[cont]
            time.sleep(0.4)
            while distance <= 120:
                move.move(speed_turn, 'no', direct, 0.8)
                distance = ultra_ICEP.checkdist()*100
                time.sleep(0.1)
            cont += 1

if __name__ == "__main__":
    try:
        setuplibs()
        time.sleep(4)
        avoid()
        move.destroy()
    except KeyboardInterrupt:
        move.destroy()
