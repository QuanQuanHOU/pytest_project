from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.remote.client_config import ClientConfig
import pytest
import yaml

@pytest.fixture(scope="class")
def init_driver(request):
    with open('config/config.yml', 'r') as f:
        config = yaml.safe_load(f)
    desired_caps = {
        'platformName': config['platformName'],
        'appPackage': config['appPackage'],
        'appActivity': config['appActivity'],
        'newCommandTimeout': config['newCommonTimeout'],
        # 'skipServerInstallation': config['skipServerInstallation'],
        'automationName': config['automationName'],
        #'systemPort': config['systemPort'],
        'deviceName': 'ppp',
        'noReset': config['noReset']
        # 'udid': 'emulator-5554',  # 根据实际情况修改
    }
    appium_server_url = f'http://localhost:{config["serverPort"]}' 
    options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote(command_executor=appium_server_url, options=options)
    driver.implicitly_wait(20)
    request.cls.driver = driver
    print('\n驱动连接成功')
    yield
    print('\ndelete session:by fixture')
    driver.quit()
    
    
    