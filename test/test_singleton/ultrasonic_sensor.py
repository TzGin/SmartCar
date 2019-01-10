/*
 * @Author: Zijing Feng 
 * @Date: 2018-12-18
 * @Last Modified by: Zijing Feng
 * @Last Modified time: 2019-01-10 21:03:01
 */
 
#!/usr/bin/env python3
"""
超声波传感器测试程序

需要更改的是第26行
第26行需要根据实际传感器插入主机的接口更改

乐高超声波传感器有效距离为3-255cm
更多细节参考https://python-ev3dev.readthedocs.io/en/ev3dev-stretch/sensors.html#touch-sensor
"""

import sys
sys.path.append(r"/home/robot/SmartCar-master/")
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor import *
from lib import debug_print

#主机与传感器建立连接
__sensor = UltrasonicSensor(INPUT_1)

#设置传感器测量模式
#以厘米为单位连续测量
__sensor.MODE_US_DIST_CM

while 1:
        debug_print(__sensor.distance_centimeters)  #读取传感器测量结果