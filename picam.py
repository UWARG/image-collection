"""
Taking images with a Raspberry pi camera module 3 on a Rpi on the drone.
DO NOT ACTIVATE VENV WHEN USING THIS SCRIPT, IT IS MEANT TO BE USED WITH THE DEFAULT
RASPBERRY PI LIBRARIES THAT ARE PRE-INSTALLED. Those libraries cannot be easily
installed using pip nad requires additionaly steps, so we just use the provided
library in global space.
"""

import pathlib
import time

from picamera2 import Picamera2


LOG_DIRECTORY_PATH = pathlib.Path("logs")
SAVE_PREFIX = str(pathlib.Path(LOG_DIRECTORY_PATH, "image_" + str(int(time.time())) + "_"))
DELAY = 1.0  # seconds


def main() -> None:
    """
    Main loop for capturing and saving images.
    """
    picam2 = Picamera2()
    picam2.start(show_preview=False)

    name_counter = 0
    while True:
        picam2.capture_file(f"{SAVE_PREFIX}{name_counter}.png")
        name_counter += 1

        time.sleep(DELAY)


if __name__ == "__main__":
    main()
