#!/usr/bin/env python

from ncclient import manager
import os
import sys
try:
    from lxml import etree as ET
except ImportError:
    import xml.etree.ElementTree as ET
#import xml.dom.minidom
from cli import cli

USER = 'vagrant'
PASS = 'vagrant'
HOST = '192.168.35.1'
PORT = 830


def main():
    """
    Simple main method calling our function.
    """
    with manager.connect(host=HOST, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         device_params={'name': 'default'},
                         allow_agent=False, look_for_keys=False) as m:

        interface_filter = """
                        <filter>
                            <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                                <interface></interface>
                            </interfaces>
                        </filter>
                        """

        interfaces = m.get_config('running', interface_filter)
        #   if you want to see the XML parsed output, you can uncomment the line below.
        #print(xml.dom.minidom.parseString(interfaces.xml).toprettyxml())

        root = ET.fromstring(interfaces.xml)

        for interface in root.iter('{urn:ietf:params:xml:ns:yang:ietf-interfaces}interface'):
            for description in interface.findall('{urn:ietf:params:xml:ns:yang:ietf-interfaces}description'):
                if description.text == 'WAN':
                    name = interface.find('{urn:ietf:params:xml:ns:yang:ietf-interfaces}name')
                    status = interface.find('{urn:ietf:params:xml:ns:yang:ietf-interfaces}enabled')
                    if status.text == 'true':
                        cli('conf t; int %s; no service-policy output normal-egress-iwan8-shape' % name.text)
                        cli('conf t; int %s; service-policy output linkdown-egress-iwan8-shape' % name.text)

if __name__ == '__main__':
    sys.exit(main())