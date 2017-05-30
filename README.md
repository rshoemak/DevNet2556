# DevNet2556
Simple scripts for running Python on IOS-XE

There are a few Python scripts on this repository to be used on conjunction with Cisco DevNet session 2556.  

get_int_ip_cli.py - A simple Python script leveraging the CLI API to collect the output of a "show ip interface brief" command

eem_script.py - This script is used on conjunction with an EEM event that monitors if a Loopback interface is "shutdown".  
  When that happens, this script uses the CLI API to bring the interface back up.
  
get_hostname.py - This script serves as an introduction to using NETCONF and demonstrates how to pull information from a NETCONF request.
  In this case, we're using the "Cisco-IOS-XE-native" YANG model and the "get_config" NETCONF request to find the hostname of the device.
  
qos_1wan.py - This script leverages both NETCONF and the CLI API and should be used in conjunction with an EEM monitoring event.  For the
 purposes of this lab, the monitoring event is a Loopback interface going "down."  However any event can serve as the trigger.
 When the script is executed, it uses NETCONF to check for interfaces witht "WAN" in the description and are enabled.  Then executes
 a QoS policy change to those interfaces.  
