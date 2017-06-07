## DevNet 2556 - Python on IOS-XE

### TABLE OF CONTENTS
* Module 1 - [Verifying Guest Shell Operation](www.github.com/rshoemak/DevNet2556/Module1)
* Module 2 - [Interactive Python Prompt](www.github.com/rshoemak/DevNet2556/Module2)
* Module 3 - [Python API](www.github.com/rshoemak/DevNet2556/Module3)
* Module 4 - [Python Script](www.github.com/rshoemak/DevNet2556/Module4)
* Module 5 - [Embedded Event Manager](www.github.com/rshoemak/DevNet2556/Module5)
* Module 6 - [NETCONF & YANG](www.github.com/rshoemak/DevNet2556/Module6)
* Module 7 - [Bringing It All Together](www.github.com/rshoemak/DevNet2556/Module7)


### Module 5 - Embedded Event Manager

One of the primary use cases for the Python container on IOS-XE is utilizing it in conjunction with an Embedded Event Manager (EEM) event.  

We will use the python script `eem_script.py` for this module.  

```python
import os
import sys,getopt
from datetime import datetime
import time
from cli import cli,clip

intf=sys.argv[1:]
intf = ''.join(intf[0])

if intf == loopback66;:
	cmd="conf t; int loopback66; no shut"
	cli(cmd)
else :
	cmd="conf t; int %s; no shut "%intf
	cli(cmd)
```

In order to execute this script, we need to create an EEM policy in CLI.  Copy the content from the grey box below and paste that into the device prompt.

```
conf t
event manager applet interface_Shutdown
 event syslog pattern "Interface Loopback66, changed state to administratively down"
 action 0.0 cli command "en"
 action 1.0 cli command "guestshell run python /flash/eem_script.py loop66"
!
end
```

Note how shutting down Loopback66 will automatically execute the Python script.  Let's see it in action!  Copy the commands from the grey box and paste them into the device prompt.  

```
term mon
conf t
int loop 66
shutdown
end
```
With `term mon` enabled, you can monitor the Syslog messages, and note how the Loopback interface gets shutdown, but then re-enabled as the EEM script is executed.

![alt text](https://github.com/rshoemak/DevNet2556/images/eem-script-loop-up.png)

### [Next Step - Module 6 - NETCONF & YANG](www.github.com/rshoemak/DevNet2556/Module6)
