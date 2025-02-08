import os
import base64
import time
import re
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
            
def is_valid_amount(text):
    """
    判断文本是否是有效的金额数值。
    
    参数:
        text (str): 要检查的文本。
    
    返回:
        bool: 如果文本是有效的金额数值，返回 True；否则返回 False。
    """
    # 定义金额的正则表达式
    amount_pattern = r'^[￥¥]\s*[-+]?\d{1,3}(,\d{3})*(\.\d+)?$'
    
    # 使用正则表达式匹配文本
    if re.match(amount_pattern, text):
        return True
    else:
        return False

from datetime import datetime, timedelta

def is_date_within_deviation(input_date_str, deviation_days = 0):
    """
    判断输入的日期是否在与今天日期的偏差天数范围内，并检查日期格式的合法性。

    参数:
        input_date_str (str): 输入的日期字符串，格式应为 "YYYY-MM-DD"。
        deviation_days (int): 与今天日期的偏差天数。

    返回:
        bool: 如果输入的日期格式合法且在指定的偏差天数范围内，返回 True；否则返回 False。
    """
    try:
        # 尝试将输入的日期字符串转换为日期对象
        input_date = datetime.strptime(input_date_str, "%Y-%m-%d").date()
    except ValueError:
        # 如果转换失败，说明输入的日期格式不合法
        return False
    
    # 获取今天的日期
    today = datetime.today().date()
    
    # 计算偏差范围的开始日期和结束日期
    exp_date = today - timedelta(days=deviation_days)
    
    # 判断输入的日期是否在偏差范围内
    return input_date == exp_date
