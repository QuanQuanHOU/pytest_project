import os
import base64
import time
from appium.webdriver.common.appiumby import AppiumBy


def input_secure_password(
    driver, image_names=["1.png", "2.png", "3.png"], pattern=[1, 2, 3, 1, 2, 3]
):
    """
    Input secure password using image-based elements
    :param driver: Appium driver instance
    :param image_names: List of image filenames
    :param pattern: Pattern of clicks (1-based index of images)
    """
    # Get base directory for images
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    image_paths = [os.path.join(current_dir, f"images/{name}") for name in image_names]

    # Read and encode images
    encoded_images = []
    for path in image_paths:
        with open(path, "rb") as file:
            encoded_images.append(base64.b64encode(file.read()).decode("UTF-8"))

    # Find elements
    elements = [driver.find_element(AppiumBy.IMAGE, img) for img in encoded_images]

    # Click according to pattern
    for idx in pattern:
        if idx == -1:
            time.sleep(0.5)
        else:
            elements[idx - 1].click()
