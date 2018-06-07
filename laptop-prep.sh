#!/bin/bash

sudo pip install requests
sudo pip install ncclient
cp devnet2556/code/*.py /bootflash
cp devnet2556/IOS-config-base.txt /bootflash
exit
