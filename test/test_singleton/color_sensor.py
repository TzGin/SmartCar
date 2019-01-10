/*
 * @Author: Xulei Cheng 
 * @Date: 2019-01-10 18:29 
 * @Last Modified by: Zijing Feng
 * @Last Modified time: 2019-01-10 21:00:33
 */

#!/usr/bin/env python3
"""
颜色传感器测试程序

需要更改的是第24行
第24行需要根据实际传感器插入主机的接口更改

更多细节参考https://ev3dev-lang.readthedocs.io/projects/python-ev3dev/en/ev3dev-stretch/sensors.html?highlight=Sensor#color-sensor
"""

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
