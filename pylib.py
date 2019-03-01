import sensor
import image
from pyb import UART


def set_baud_rate(baud_rate=115200):
    uart = UART(3, baud_rate)


def init_camera(pixformat=sensor.RGB565, framesize=sensor.QQVGA, skip_frames=100, auto_whitebal=False, auto_gain=False):
    sensor.reset()
    sensor.set_pixformat(pixformat)
    sensor.set_framesize(framesize)
    sensor.skip_frames(skip_frames)
    sensor.set_auto_whitebal(auto_whitebal)
    sensor.set_auto_gain(auto_gain)


def pid(image, target_x, target_y, KP=0, KI=0, KD=0):
    error_x = target_x - image.cx()
    error_y = target_y - image.cy()

    integral_x = 0
    derivative_x = 0
    last_error_x = 0

    integral_y = 0
    derivative_y = 0
    last_error_y = 0

    integral_x = integral_x + error_x
    derivative_x = error_x - last_error_x

    integral_y = integral_y + error_y
    derivative_y = error_y - last_error_y

    speed_x = KP * error_x + KI * integral_x + KD * derivative_x
    speed_y = KP * error_y + KI * integral_y + KD * derivative_y

    r_speed = speed_y + speed_x
    l_speed = speed_y - speed_x
