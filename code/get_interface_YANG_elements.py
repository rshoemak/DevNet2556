#!/usr/bin/env python
#
# Get interface elements using Netconf and Cisco-IOS-XE-Native YANG model
#
# rshoemak@cisco.com
#

from ncclient import manager
import sys
import xml.dom.minidom as DOM


# the variables below assume the user is leveraging a
# Vagrant Image running IOS-XE 16.6 on local device
HOST = '192.168.35.1'
# use the NETCONF port for your IOS-XE
PORT = 830
# use the user credentials for your IOS-XE
USER = 'vagrant'
PASS = 'vagrant'


def main():
    """
    Main method that retrieves the node list of the interface node via NETCONF.
    """
    with manager.connect(host=HOST, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         device_params={'name': 'default'},
                         allow_agent=False, look_for_keys=False) as m:

        # XML filter to issue with the get operation
        interface_filter = """
                        <filter>
                            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                                <interface></interface>
                            </native>
                        </filter>
                        """

        result = m.get_config('running', interface_filter)
        print(DOM.parseString(result.xml).toprettyxml())


if __name__ == '__main__':
    sys.exit(main())