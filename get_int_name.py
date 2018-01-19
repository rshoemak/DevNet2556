#!/usr/bin/env python
#
# Get configured interfaces using Netconf
#
# rshoemak@cisco.com
#

from ncclient import manager
import sys
import xml.dom.minidom as DOM
import cli


# the variables below assume the user is leveraging a
# Vagrant Image running IOS-XE 16.6 on local device
HOST = '192.168.35.1'
# use the NETCONF port for your IOS-XE
PORT = 830
# use the user credentials for your IOS-XE
USER = 'vagrant'
PASS = 'vagrant'

# XML namespace to be used
NS = """
    <filter>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <interface></interface>
        </native>
    </filter>
    """


# definition to grab interface information and return it
def connect(xml_filter):
    """
    definition that grabs the interface information from config via NETCONF.
    """
    with manager.connect(host=HOST, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         device_params={'name': 'default'},
                         allow_agent=False, look_for_keys=False) as m:
        with open(xml_filter) as f:
            return(m.get_config('running', f.read()))


def find_wan_int(xml):
    """
    definition that finds the WAN interface names
    """
    doc = DOM.parseString(xml)

    gigs = doc.getElementsByTagName("GigabitEthernet")
    for GE in gigs:
        name_obj = GE.getElementsByTagName("name")[0]
        description_obj = GE.getElementsByTagName("description")[0]
        description = description_obj.firstChild.data
        # find interfaces that have WAN in their description field
        if 'WAN' in description:
            print "Found WAN"
            wan_int = name_obj.firstChild.data
            return wan_int


def main():
    """
    Simple main method calling our function.
    """
    interfaces = connect(NS)
    # print(DOM.parseString(interfaces.xml).toprettyxml())

    wan_int = find_wan_int(interfaces.xml)
    print('WAN is GigabitEthernet%s' % wan_int)


if __name__ == '__main__':
    sys.exit(main())