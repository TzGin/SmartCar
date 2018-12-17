#!/usr/bin/env python3
"""
陀螺仪传感器测试程序

需要更改的是第18行
第18行需要根据实际传感器插入主机的接口更改

更多细节参考https://python-ev3dev.readthedocs.io/en/ev3dev-stretch/sensors.html#gyro-sensor
"""

import sys
sys.path.append(r"/home/robot/SmartCar-master/")
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sensor import *
from lib import debug_print

#主机与传感器建立连接
__sensor = GyroSensor(INPUT_1)

#设置传感器的运行模式为测量角度和转速
__sensor.MODE_GYRO_G_A

while 1:
    debug_print(__sensor.rate_and_angle)    #输出传感器设置模式之后旋转的角度和当前旋转的速率