#!/bin/bash

if [ -d "venv" ]; then
  echo "Virtual environment exists"
else
  echo "Creating virtual environment ..."
  virtualenv --python=python2.7 venv
  echo "Virtual environment created"
fi

echo "Updating virtual environment ..."
venv/bin/pip install --default-timeout=60 -e .
venv/bin/pip install --default-timeout=60 -r requirements.txt
echo "Virtual environment updated"

echo "Updating Node dependencies ..."
npm i -g bower
npm i
echo "Node dependencies updated"

echo "Creating directories ..."
mkdir -p app/cache/plots
echo "Directories created"

echo "Creating datasets ..."
venv/bin/python data/schools/install.py
echo "Datasets created"
