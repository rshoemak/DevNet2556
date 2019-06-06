## DevNet 2556 - Python on IOS-XE

### TABLE OF CONTENTS
* Module 1 - [Verifying Guest Shell Operation](Module1.md)
* Module 2 - [Interactive Python Prompt](Module2.md)
* Module 3 - [Python API](Module3.md)
* Module 4 - [Python Script](Module4.md)
* Module 5 - [Embedded Event Manager](Module5.md)
* Module 6 - [NETCONF & YANG](Module6.md)
* Module 7 - [A Deeper Look at NETCONF](Module7.md)
* Module 8 - [Bringing It All Together](Module8.md)


### Module 1 - Verifying Guest Shell Operation

The goal of this module is to demonstrate that the Guest Shell container is up and running.  The Guest Shell is an embedded Linux environment in which users can install scripts or software packages and run them.  

In this lab, we are going to be using the Guest Shell container to run Python scripts which can be a powerful add on to IOS-XE by adding enhanced functionality that is not embedded inside the operating system as it ships.

Let's start by examining the status on the router.  Copy and paste the content inside the grey box below.  

```
show iox-service
show app-hosting detail appid guestshell
```

When these commands are input into IOS-XE.  You should see the output below:

```
devnet2556#show iox-service 
Virtual Service Global State and Virtualization Limits:

Infrastructure version : 1.7
Total virtual services installed : 1
Total virtual services activated : 0

Machine types supported   : LXC
Machine types disabled    : KVM

Maximum VCPUs per virtual service : 0
Resource virtualization limits:
Name                         Quota     Committed     Available  
--------------------------------------------------------------
system CPU (%)                   7             0             7  
memory (MB)                   1024             0          1024  
bootflash (MB)               20000           120          5171  


IOx Infrastructure Summary:
---------------------------
IOx service (CAF)    : Running 
IOx service (HA)     : Not Running 
IOx service (IOxman) : Running 
Libvirtd             : Running 
```

```
devnet2556#show app-hosting detail appid guestshell
App id					   : guestshell
Owner                  : iox
State                  : RUNNING
Application
  Type                 : lxc
  Name                 : GuestShell
  Version              : 2.4.1(0.1)
  Description          : Cisco Systems Guest Shell XE fo x86
Activated profile name : custom
  
Resource reservation
  Memory               : 512 MB
  Disk                 : 1 MB
  CPU                  : 1500 units

Attached devices
  Type              Name               Alias
  ---------------------------------------------
  Serial/shell    iox_console_shell   serial0
  Serial/aux      iox_console_aux     serial1
  Serial/Syslog   iox_syslog          serial2
  Serial/Trace    iox_trace           serial3

Network interfaces
   ---------------------------------------
eth0:
   MAC address         : 52:54:dd:70:b2:e3
   IPv4 address        : 192.168.35.2
```
These indicate our Linux environment is up and running.  We can proceed to the next section of the lab.

### [Next Step - Module 2 - Interactive Python Prompt](Module2.md)