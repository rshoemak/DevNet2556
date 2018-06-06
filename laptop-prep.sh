#!/bin/bash

sudo pip install requests
sudo pip install ncclient
cp DevNet2556/code/*.py /bootflash
cp DevNet2556/IOS-config-base.txt /bootflash
exit
