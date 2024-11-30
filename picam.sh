#!/bin/bash

# Get current Unix time to avoid collision
# TODO: Something more sophisticated (e.g. counter)
TIME="${date +%s}"
echo $TIME

# Picamera Python
cd /home/warg/image-collection  # Update to actual path
touch logs/record_$TIME.log  # To confirm script has run
source venv/bin/activate
python picam.py &
