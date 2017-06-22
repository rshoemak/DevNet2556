#!/bin/bash

sudo pip install requests
sudo yum -y update
sudo yum install -y centos-release-openstack-newton
sudo yum install -y python-ncclient
cp DevNet2556/*.py /bootflash
cp DevNet2556/IOS-config-base.txt /bootflash
exit
