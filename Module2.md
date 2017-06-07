## DevNet 2556 - Python on IOS-XE

### TABLE OF CONTENTS
* Module 1 - [Verifying Guest Shell Operation](Module1.md)
* Module 2 - [Interactive Python Prompt](Module2.md)
* Module 3 - [Python API](Module3.md)
* Module 4 - [Python Script](Module4.md)
* Module 5 - [Embedded Event Manager](Module5.md)
* Module 6 - [NETCONF & YANG](Module6.md)
* Module 7 - [Bringing It All Together](Module7.md)


### Module 2 - Interactive Python Prompt

The goal of this module is to familiarize the user with basic functionality of the Python interpreter embedded in the Linux environment of Guest Shell.  

Inside the virtual IOS-XE instance we are running, the Guest Shell container is accessed via a VirtualPortGroup.  This virtual interface provides a network and default gateway for the Guest Shell so that it can reach external resources.  

Let's jump into the Python interpreter in Guest Shell.  Copy the contents of the grey box below and paste it into the IOS-XE prompt.

```
guestshell run python
```

Note the version of Python that is embedded in IOS-XE is 2.7.5.  While it is possible to upgrade this to Python3, that is outside the scope of this lab.

```
devnet2556#guestshell run python
Python 2.7.5 (default, Jun 17 2014, 18:11:42) 
[GCC 4.8.2 20140120 (Red Hat 4.8.2-16)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

Let's start with a very basic "hello world" python script.  Copy the contents in the grey box and paste them into your console.

```
x = "hello world"
print(x)
```

You will see a very expected output.

```
>>> x = "hello world"
>>> print(x)
hello world
```

This demonstrates a very basic usage of Python.  We will proceed to a more useful Python tool in IOS-XE.

### [Next Step - Module 3 - Python API](www.github.com/rshoemak/DevNet2556/Module3)