/*
 * @Author: Zijing Feng 
 * @Date: 2018-12-18
 * @Last Modified by:   Zijing Feng 
 * @Last Modified time: 2019-01-10 20:57:05 
 */
 
#!/usr/bin/env python3 
import serial,sys

serial = serial.Serial('/dev/ttyACM0', 9600)

while True:
    data = serial.readline()
    print(data, file=sys.stderr)