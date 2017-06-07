import os
import sys,getopt
from datetime import datetime
import time
from cli import cli,clip
 
intf = sys.argv[1:]
intf = ''.join(intf[0])
 
if intf == 'loopback66':
    cmd="conf t; int loopback66; no shut"
    cli(cmd)
else:
    cmd="conf t; int %s; no shut "%intf
    cli(cmd)