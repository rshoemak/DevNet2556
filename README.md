## DevNet 2556 - Python on IOS-XE

Welcome to the Python on IOS-XE introductory lab.  This lab is built to be used on a local laptop running a Vagrant install of IOS-XE.  That version of IOS-XE should have Guest Shell up and running.  It should also have `python-ncclient` libraries installed on its bash shell so that the Python container can utilize NETCONF commands.  

The Python scripts that are in this Github repository should be transferred to the flash/bootflash on the IOS-XE.

Finally, the IOS-config-base.txt file contains the starting configuration that needs to be added to the running IOS-XE device on the local laptop.

Once these are setup, you can proceed to the [Intro](Intro.md) module.  

