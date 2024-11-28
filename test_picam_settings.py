"""
Utility script to test different picamera settings (for use on a Rpi5).
See appendix C in https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf
for avilable configs.
"""

import picamera2
from libcamera import controls

picam2 = picamera2.Picamera2()

picam2.configure(picam2.create_preview_configuration())
# Example default settings for use with IR camera + IR filter. (only sees IR hotspot)
# Don't change Brightness (artificially makes everything whiter) or Contrast (doesn't look too good)
# picam2.set_controls({"ExposureTime": 250, "AnalogueGain": 64.0, "Brightness": 0.0, "Contrast": 1.0})
print(picam2.controls)
picam2.start(show_preview=True)

while True:
    command = input("enter a config and value (space separated): ")
    config = command.split()[0]
    value = float(command.split()[1])
    if config == "ExposureTime":
        value = int(value)
    picam2.set_controls({command: value})
