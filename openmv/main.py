import sensor
import image
import time
from pyb import UART
uart = UART(3, 115200)
ball =(37, 66, -25, 14, 20, 84)
ROI = (0, 100, 160, 15)
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(100)
sensor.set_auto_whitebal(False)
sensor.set_auto_gain(False)
sensor.set_auto_exposure(False , exposure_us = int (0.25*sensor.get_exposure_us()))
clock = time.clock()
def find_max(blobs):
    max_size=0;
    for blob in blobs:
        temp_size = blob.w() * blob.h()
        if temp_size > max_size:
            max_blob = blob
            max_size = temp_size
    return max_blob
while(True):
    clock.tick()
    img = sensor.snapshot()
    img.draw_rectangle(ROI)
    blobs = img.find_blobs([ball], roi = ROI, merge = True)
    if blobs:
        max_blob = find_max(blobs)
        img.draw_cross(max_blob.cx(),max_blob.cy())
        print(max_blob.cx())
    else:
        print(-1)
