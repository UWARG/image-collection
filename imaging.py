"""
Taking images with a USB camera on a computer on the drone.
"""
import pathlib
import time

import cv2


CAMERA_NAME = 0

# TODO: Move this to configuration file
CAMERA_WIDTH = 1920
CAMERA_HEIGHT = 1200

LOG_DIRECTORY_PATH = pathlib.Path("logs")
SAVE_PREFIX = str(pathlib.Path(LOG_DIRECTORY_PATH, "image_" + str(int(time.time())) + "_"))
DELAY = 1.0  # seconds


def main() -> int:
    """
    Main function.
    """
    pathlib.Path(LOG_DIRECTORY_PATH).mkdir(exist_ok=True)

    camera = cv2.VideoCapture(CAMERA_NAME)
    if not camera.isOpened():
        with open(SAVE_PREFIX + "error.txt", "w", encoding="utf-8") as f:
            f.write(SAVE_PREFIX + "\n" + "ERROR: Failed to open camera")
        return -1

    result = camera.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
    if not result:
        with open(SAVE_PREFIX + "error.txt", "w", encoding="utf-8") as f:
            f.write(SAVE_PREFIX + "\n" + "ERROR: Failed to set camera width")
        return -1

    result = camera.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)
    if not result:
        with open(SAVE_PREFIX + "error.txt", "w", encoding="utf-8") as f:
            f.write(SAVE_PREFIX + "\n" + "ERROR: Failed to set camera height")
        return -1

    width = camera.get(cv2.CAP_PROP_FRAME_WIDTH)
    if width != CAMERA_WIDTH:
        with open(SAVE_PREFIX + "error.txt", "w", encoding="utf-8") as f:
            f.write(
                SAVE_PREFIX + "\n"
                + "ERROR: Camera width: " + str(width) + ", expected: " + str(CAMERA_WIDTH)
            )
        return -1

    height = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
    if height != CAMERA_HEIGHT:
        with open(SAVE_PREFIX + "error.txt", "w", encoding="utf-8") as f:
            f.write(
                SAVE_PREFIX + "\n"
                + "ERROR: Camera height: " + str(height) + ", expected: " + str(CAMERA_HEIGHT)
            )
        return -1

    name_counter = 0
    while True:
        result, image = camera.read()
        if not result:
            continue

        cv2.imwrite(SAVE_PREFIX + str(name_counter) + ".png", image)
        name_counter += 1

        time.sleep(DELAY)

    camera.release()

    return 0


if __name__ == "__main__":
    result_main = main()
    if result_main < 0:
        print(f"ERROR: Status code: {result_main}")

    print("Done!")
