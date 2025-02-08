
import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy
from common.base_page import login
import common.utils as Utils


@pytest.mark.usefixtures("init_driver")
class TestSuites:
    
    # def setup_class(self):
    #     print('\ninit appium:hook before test')
    #     # time.sleep(10)
    #     login(self.driver)

    # def teardown_class(self):
    #     print('\ndelete session:hook after test')
    #     #self.driver.quit()

    def test_transfer_success(self):
        #进入首页并登录
        # self.driver.wait_activity("com.csii.huayi.MainActivity")
        self.driver.terminate_app("com.csii.hy")
        self.driver.activate_app("com.csii.hy")
        login(self.driver)
        # 开始测试
        el1 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.View\").instance(10)")
        el1.click()
        el2 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="className(\"android.widget.TextView\").instance(3)")
        debt_amt = el2.text
        assert Utils.is_valid_amount(debt_amt),"总资产不是有效的金额文本"
        el3 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="className(\"android.widget.TextView\").instance(6)")
        credit_amt = el3.text
        assert Utils.is_valid_amount(credit_amt),"总负债不是有效的金额文本"
        el4 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="className(\"android.widget.TextView\").instance(4)")
        debt_date = el4.text 
        assert Utils.is_date_within_deviation(debt_date),"资产金额日期不符"
        el5 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="className(\"android.widget.TextView\").instance(7)")
        credit_date = el5.text
        assert Utils.is_date_within_deviation(credit_date,1),"负债日期不符"
        el6 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="className(\"android.view.View\").instance(9)")
        assert el6.is_displayed(), "一类户不存在"
        
        el7=self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="className(\"android.widget.TextView\").instance(12)")
        # print("子元素",el7.text,el6.id)
        amt1 = el7.text
        assert Utils.is_valid_amount(amt1), "一类户金额无值"
        