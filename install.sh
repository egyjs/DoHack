#!/usr/bin/env bash

## build by https://instagram.com/egy.js
## https://github.com/el3zahaby


# start install:
sudo apt-get update
sudo apt-get install tor
sudo apt-get install python-pip

#pip requirements:
pip install --upgrade -r requirements.txt

# extension:
git clone https://github.com/Mebus/cupp.git
