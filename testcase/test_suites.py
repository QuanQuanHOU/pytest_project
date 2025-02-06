
import time

import pytest
from common.base_driver import init_driver
from appium.webdriver.common.appiumby import AppiumBy
from common.base_page import login


class TestSuites:
    @pytest.mark.usefixtures("init_driver")
    def setup_class(self):
        print('\ninit appium:hook before test')
        self.driver = init_driver()
        # time.sleep(10)
        login(self.driver)

    def teardown_class(self):
        print('\ndelete session:hook after test')
        self.driver.quit()

    def test_transfer_success(self):
        
        
        # 断言登录成功
        assert 1 == 1