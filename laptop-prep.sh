#!/usr/bin/env bash

# Copyright (c) {{current_year}} Cisco and/or its affiliates.
#
# This software is licensed to you under the terms of the Cisco Sample
# Code License, Version 1.0 (the "License"). You may obtain a copy of the
# License at
#
#               https://developer.cisco.com/docs/licenses
#
# All use of the material herein must be in accordance with the terms of
# the License. All rights not expressly granted by the License are
# reserved. Unless required by applicable law or agreed to separately in
# writing, software distributed under the License is distributed on an "AS
# IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.


echo
echo ***Update Requests***
echo
sudo pip install requests --trusted-host pypi.org --trusted-host files.pythonhosted.org

echo
echo ***Install NetConf Client***
echo
sudo pip install ncclient --trusted-host pypi.org --trusted-host files.pythonhosted.org

echo
echo ***Copy Python Files to Bootflash***
echo
cp DevNet2556/code/*.py /bootflash

echo
echo ***Copy IOS Starting Config to Bootflash***
echo
cp DevNet2556/IOS-config-base.txt /bootflash

exit
