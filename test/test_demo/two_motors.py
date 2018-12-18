#!/usr/bin/env python3
"""
马达组测试程序

需要更改的是第14行
第14行需要根据实际传感器插入主机的接口更改

更多细节参考https://python-ev3dev.readthedocs.io/en/ev3dev-stretch/motors.html#move-tank
"""

from ev3dev2.motor import *

#主机与马达组建立连接
__tank = MoveTank(OUTPUT_A, OUTPUT_B)

#直行3s
__tank.on_for_seconds(left_speed=30, right_speed=30, seconds=3, brake=False)
#右轮旋转360°
__tank.on_for_degrees(left_speed=0, right_speed=30, degrees=360, brake=False)
#直行
__tank.on(left_speed=50, right_speed=50)
