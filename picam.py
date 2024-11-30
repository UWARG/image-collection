"""
Taking images with a Raspberry pi camera module 3 on a Rpi on the drone.
"""

import pathlib
import time

import picamera2


LOG_DIRECTORY_PATH = pathlib.Path("logs")
SAVE_PREFIX = str(pathlib.Path(LOG_DIRECTORY_PATH, "image_" + str(int(time.time())) + "_"))
DELAY = 1.0  # seconds


def main() -> None:
    """
    Main loop for capturing and saving images.
    """
    picam2 = picamera2.Picamera2()
    picam2.start(show_preview=False)

    name_counter = 0
    while True:
        picam2.capture_file(f"{SAVE_PREFIX}{name_counter}.png")
        name_counter += 1

        time.sleep(DELAY)


if __name__ == "__main__":
    LOG_DIRECTORY_PATH.mkdir(parents=True, exist_ok=True)
    main()
