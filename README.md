# TerMITes ROS

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c778ce67e4cc468e8ce6452c2c6902a4)](https://app.codacy.com/app/yagoliz/termites_ros?utm_source=github.com&utm_medium=referral&utm_content=yagoliz/termites_ros&utm_campaign=Badge_Grade_Dashboard)

This package gets the data sent from terMITes and sends it to the ROS system.

---
## What are terMITes
TerMITes are embedded devices created by Carson Smuts at [MIT Media Lab](https://www.media.mit.edu/projects/termites/overview/)

---
## How to run the node

You will have to install the serial library for Python:
```bash
user@machine:~$ sudo pip install pyserial
```

Create a catkin workspace and paste the folder:
```bash
user@machine:~$ mkdir -p catkin_ws/src && cd catkin_ws/src
user@machine:~/catkin_ws/src$ git clone https://github.com/yagoliz/termites_ros.git
user@machine:~/catkin_ws/src$ cd .. && catkin_make
```

If it compiles without errors, open a terminal and start a roscore:
```bash
user@machine:~$ roscore
```

On another terminal run:
```bash
user@machine:~$ rosrun termites_ros termite_control.py
```

To check if it's working, you can open a third terminal and run:
```bash
user@machine:~$ rostopic echo /termite
```

## Notes to open the serial

The [hardware_rule](hardware_rule/hardwareRule.md) folder contains intructions on ow to set the udev rules for the terMITe