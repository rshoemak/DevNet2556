#!/usr/bin/env python
#
# Get configured interfaces using Netconf
#
# rshoemak@cisco.com
#

from ncclient import manager
import sys
import xml.dom.minidom
try:
    from lxml import etree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import cli


# the variables below assume the user is leveraging a
# Vagrant Image running IOS-XE 16.5 on local device
HOST = '192.168.35.1'
# use the NETCONF port for your IOS-XE
PORT = 830
# use the user credentials for your IOS-XE
USER = 'vagrant'
PASS = 'vagrant'

# XML namespace to be used
NS = 'Filter.xml'

# definition to grab interface information and return it
def get_interface_info(xml_filter):
    """
    definition that grabs the interface information from config via NETCONF.
    """
    with manager.connect(host=HOST, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         device_params={'name': 'default'},
                         allow_agent=False, look_for_keys=False) as m:
        with open(xml_filter) as f:
            return(m.get_config('running', f.read()))

def get_WAN_name(root):
    """
    definiation that finds the WAN interface names
    """
    for interface in root.iter('{urn:ietf:params:xml:ns:yang:ietf-interfaces}interface'):
        for description in interface.findall('{urn:ietf:params:xml:ns:yang:ietf-interfaces}description'):
            # find interfaces that have WAN in their description field
            if description.text == 'WAN':
                print "Found WAN"
                for enabled in interface.findall('{urn:ietf:params:xml:ns:yang:ietf-interfaces}enabled'):
                    # find if the WAN interface is in an enabled state
                    if enabled.text == "true":
                        for name in interface.findall('{urn:ietf:params:xml:ns:yang:ietf-interfaces}name'):
                            WAN_Int = name.text
                            return WAN_Int


def main():
    """
    Simple main method calling our function.
    """
    interfaces = get_interface_info(NS)
    print(xml.dom.minidom.parseString(interfaces.xml).toprettyxml())

    root = ET.fromstring(interfaces.xml)

    WAN_Int = get_WAN_name(root)
    print(WAN_Int)




if __name__ == '__main__':
    sys.exit(main())