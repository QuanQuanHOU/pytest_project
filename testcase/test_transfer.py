import os
import base64
from common.base_driver import init_driver
from appium.webdriver.common.appiumby import AppiumBy


class TestSuites:

    def setup_class(self):
        print('\ninit appium:hook before test')
        self.driver = init_driver()

    def teardown_class(self):
        print('\ndelete session:hook after test')
        self.driver.quit()

    def test_transfer_success(self):
        # 定义图像文件路径
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(current_dir)
        image_path1 = os.path.join(parent_dir, "images/1.png")
        image_path2 = os.path.join(parent_dir, "images/2.png")
        image_path3 = os.path.join(parent_dir, "images/3.png")

        # 读取图像文件并进行base64编码
        with open(image_path1, 'rb') as png_file1:
            b64_data1 = base64.b64encode(png_file1.read()).decode('UTF-8')

        with open(image_path2, 'rb') as png_file2:
            b64_data2 = base64.b64encode(png_file2.read()).decode('UTF-8')

        with open(image_path3, 'rb') as png_file3:
            b64_data3 = base64.b64encode(png_file3.read()).decode('UTF-8')

        # 使用-image定位器策略查找元素并点击
        element1 = self.driver.find_element(AppiumBy.IMAGE, b64_data1)
        element2 = self.driver.find_element(AppiumBy.IMAGE, b64_data2)
        element3 = self.driver.find_element(AppiumBy.IMAGE, b64_data3)
        element1.click()
        element2.click()
        element3.click()
        element1.click()
        element2.click()
        element3.click()

        # 断言登录成功
        assert 1 == 1