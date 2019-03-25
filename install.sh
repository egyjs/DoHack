#!/usr/bin/env bash

## build by https://instagram.com/egy.js
## https://github.com/el3zahaby


# start install:
echo "sudo apt-get update"
sudo apt-get update

echo "installing/updatin tor"
sudo apt-get install tor

echo "installing/updatin pip"
sudo apt-get install python-pip

#pip requirements:
pip install --upgrade -r requirements.txt

# extension:
echo "installing extensions:"
git clone https://github.com/Mebus/cupp.git
