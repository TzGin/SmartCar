/*
 * @Author: Zijing Feng 
 * @Date: 2018-12-18
 * @Last Modified by: Zijing Feng
 * @Last Modified time: 2019-01-10 21:02:46
 */
 
#!/usr/bin/env python3
"""
触摸传感器测试程序

需要更改的是第25行
第25行需要根据实际传感器插入主机的接口更改

更多细节参考https://python-ev3dev.readthedocs.io/en/ev3dev-stretch/sensors.html#touch-sensor
"""

import sys
sys.path.append(r"/home/robot/SmartCar-master/")
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor import *
from lib import debug_print

#主机与传感器建立连接
__sensor = TouchSensor(INPUT_1)

while 1:
    if __sensor.is_pressed:     #指示当前触摸传感器是否被按下的布尔值
        debug_print("Touched")
    else:
        debug_print("No touch")