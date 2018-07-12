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

# Import rospy and start publishers
rospy.init_node("termite_serial_node")
serial_port = rospy.get_param("serial", "/dev/termite")
debug = rospy.get_param("debug", False)

# Start data collecting through serial port
# Open serial port
ser = serial.Serial(serial_port, 115200)
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

# Log information
rospy.loginfo("Termite succesfuly connected. Publishing data")

# Create termite msg
termite_msg = Termite()

# Create termite publisher
termite_pub = rospy.Publisher("/termite", Termite, queue_size=1)

# Start main loop
ctrl_c = True
def shutdownhook():
  ctrl_c = False

rospy.on_shutdown(shutdownhook)

while ctrl_c:
  # Read data from serial
  data = ser.readline()
  data = data.split(',')

  # Pass if there is not enough data coming from serial port
  if len(data) < 10:
    pass

  # We send the message otherwise
  else:
    # We get the header
    termite_msg.header.frame_id = "termite_link"
    termite_msg.header.stamp = rospy.Time.now()

    # We populate the rest of the variables
    termite_msg.acceleration.x = float(data[0])
    termite_msg.acceleration.y = float(data[1])
    termite_msg.acceleration.z = float(data[2])
    termite_msg.temperature = float(data[3])
    termite_msg.light = float(data[4])
    termite_msg.humidity = float(data[5])
    termite_msg.proximity = float(data[6])
    termite_msg.pressure = float(data[7])
    termite_msg.altitude = float(data[8])
    termite_msg.dewpoint = float(data[9])

    # In case it is version 1.1
    if len(data) > 10:
      termite_msg.rgb.x = float(data[10])
      termite_msg.rgb.y = float(data[11])
      termite_msg.rgb.z = float(data[12])

    termite_pub.publish(termite_msg)

    if debug:
      print(data)  

  ser.flush()

# Close the serial port
ser.close()
