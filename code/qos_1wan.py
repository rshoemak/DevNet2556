#!/usr/bin/env python

from ncclient import manager
import sys
import xml.dom.minidom as DOM
from cli import cli

HOST = '192.168.35.1'
PORT = 830
USER = 'vagrant'
PASS = 'vagrant'
NS = """
        <filter>
            <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                <interface></interface>
            </interfaces>
        </filter>
        """


class IntInfo():
    def __init__(self, name, description, enabled):
        self.name = name
        self.description = description
        self.enabled = enabled


def connect(xml_filter):
    """
    Grab running config and filter returned data based on XML Filter
    """
    with manager.connect(host=HOST, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         device_params={'name': 'default'},
                         allow_agent=False, look_for_keys=False) as m:

        return(m.get_config('running', xml_filter))


def get_int_info(int):
    name_obj = int.getElementsByTagName("name")[0]
    name = name_obj.firstChild.nodeValue

    if len(int.getElementsByTagName("description")) != 1:
        description = "empty"
    else:
        description_obj = int.getElementsByTagName("description")[0]
        description = description_obj.firstChild.nodeValue

    enabled_obj = int.getElementsByTagName("enabled")[0]
    enabled = enabled_obj.firstChild.nodeValue

    return IntInfo(name, description, enabled)


def main():
    """
    Main function
    """
    interfaces_ietf = connect(NS)

    #   if you want to see the XML parsed output, you can uncomment the line below.
    # print(DOM.parseString(interfaces_ietf.xml).toprettyxml())

    doc = DOM.parseString(interfaces_ietf.xml)
    node = doc.documentElement

    inters_ietf = doc.getElementsByTagName("interface")
    for each in inters_ietf:
        ints = get_int_info(each)
        # print("%s, description: %s,  enabled: %s" % (ints.name, ints.description, ints.enabled))

        if ints.description == 'WAN':
            if ints.enabled == 'true':
                print("Adjusting QoS Policy on interface %s" % ints.name)
                cli('conf t; int %s; no service-policy output normal-egress-shape' % ints.name)
                cli('conf t; int %s; service-policy output linkdown-egress-shape' % ints.name)


if __name__ == '__main__':
    sys.exit(main())