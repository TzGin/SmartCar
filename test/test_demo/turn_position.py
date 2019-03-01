#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   turn_position.py
@Time    :   2019/03/01 17:25:27
@Author  :   Zijing Feng
'''

from ev3dev2.motor import *
import sys

m = Motor(OUTPUT_D)

while 1:
    p = m.position
    print(p, file = sys.stderr)
    # m.on_to_position(speed=15,position=35,block=False)


