#!/usr/bin/env python3
import serial
import sys
import json
from lib import debug_print
from ev3dev2.motor import *

s = serial.Serial('/dev/ttyACM0', 115200)

# Connect Motors
r_motor = Motor(OUTPUT_A)
l_motor = Motor(OUTPUT_C)

GAIN = 5

while True:
    data = s.readline().decode('utf-8')
    try:
        if data:
            json_data = json.loads(data)
            s.flushInput()
    except ValueError:
        pass
    else:
        r_speed = GAIN*(json_data[1] + json_data[0])
        l_speed = GAIN*(json_data[1] - json_data[0])
        debug_print(l_speed,r_speed)
        if r_speed in range(-1050, 1050) and l_speed in range(-1050, 1050):
            r_motor.run_forever(speed_sp=r_speed)
            l_motor.run_forever(speed_sp=l_speed)
        else:
            r_motor.run_forever(speed_sp=0)
            l_motor.run_forever(speed_sp=0)
