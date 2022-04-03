#!/bin/bash
set -e

#cd /opt/datalake/league-exp

if [ ! -d "./venv" ]; then
    python -m venv venv
fi

source ./venv/Scripts/activate
#pip install --upgrade pip
pip install -r requirements.txt --upgrade

python -m main
