"""
Utility script to test different picamera settings (for use on a Rpi5).
For available settings, see appendix C: https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf
"""

import picamera2


if __name__ == "__main__":
    picam2 = picamera2.Picamera2()

    picam2.configure(picam2.create_preview_configuration())
    # Example default settings for use with IR camera + IR filter. (only sees IR hotspot)
    # Don't change Brightness (artificially makes everything whiter) or Contrast (doesn't look too good)
    # picam2.set_controls({"ExposureTime": 250, "AnalogueGain": 64.0, "Brightness": 0.0, "Contrast": 1.0})
    print(picam2.controls)
    picam2.start(show_preview=True)

    while True:
        command = input("Enter a config and value (e.g. 'ExposureTime 250'): ")

        input_tokens = command.split()
        if len(input_tokens != 2):
            print("Invalid input")
            continue

        config, raw_value = input_tokens
        value = int(raw_value) if config == "ExposureTime" else float(raw_value)

        picam2.set_controls({command: value})
        print("New controls set")
        print(picam2.controls)
