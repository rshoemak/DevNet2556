import os
import sys,getopt
from datetime import datetime
import time
from cli import cli,clip
 
intf= sys.argv[1:]
intf = ''.join(intf[0])
 
if intf == 'loopback55':
    cmd="conf t; int loopback55; no shut "
    cli(cmd)
else :
    cmd="conf t; int %s; no shut "%intf
    cli(cmd)