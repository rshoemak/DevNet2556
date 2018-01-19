import sys
import cli
 
intf = sys.argv[1:]
intf = ''.join(intf[0])

cli.cli("conf t; int %s; no shutdown; end" %intf)