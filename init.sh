#!/bin/bash

sudo apt update -yqq

sudo apt install python3-pip -yqq

sudo apt install python3.10-venv -yqq

sudo apt install python3-virtualenv -y

python3 -m venv 3.10-venv

virtualenv --python="/home/sda/Desktop/Lambda" 3.10-venv  

source 3.10-venv/bin/activate

pip install -r requirements.txt
