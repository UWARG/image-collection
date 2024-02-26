#!/bin/bash

# Get current Unix time to avoid collision
# TODO: Something more sophisticated (e.g. counter)
TIME="${date +%s}"
echo $TIME

# FFMPEG video
cd /home/warg/image-collection/  # Update to actual path
touch logs/record_$TIME.log  # To confirm script has run
ffmpeg -f v4l2 -framerate 30 -video_size 1920x1200 -input_format mjpeg -i /dev/video0 -c copy logs/$TIME.mkv -y
