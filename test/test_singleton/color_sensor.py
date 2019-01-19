#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   color_sensor.py
@Time    :   2019/01/19 11:22:34
@Author  :   Zijing Feng

颜色传感器测试程序

需要更改的是第22行
第22行需要根据实际传感器插入主机的接口更改

更多细节参考https://ev3dev-lang.readthedocs.io/projects/python-ev3dev/en/ev3dev-stretch/sensors.html?highlight=Sensor#color-sensor
'''

import sys
sys.path.append(r"/home/robot/SmartCar-master/")
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import *

#主机与传感器建立连接
__sensor = ColorSensor(INPUT_1)

#获得颜色传感器反射光的值
ColorSensor().mode = 'COL-REFLECT'

while 1:
    debug_print(ColorSensor.value)

#ColorSensor().value()  reflected_light_intensity 反射光亮度 单位%
