#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   serial_to_ev3.py
@Time    :   2019/01/19 11:24:46
@Author  :   Zijing Feng
'''

import sys
sys.path.append(r"/home/robot/SmartCar-master/")
import serial
from lib import debug_print

s = serial.Serial('/dev/ttyACM0', 9600)

while True:
    data = s.readline()
    debug_print(data)