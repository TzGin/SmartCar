#!/usr/bin/env python3
"""
    测试EV3大型伺服电机速度程序

    注意马达对应的输出端口号
    通过改变 left_speed 和 right_speed 从而改变马达的速度
    左右速度相等 ---> 直行
    左右存在速度差 ---> 转弯
    速度取负则电机反转
    如需测试EV3中型伺服电机则将第15,20,25行的注释去掉即可
"""

from ev3dev.ev3 import *

#马达与主机连接
__right_motor = LargeMotor(OUTPUT_A)
__left_motor = LargeMotor(OUTPUT_B)
# __medium_motor = MediumMotor(OUTPUT_C)

#设定马达的速度
left_speed = 200
right_speed = 200
#medium_speed = 200

while 1:
    __right_motor.run_forever(speed_sp = right_speed)
    __left_motor.run_forever(speed_sp = left_speed)
    # __medium_motor.run_forever(speed_sp = medium_speed)
