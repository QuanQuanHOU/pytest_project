import time
from appium.webdriver.common.appiumby import AppiumBy

from common.utils import input_secure_password

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


def login_android_full(driver, username="U282546219"):
    el1 = driver.find_element(by=AppiumBy.ID, value="com.csii.hy:id/tv_userinfo")
    el1.click()
    el2 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
    el2.send_keys(username)
    el3 = driver.find_element(
        by=AppiumBy.ANDROID_UIAUTOMATOR,
        value='new UiSelector().className("android.widget.TextView").instance(3)',
    )
    el3.click()
    el4 = driver.find_element(
        by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().resourceId("password")'
    )
    el4.click()
    input_secure_password(
        driver,
        [
            "123.png",
            "11.png",
            "22.png",
            "33.png",
            "abc.png",
            "q.png",
            "w.png",
            "e.png",
            "confirm.png",
        ],
        [1, -1, 2, 3, 4, 5, -1, 6, 7, 8, 9],
    )
    # todo --点击登陆按钮，确认一系列条款等等


def login(driver):
    el1 = driver.find_element(by=AppiumBy.ID, value="com.csii.hy:id/tv_userinfo")
    el1.click()
    # time.sleep(1)
    # el2 = driver.find_element(
    #     by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("切换登录方式")'
    # )
    # el2.click()
    # el3 = driver.find_element(
    #     by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("手势登录")'
    # )
    # el3.click()
    # Get coordinates of pattern points
    elem_a = driver.find_element(
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@resource-id="com.csii.hy:id/lock_9_view"]/android.view.View[2]',
    )
    elem_b = driver.find_element(
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@resource-id="com.csii.hy:id/lock_9_view"]/android.view.View[8]',
    )
    elem_c = driver.find_element(
        AppiumBy.XPATH,
        '//android.view.ViewGroup[@resource-id="com.csii.hy:id/lock_9_view"]/android.view.View[9]',
    )

    coord_a = elem_a.location
    coord_b = elem_b.location
    coord_c = elem_c.location

    # Create and execute touch action for pattern
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(
        driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
    )
    actions.w3c_actions.pointer_action.move_to_location(coord_a["x"], coord_a["y"])
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(coord_b["x"], coord_b["y"])
    actions.w3c_actions.pointer_action.move_to_location(coord_c["x"], coord_c["y"])
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    # time.sleep(15)
    el4 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"下次提醒\")")
    el4.click()
    # time.sleep(5)
    # el5 = driver.find_element(by=AppiumBy.ID, value="com.csii.hy:id/img_close")
    # el5.click()
