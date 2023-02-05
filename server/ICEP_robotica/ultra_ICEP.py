# File name: ultra_ICEP.py
# Description: Detection distance and tracking with ultrasonic
# Author: Irving
# Date: 2023/02/05
import RPi.GPIO as GPIO # General Purpose Input/Output library
import time             # python time library

Tr = 11 # Trigger pin
Ec = 8  # Echo pin

def checkdist():            # Define function
    #Setup trigger and Echo
    GPIO.setwarnings(False) # Ignore Raspberry warnings
    GPIO.setmode(GPIO.BCM)  # Setmode broadcom
    GPIO.setup(Tr, GPIO.OUT,initial=GPIO.LOW) # Configure Tr as output
    GPIO.setup(Ec, GPIO.IN) # Configure Ec as input

   #For loop to make 5 measures before give a result
    for i in range(5): # Remove invalid test results
        GPIO.output(Tr, GPIO.LOW) # Tr in low for 2us to stable
        time.sleep(0.000002)
        GPIO.output(Tr, GPIO.HIGH) # Send out an initial sound wave   
        time.sleep(0.000015) # Minimum time for trigger to send its 8 pulses
        GPIO.output(Tr, GPIO.LOW) 
        # Program execution is faster than sensor (40kHz vs 15us)
        while not GPIO.input(Ec): # By this time, waves haven't been sent, Ec = LOW
            pass
        # Once the pulses are sent, Ec = HIGH
        t1 = time.time()
        while GPIO.input(Ec): # Wait for the wave to come back
            pass
        t2 = time.time() # Once the wave arrives, Ec = LOW, exiting while loop
        dist = (t2-t1)*340/2

        if dist > 9 and i < 4: # 5 consecutive times are invalid data, return the last test data
            continue
        else:
            return (t2-t1)*340/2

if __name__ == '__main__':
    while True:
        distance = checkdist()*100
        print("%.2f cm" %distance)
        time.sleep(1)
