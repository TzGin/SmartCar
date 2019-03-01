#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   tacho_motor.py
@Time    :   2019/01/19 11:15:37
@Author  :   Zijing Feng

转速马达测试程序

需要更改的是第25，28行
第27行需要根据实际马达插入主机的接口更改
第30行speed指的是最大速度的百分比，可以加负号改变转向，测试达不到最大速度是正常的情况

由于内置PID，马达无法恒速运行
更多细节参考https://python-ev3dev.readthedocs.io/en/ev3dev-stretch/motors.html#tacho-motor-motor
'''

import sys
sys.path.append(r"/home/robot/SmartCar-master/")
from ev3dev2.motor import *
from lib import debug_print


#主机与马达建立连接
__motor = Motor(OUTPUT_D)

while 1:
    __motor.on(speed=30, brake=False, block=False) #马达以大约最大速度的30%运行
    debug_print(__motor.speed)  #输出马达的当前速度
    debug_print(__motor.state)  #输出马达的当前状态

#on方法中block参数默认是False，若改为True和上述写法效果一样，马达一直在循环运行但是on之后的语句不会执行
#__motor.on(speed=30, brake=False, block=True)