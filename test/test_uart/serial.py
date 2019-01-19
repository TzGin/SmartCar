#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   serial.py
@Time    :   2019/01/19 11:24:46
@Author  :   Zijing Feng
'''

import serial.Serial
import sys
sys.path.append(r"/home/robot/SmartCar-master/")
from lib import debug_print


s = Serial('/dev/ttyACM0', 9600)

while True:
    data = s.readline()
    print(data)
    debug_print(data, file=sys.stderr)