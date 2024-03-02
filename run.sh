#!/bin/bash

# Camera calibration
v4l2-ctl -d /dev/video0 --set-ctrl white_balance_temperature=4600
v4l2-ctl -d /dev/video0 --set-ctrl white_balance_automatic=1
v4l2-ctl -d /dev/video0 --set-ctrl auto_exposure=3

# Get current Unix time to avoid collision
# TODO: Something more sophisticated (e.g. counter)
TIME="${date +%s}"
echo $TIME

# OpenCV Python
cd /home/warg/image-collection/  # Update to actual path
touch logs/record_$TIME.log  # To confirm script has run
source venv/bin/activate
python -m imaging
