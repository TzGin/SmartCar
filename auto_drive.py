#!/usr/bin/env python3
import serial
import sys
from ev3dev2.motor import *

s = serial.Serial('/dev/ttyACM0', 115200)

r_motor = Motor(OUTPUT_B)
l_motor = Motor(OUTPUT_A)
m_motor = Motor(OUTPUT_D)

T = 0
KP = 15
KD = 0.01
last_error = 0
derivative = 0

def limit_speed(speed):
    s = speed
    if s > 90:
        s = 90
    elif s < -90:
        s = -90
    return s

while 1:
    data = s.readline().decode('utf-8')
    try:
        if data.isnumeric:
            s.flushInput()

        print(data, file = sys.stderr)
        if int(data) > 0 and data.isnumeric:
            t = -0.625 * int(data) + 50
            error = T - t
            derivative = error - last_error
            speed = KP * error + KD * derivative   
            last_error = error 
            
            print(limit_speed(speed), file = sys.stderr)
            m_motor.on_to_position(speed=limit_speed(speed), position=t, brake=False, block=False)
            l_motor.on(speed=-10, brake=False, block=False)
            r_motor.on(speed=-10, brake=False, block=False)   
            
        else:
            l_motor.on(speed=0)
            r_motor.on(speed=0)

    except ValueError:
        pass
       