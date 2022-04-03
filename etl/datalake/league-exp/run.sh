#!/bin/bash
set -e

cd /opt/datalake/league-exp

if [ ! -d "./venv" ]; then
    python3 -m venv venv
fi

source ./venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt --upgrade

python -m main
