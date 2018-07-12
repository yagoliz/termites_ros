#!/usr/bin/env python

# Regular libraries
import sys

# Regular Python libraries
import rospy
import time
# ROS libraries
from termite_msgs.msg import Termite
import serial

# TerMITes data flow
# [X, Y, X]: [0, 1, 2]
# Temperature: 3
# Light: 4
# Humidity: 5
# Proximity: 6
# Pressure: 7
# Altitude: 8
# DewPoint: 9
# [R, G, B]: [10, 11, 12]

# Start data collecting through serial port
# Open serial port
ser = serial.Serial("/dev/termite", 115200)

ser.write(b'CMD')
time.sleep(2.0)
ser.flush()

ser.write(b'TMT')
time.sleep(1.0)
data = ser.readline()
print(data) 

# Send commands to terMITe to ouput data in CSV mode
# Stop sending data
ser.write(b'CMD')
time.sleep(2.0)
# Change mode to CSV
ser.write(b'CSV')
time.sleep(1.0)
# Start sending data
ser.write(b'EXT')
time.sleep(1.0)

# while True:
#   # Read data from serial
#   data = ser.readline()
#   data = data.split(',')

#   print(data)

# # Close the serial port
ser.close()
