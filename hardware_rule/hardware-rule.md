# How to set udev rules for terMITes

[Hardware/Udev](https://wiki.debian.org/udev) rules are a great tool to organize your peripherals, since they allow you to give them unique symbolic names.

In the case of the terMITes, while in this folder, open a terminal and run:
```bash
user@machine:~$ chmod +x setRule.sh
user@machine:~$ ./setRule.sh
```

Once this is done, you can chech that the udev rule was properly loaded by typing in the terminal:
```bash
user@machine:~$ ls /dev/termite
/dev/termite (in blue color)
```
