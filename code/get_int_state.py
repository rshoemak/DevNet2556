#!/usr/bin/env python
#
# Get configured interfaces using Netconf
#
# rshoemak@cisco.com
#

from ncclient import manager
import sys
import xml.dom.minidom as DOM
#import cli


# the variables below assume the user is leveraging a
# Vagrant Image running IOS-XE 16.7 on local device
HOST = '127.0.0.1'
# use the NETCONF port for your IOS-XE
PORT = 2223
# use the user credentials for your IOS-XE
USER = 'vagrant'
PASS = 'vagrant'

# XML namespace to be used
NS1 = 'ietf-Interfaces-Filter.xml'
NS2 = 'ietf-Int-States-Filter.xml'


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

    gigs = doc.getElementsByTagName("interface")
    for GE in gigs:
        name_obj = GE.getElementsByTagName("name")[0]
        description_obj = GE.getElementsByTagName("description")[0]
        description = description_obj.firstChild.data
        # find interfaces that have WAN in their description field
        if 'WAN' in description:
            print "Found WAN"
            wan_int = name_obj.firstChild.data
            return wan_int


def find_wan_state(xml_filter):
    """
    definition that finds if WAN is operational
    """
    with manager.connect(host='127.0.0.1', port=2223, username='vagrant',
                         password='vagrant', hostkey_verify=False,
                         device_params={'name': 'default'},
                         allow_agent=False, look_for_keys=False) as m:

        with open(xml_filter) as f:
            result = m.get(f.read())
            print(DOM.parseString(result.xml).toprettyxml())
        '''
        doc = DOM.parseString(result.xml)

        ints = doc.getElementsByTagName("interface")
        for each in ints:
            name_obj = each.getElementsByTagName("name")[0]
            print(name_obj)
            name = name_obj.firstChild.data
            print(name)
            if 'name' == 'GigabitEthernet1':
                state_obj = each.getElementsByTagName("oper-status")[0]
                state = state_obj.firstChild.data
            else:
                state = "invalid"
            return state'''


def main():
    """
    Simple main method calling our function.
    """
    #interfaces = connect(NS1)
    # print(DOM.parseString(interfaces.xml).toprettyxml())
    #wan_int = find_wan_int(interfaces.xml)
    #print(wan_int)

    #wan_state = find_wan_state()
    #print(wan_state)
    find_wan_state(NS2)

if __name__ == '__main__':
    sys.exit(main())