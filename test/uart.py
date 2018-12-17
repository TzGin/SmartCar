#!/usr/bin/env python3 
import serial,sys

serial = serial.Serial('/dev/ttyACM0', 9600)

while True:
    data = serial.readline()
    print(data, file=sys.stderr)