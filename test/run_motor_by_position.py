#!/usr/bin/env python3
"""
    测试EV3中型伺服电机位置程序

    EV3伺服电机有两种工作形式，一种只设定速度，另一种通过设定速度及位置使电机定速定量的运行
    每次运行程序时电机的位置会复位到0
    可以调用run_to_abs_pos或者run_to_rel_pos控制电机运行到绝对位置或者相对位置
    这里的绝对位置和相对位置都是在每次复位到0的基础上的绝对和相对概念
    比如说在循环中反复执行run_to_abs_pos和run_to_rel_pos
    run_to_abs_pos 在第一次运行到position_sp的之后不管多少次循环都不会转动了，并且此时电机依旧有力维持电机保持在这个position，此时可能会产生抖动
    run_to_rel_pos 每经过一次循环都会转动一个position
    如有疑惑可自行查看定义
"""

from ev3dev.ev3 import *

#马达与主机连接
__medium_motor = LargeMotor(OUTPUT_A)
__medium_motor2 = LargeMotor(OUTPUT_B)

#设定马达的速度
medium_speed = 400

#设定马达运行到的位置
position_sp = 250


# print(__medium_motor.position, file = sys.stderr)
# print(__medium_motor2.position,file = sys.stderr)
# time.sleep(3)
# __medium_motor.run_to_abs_pos(speed_sp = medium_speed, position_sp = position_sp)
# __medium_motor2.run_to_abs_pos(speed_sp = medium_speed, position_sp = position_sp)
# time.sleep(1)
# print(__medium_motor.position, file = sys.stderr)
# print(__medium_motor2.position,file = sys.stderr)

# time.sleep(3)
# __medium_motor.run_to_abs_pos(speed_sp = medium_speed, position_sp = position_sp)
# __medium_motor2.run_to_abs_pos(speed_sp = medium_speed, position_sp = position_sp)
# time.sleep(1)
# print(__medium_motor.position, file = sys.stderr)
# print(__medium_motor2.position,file = sys.stderr)

while 1:
    __medium_motor.run_to_abs_pos(speed_sp = medium_speed, position_sp = position_sp)
    __medium_motor2.run_to_abs_pos(speed_sp = medium_speed, position_sp = position_sp)